# application/services/project.py

from domain.models.project.entity import Project
from domain.models.user.entity import User
from domain.repositories.project import ProjectRepository
from application.services.authentication import AuthenticationService
from domain.exceptions import ProjectNameError


class ProjectService:
    def __init__(
            self,
            project_repository: ProjectRepository,
            authentication_service: AuthenticationService
    ):
        self._project_repository = project_repository
        self._authentication_service = authentication_service

    async def create_project(
            self,
            creator: User,
            project_name: str,
            description: str | None = None
    ) -> Project:
        # 验证项目名称是否已存在
        existing_project = await self._project_repository.get_project_by_name(project_name)
        if existing_project:
            raise ProjectNameError("项目名称已存在")

        # 验证创建者信息
        if not creator or not creator.id:
            raise ValueError("创建者信息不能为空")

        # 创建并保存项目
        project = Project(
            project_name=project_name,
            description=description,
        )
        project.validate_project_name()
        return await self._project_repository.save(project)
