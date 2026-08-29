from fastapi import FastAPI

from app.api.application import router as application_router
from app.api.auth import router as auth_router
from app.api.candidate_profile import router as candidate_profile_router
from app.api.company import router as company_router
from app.api.company_membership import router as company_membership_router
from app.api.job import router as job_router
from app.api.user import router as user_router
from app.core.exceptions import (
    ApplicationAlreadyExistsError,
    ApplicationNotFoundError,
    CandidateProfileAlreadyExistsError,
    CandidateProfileNotFoundError,
    CannotDeleteCompanyError,
    CompanyAlreadyExistsError,
    CompanyNotFoundError,
    EmailAlreadyExistsError,
    ForbiddenError,
    InactiveUserError,
    InvalidCredentialsError,
    JobNotFoundError,
    MembershipAlreadyExistsError,
    MembershipNotFoundError,
    StatusCannotBeSameError,
)
from app.core.exceptions_handler import (
    application_already_exists_handler,
    application_not_found_handler,
    candidate_profile_already_exists_handler,
    candidate_profile_not_found_handler,
    cannot_delete_company_handler,
    company_already_exist_handler,
    company_not_found_handler,
    email_exists_handler,
    forbidden_handler,
    inactive_user_handler,
    invalid_credentials_handler,
    job_not_found_handler,
    membership_already_exists_handler,
    membership_not_found_handler,
    status_cannot_be_same_handler,
)

app = FastAPI(
    title="track-hire-api",
    version="1.0.0",
    description="User based(Admin, HR & Candidate) workflow with proper Authentication and Authorization",
)

app.add_exception_handler(EmailAlreadyExistsError, email_exists_handler)
app.add_exception_handler(ForbiddenError, forbidden_handler)
app.add_exception_handler(InvalidCredentialsError, invalid_credentials_handler)
app.add_exception_handler(InactiveUserError, inactive_user_handler)
app.add_exception_handler(CompanyAlreadyExistsError, company_already_exist_handler)
app.add_exception_handler(CompanyNotFoundError, company_not_found_handler)
app.add_exception_handler(JobNotFoundError, job_not_found_handler)
app.add_exception_handler(CannotDeleteCompanyError, cannot_delete_company_handler)
app.add_exception_handler(ApplicationAlreadyExistsError, application_already_exists_handler)
app.add_exception_handler(ApplicationNotFoundError, application_not_found_handler)
app.add_exception_handler(StatusCannotBeSameError, status_cannot_be_same_handler)
app.add_exception_handler(MembershipAlreadyExistsError, membership_already_exists_handler)
app.add_exception_handler(MembershipNotFoundError, membership_not_found_handler)
app.add_exception_handler(CandidateProfileAlreadyExistsError, candidate_profile_already_exists_handler)
app.add_exception_handler(CandidateProfileNotFoundError, candidate_profile_not_found_handler)

app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(company_router, prefix="/companies", tags=["Companies"])
app.include_router(job_router, prefix="/api", tags=["Jobs"])
app.include_router(application_router, prefix="/api", tags=["Applications"])
app.include_router(company_membership_router, prefix="/companies", tags=["Company Members"])
app.include_router(candidate_profile_router, prefix="/candidates", tags=["Candidate Profile"])