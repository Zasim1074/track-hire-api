from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_active_user
from app.db.session import get_db
from app.models.user import User
from app.schemas.interview import (
    InterviewCreate,
    InterviewResponse,
)
from app.services import interview_service

router = APIRouter()
db_dependency = Depends(get_db)
user_dependency = Depends(get_current_active_user)


@router.post("/applications/{application_id}", response_model=InterviewResponse, status_code=status.HTTP_201_CREATED)
def create_interview(application_id: UUID, payload: InterviewCreate, db: Session = db_dependency, current_user: User = user_dependency):
    return interview_service.create_interview(db, application_id, payload, current_user)