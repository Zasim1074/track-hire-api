from uuid import UUID

from sqlalchemy.orm import Session

from app.core.dependencies import require_company_membership
from app.core.exceptions import (
    ApplicationNotFoundError,
    ForbiddenError,
    InterviewConflictError,
    InterviewerNotEligibleError,
    InterviewerNotFoundError,
    InterviewNotAllowedError,
)
from app.models.application import ApplicationStatus
from app.models.application_history import ApplicationStatusHistory
from app.models.company_membership import MembershipRole
from app.models.interview import Interview, InterviewStatus
from app.models.user import User, UserRole
from app.repositories.application_repository import get_by_id as get_application_by_id
from app.repositories.interview_repository import (
    create,
    has_conflict,
)
from app.repositories.user_repository import get_by_id as get_user_by_id
from app.schemas.interview import InterviewCreate, InterviewResponse


def create_interview(
    db: Session,
    application_id: UUID,
    payload: InterviewCreate,
    current_user: User,
) -> InterviewResponse:

    application = get_application_by_id(
        db,
        application_id,
    )

    if application is None:
        raise ApplicationNotFoundError

    if current_user.role not in {
        MembershipRole.HR,
        UserRole.ADMIN,
    }:
        raise ForbiddenError

    if current_user.role == MembershipRole.HR:
        require_company_membership(
            db,
            application.job.company_id,
            current_user,
        )

    if application.status != ApplicationStatus.SHORTLISTED:
        raise InterviewNotAllowedError

    interviewer = get_user_by_id(
        db,
        payload.interviewer_id,
    )

    if interviewer is None:
        raise InterviewerNotFoundError

    if interviewer.role != MembershipRole.HR:
        raise InterviewerNotEligibleError

    require_company_membership(
        db,
        application.job.company_id,
        interviewer,
    )

    if has_conflict(
        db,
        interviewer.id,
        payload.scheduled_at,
        payload.duration_minutes,
    ):
        raise InterviewConflictError

    # Create interview
    interview = Interview(
        application_id=application.id,
        interviewer_id=interviewer.id,
        scheduled_at=payload.scheduled_at,
        duration_minutes=payload.duration_minutes,
        meeting_url=payload.meeting_url,
        interview_type=payload.interview_type,
        status=InterviewStatus.SCHEDULED,
        notes=payload.notes,
    )

    db.add(interview)

    # Update application status
    old_status = application.status

    application.status = ApplicationStatus.INTERVIEW

    # Create status history
    history = ApplicationStatusHistory(
        application_id=application.id,
        from_status=old_status,
        to_status=ApplicationStatus.INTERVIEW,
        changed_by=current_user.id,
        notes="Interview scheduled.",
    )

    db.add(history)

    # One transaction
    db.commit()

    db.refresh(interview)

    return InterviewResponse.model_validate(interview)