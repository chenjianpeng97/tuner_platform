class DomainError(Exception):
    """Base exception for all domain errors"""
class ProjectError(DomainError):
    """Base exception for project-related errors"""
class ProjectNotFoundError(ProjectError):
    """Raised when a project is not found"""