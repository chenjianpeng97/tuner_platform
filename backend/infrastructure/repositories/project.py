from typing import Optional
from abc import ABC, abstractmethod

from sqlalchemy.orm import Session

from domain.models.project.entity import Project
from infrastructure.database.models import ProjectDB
from domain.repositories.project import ProjectRepository


class SQLAlchemyProjectRepository(ProjectRepository):
    def __init__(self, db: Session):
        self.db = db

    def save(self, project: Project) -> Optional[Project]:
        """
        保存 Project 对象到数据库
        """
        project_db = self.db.query(ProjectDB).filter(ProjectDB.id == project.id).first()

        if project_db:
            # 更新已存在的 Project
            for key, value in project.dict(exclude={"id"}).items():
                setattr(project_db, key, value)
        else:
            # 创建新的 Project
            project_db = ProjectDB(**project.dict(exclude_unset=True))
            self.db.add(project_db)

        self.db.commit()
        self.db.refresh(project_db)
        return Project.from_orm(project_db)  # 从数据库模型创建 Pydantic 模型

    def get_project_by_id(self, project_id: int) -> Optional[Project]:
        """
        根据 ID 获取 Project 对象
        """
        project_db = self.db.query(ProjectDB).filter(ProjectDB.id == project_id).first()
        if project_db:
            return Project.from_orm(project_db)  # 从数据库模型创建 Pydantic 模型
        return None

    def get_project_by_name(self, project_name: str) -> Optional[Project]:
        """
        根据项目名称获取项目
        """
        project_db = self.db.query(ProjectDB).filter(ProjectDB.project_name == project_name).first()
        if project_db:
            return Project.from_orm(project_db)
        return None
