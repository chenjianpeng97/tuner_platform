from abc import ABC, abstractmethod
from typing import Optional
from domain.models.project.entity import Project


class ProjectRepository(ABC):
    @abstractmethod
    def save(self, project: Project) -> Optional[None]:
        pass

    @abstractmethod
    def get_project_by_id(self, user_id: int) -> Optional[Project]:
        pass
