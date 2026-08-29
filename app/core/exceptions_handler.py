from fastapi import Request
from fastapi.responses import JSONResponse

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
    ResumeNotFoundError,
    StatusCannotBeSameError,
)


async def email_exists_handler(request:Request, exc: EmailAlreadyExistsError ):
    return JSONResponse(status_code=409, content={"detail" : "Email is already registered."})

async def invalid_credentials_handler(request:Request, exc:InvalidCredentialsError):
    return JSONResponse(status_code=401, content={"detail" : "Invalid Credentials."})

async def inactive_user_handler(request:Request, exc:InactiveUserError):
    return JSONResponse(status_code=403, content={"detail" : "User is inactive."})

async def forbidden_handler(request:Request, exc:ForbiddenError):
    return JSONResponse(status_code=401, content={"details" : "You don't have enough permissions."})

async def company_already_exist_handler(request: Request, exc:CompanyAlreadyExistsError):
    return JSONResponse(status_code=409, content={"details" : "Company with this website already exists."})

async def company_not_found_handler(request:Request, exc:CompanyNotFoundError):
    return JSONResponse(status_code=404, content={"details" : "Company doesn't exist."})

async def cannot_delete_company_handler(request:Request, exc: CannotDeleteCompanyError):
    return JSONResponse(status_code=409, content={"details" : "Company can't deleted because there are jobs listed."})

async def job_not_found_handler(request:Request, exc:JobNotFoundError):
    return JSONResponse(status_code=404, content={"details" : "Job doesn't exist."})

async def application_not_found_handler(request:Request, exc:ApplicationNotFoundError):
    return JSONResponse(status_code=404, content={"details" : "Application doesn't exist."})

async def application_already_exists_handler(request:Request, exc:ApplicationAlreadyExistsError):
    return JSONResponse(status_code=409, content={"details" : "Application already exists"})

async def status_cannot_be_same_handler(request:Request, exc: StatusCannotBeSameError):
    return JSONResponse(status_code=409, content={"details" : "Please update the status, new one can't be same."})

async def membership_already_exists_handler(request:Request, exc:MembershipAlreadyExistsError):
    return JSONResponse(status_code=409, content={"details" : "You already have a membership."})

async def membership_not_found_handler(request:Request, exc:MembershipNotFoundError):
    return JSONResponse(status_code=404, content={"detatils" : "Membership doesn't exist."})

async def candidate_profile_already_exists_handler(request:Request, exc: CandidateProfileAlreadyExistsError):
    return JSONResponse(status_code=409, content={"details" : "Candidate profile already exists."})

async def candidate_profile_not_found_handler(request:Request, exc:CandidateProfileNotFoundError):
    return JSONResponse(status_code=404, content={"details" : "Profile doesn't exist."})

async def resume_not_found_handler(request:Request, exc:ResumeNotFoundError):
    return JSONResponse(status_code=404, content={"details" : "Resume doesn't exist."})