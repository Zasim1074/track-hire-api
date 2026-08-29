import uuid

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_active_user
from app.db.session import get_db
from app.models.user import User
from app.services import resume_service

router = APIRouter()

db_dependency = Depends(get_db)
user_dependency = Depends(get_current_active_user)


@router.get("/me")
def get_my_resumes(db: Session = db_dependency, current_user: User = user_dependency):
    return resume_service.get_my_resumes(db, current_user)
    
    
@router.get("/{resume_id}")
def get_resume(resume_id: uuid.UUID, db: Session = db_dependency, current_user: User = user_dependency):
    return resume_service.get_resume(db, resume_id, current_user)