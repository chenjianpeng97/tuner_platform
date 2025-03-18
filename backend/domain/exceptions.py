class DomainError(Exception):
    """Base exception for all domain errors"""


class ProjectError(DomainError):
    """Base exception for project-related errors"""

class ProjectNameError(DomainError):
    """Raised when a project name is invalid"""
class ProjectNotFoundError(ProjectError):
    """Raised when a project is not found"""


class ProjectCreationError(ProjectError):
    """Raised when a project creation fails"""
