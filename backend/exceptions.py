class DomainError(Exception):
    """Base exception for all domain errors"""
    pass
class DefineError(DomainError):
    """Base exception for define-related errors"""
    pass
class FeatureFormatError(DefineError):
    """Raised when a feature can't be parsed correctly"""
    pass 
class TestError(DomainError):
    """Base exception for test-related errors"""
    pass