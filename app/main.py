from fastapi import FastAPI

from app.api.application import router as application_router
from app.api.auth import router as auth_router
from app.api.candidate_profile import router as candidate_profile_router
from app.api.company import router as company_router
from app.api.company_membership import router as company_membership_router
from app.api.interview import router as interview_router
from app.api.interview_feedback import router as interview_feedback_router
from app.api.job import router as job_router
from app.api.resume import router as resume_router
from app.api.user import router as user_router
from app.core import exceptions, exceptions_handler

app = FastAPI(
    title="track-hire-api",
    version="1.0.0",
    description="User based(Admin, HR & Candidate) workflow with proper Authentication and Authorization",
)

app.add_exception_handler(exceptions.EmailAlreadyExistsError, exceptions_handler.email_exists_handler)
app.add_exception_handler(exceptions.ForbiddenError, exceptions_handler.forbidden_handler)
app.add_exception_handler(exceptions.InvalidCredentialsError, exceptions_handler.invalid_credentials_handler)
app.add_exception_handler(exceptions.InactiveUserError, exceptions_handler.inactive_user_handler)
app.add_exception_handler(exceptions.CompanyAlreadyExistsError, exceptions_handler.company_already_exist_handler)
app.add_exception_handler(exceptions.CompanyNotFoundError, exceptions_handler.company_not_found_handler)
app.add_exception_handler(exceptions.JobNotFoundError, exceptions_handler.job_not_found_handler)
app.add_exception_handler(exceptions.CannotDeleteCompanyError, exceptions_handler.cannot_delete_company_handler)
app.add_exception_handler(exceptions.ApplicationAlreadyExistsError, exceptions_handler.application_already_exists_handler)
app.add_exception_handler(exceptions.ApplicationNotFoundError, exceptions_handler.application_not_found_handler)
app.add_exception_handler(exceptions.StatusCannotBeSameError, exceptions_handler.status_cannot_be_same_handler)
app.add_exception_handler(exceptions.MembershipAlreadyExistsError, exceptions_handler.membership_already_exists_handler)
app.add_exception_handler(exceptions.MembershipNotFoundError, exceptions_handler.membership_not_found_handler)
app.add_exception_handler(exceptions.CandidateProfileAlreadyExistsError, exceptions_handler.candidate_profile_already_exists_handler)
app.add_exception_handler(exceptions.CandidateProfileNotFoundError, exceptions_handler.candidate_profile_not_found_handler)
app.add_exception_handler(exceptions.ResumeNotFoundError, exceptions_handler.resume_not_found_handler)
app.add_exception_handler(exceptions.AlreadyAppliedError, exceptions_handler.already_applied_handler)
app.add_exception_handler(exceptions.JobNotAcceptingApplicationsError, exceptions_handler.job_not_accepting_applications_handler)
app.add_exception_handler(exceptions.InvalidApplicationStatusTransitionError, exceptions_handler.invalid_application_status_transition_handler)
app.add_exception_handler(exceptions.InterviewConflictError, exceptions_handler.interview_conflict_handler)





app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(application_router, prefix="/api", tags=["Applications"])
app.include_router(job_router, prefix="/api", tags=["Jobs"])
app.include_router(candidate_profile_router, prefix="/candidates", tags=["Candidate Profile"])
app.include_router(company_router, prefix="/companies", tags=["Companies"])
app.include_router(company_membership_router, prefix="/companies", tags=["Company Members"])
app.include_router(resume_router, prefix="/resumes", tags=["Resumes"])
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(interview_router, prefix="/interviews",tags=["Interviews"])
app.include_router(interview_feedback_router)