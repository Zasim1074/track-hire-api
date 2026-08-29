class EmailAlreadyExistsError(Exception):
    pass


class InvalidCredentialsError(Exception):
    pass


class InactiveUserError(Exception):
    pass


class ForbiddenError(Exception):
    pass


class CompanyAlreadyExistsError(Exception):
    pass


class CompanyNotFoundError(Exception):
    pass


class CannotDeleteCompanyError(Exception):
    pass


class JobNotFoundError(Exception):
    pass


class ApplicationNotFoundError(Exception):
    pass


class ApplicationAlreadyExistsError(Exception):
    pass


class StatusCannotBeSameError(Exception):
    pass


class MembershipAlreadyExistsError(Exception):
    pass


class MembershipNotFoundError(Exception):
    pass


class CandidateProfileAlreadyExistsError(Exception):
    pass


class CandidateProfileNotFoundError(Exception):
    pass


class ResumeNotFoundError(Exception):
    pass