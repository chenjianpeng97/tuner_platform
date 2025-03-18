from abc import ABC, abstractmethod
from typing import Optional
from domain.models.project.entity import Project


class ProjectRepository(ABC):
    @abstractmethod
    def save(self, project: Project) -> Optional[None]:
        pass

    @abstractmethod
    def get_project_by_id(self, project_id: int) -> Optional[Project]:
        pass

    @abstractmethod
    def get_project_by_name(self, project_name: str) -> Optional[Project]:
        """根据项目名称获取项目

        Args:
            project_name: 项目名称

        Returns:
            Optional[Project]: 项目实体，如果不存在则返回None
        """
        pass
