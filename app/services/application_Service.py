import math
from uuid import UUID

from sqlalchemy.orm import Session

from app.core.dependencies import require_company_membership
from app.core.exceptions import (
    ApplicationAlreadyExistsError,
    ApplicationNotFoundError,
    ForbiddenError,
    JobNotFoundError,
    StatusCannotBeSameError,
)
from app.models.application import Application, ApplicationStatus
from app.models.job import JobStatus
from app.models.user import User, UserRole
from app.repositories.application_repository import (
    create,
    get_by_candidate_id,
    get_by_id,
    get_by_job_and_candidate,
    get_by_job_id,
    update_application,
)
from app.repositories.job_repository import get_job_by_id
from app.schemas.application import (
    ApplicationCreate,
    ApplicationListResponse,
    ApplicationResponse,
    ApplicationStatusUpdate,
)


def apply_for_job(
    db: Session, job_id: UUID, payload: ApplicationCreate, current_user: User
) -> ApplicationResponse:
    job = get_job_by_id(db, job_id)
    if job is None or job.status != JobStatus.PUBLISHED or not job.is_active:
        raise JobNotFoundError

    existing_application = get_by_job_and_candidate(db, job_id, current_user.id)
    if existing_application is not None:
        raise ApplicationAlreadyExistsError

    application = Application(
        job_id=job.id,
        candidate_id=current_user.id,
        resume_url=payload.resume_url,
        cover_letter=payload.cover_letter,
    )

    created_application = create(db, application)
    return ApplicationResponse.model_validate(created_application)


def get_my_applications( db: Session, current_user: User, page: int, page_size: int, application_status: ApplicationStatus | None = None) -> ApplicationListResponse:
    applications, total = get_by_candidate_id(db, current_user.id, page, page_size, application_status)
    total_pages = math.ceil(total / page_size)

    return ApplicationListResponse(
        items=[ApplicationResponse.model_validate(application) for application in applications],
        page=page,
        page_size=page_size,
        total_pages=total_pages,
        total=total,
    )


def get_job_applications(
    db: Session,
    job_id: UUID,
    current_user: User,
    page: int,
    page_size: int,
    application_status: ApplicationStatus | None,
) -> ApplicationListResponse:
    job = get_job_by_id(db, job_id)

    if job is None:
        raise JobNotFoundError

    require_company_membership(db, job.company_id, current_user)
    applications, total = get_by_job_id(db, job_id, page, page_size, application_status)
    total_pages = math.ceil(total / page_size)

    return ApplicationListResponse(
        items=[
            ApplicationResponse.model_validate(application)
            for application in applications
        ],
        page=page,
        page_size=page_size,
        total_pages=total_pages,
        total=total,
    )


def update_application_status(
    db: Session,
    application_id: UUID,
    payload: ApplicationStatusUpdate,
    current_user: User,
) -> ApplicationResponse:
    application = get_by_id(db, application_id)
    if application is None:
        raise ApplicationNotFoundError

    job = get_job_by_id(db, application.job_id)
    if job is None:
        raise JobNotFoundError

    require_company_membership(db, job.company_id, current_user)
        
    if application.status == payload.status:
        raise StatusCannotBeSameError

    application.status = payload.status
    updated_application = update_application(db, application)
    return ApplicationResponse.model_validate(updated_application)


def withdraw_application(
    db: Session, application_id: UUID, current_user: User
) -> ApplicationResponse:
    application = get_by_id(db, application_id)
    if application is None:
        raise ApplicationNotFoundError

    if application.candidate_id != current_user.id:
        raise ForbiddenError

    application.status = ApplicationStatus.WITHDRAWN
    updated_application = update_application(db, application)
    return ApplicationResponse.model_validate(updated_application)
