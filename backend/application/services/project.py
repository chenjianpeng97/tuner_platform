# application/services/project.py

from typing import List

from domain.models.project.entity import Project
from domain.models.user.entity import User
from domain.repositories.project import ProjectRepository


class ProjectService:
    def __init__(
            self,
            project_repository: ProjectRepository,
    ):
        self._project_repository = project_repository

    async def create_project(
            self,
            creator: User,
            project_name: str
    ) -> Project:
        # Create and save project
        project = Project(creator_id=User.id, project_name=project_name)
        await self._project_repository.save(project)
        return project
