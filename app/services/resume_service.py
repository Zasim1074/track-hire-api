import uuid

from sqlalchemy.orm import Session

from app.core.exceptions import ForbiddenError, ResumeNotFoundError
from app.models.user import User, UserRole
from app.repositories.resume_repository import get_by_candidate, get_by_id
from app.schemas.resume import ResumeResponse


def get_my_resumes(db: Session, current_user: User) -> list[ResumeResponse]:
    if current_user.role != UserRole.CANDIDATE:
        raise ForbiddenError

    resumes = get_by_candidate(db, current_user.id)

    return [ResumeResponse.model_validate(resume) for resume in resumes]


def get_resume(db: Session, resume_id: uuid.UUID, current_user: User) -> ResumeResponse:
    resume = get_by_id(db, resume_id)

    if resume is None:
        raise ResumeNotFoundError

    if current_user.role != UserRole.ADMIN and resume.candidate_id != current_user.id:
        raise ForbiddenError

    return ResumeResponse.model_validate(resume)
