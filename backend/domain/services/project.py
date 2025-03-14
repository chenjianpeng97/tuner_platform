"""项目领域服务"""
from typing import List, Optional

from domain.models.project.entity import Project
from domain.models.auth.entity import User
from domain.models.test.entity import TestRun
from domain.repositories.project_repository import ProjectRepository
from domain.repositories.user_repository import UserRepository
from domain.repositories.test_repository import TestRepository

class ProjectService:
    """项目领域服务"""
    
    def __init__(
        self,
        project_repository: ProjectRepository,
        user_repository: UserRepository,
        test_repository: TestRepository
    ):
        self.project_repository = project_repository
        self.user_repository = user_repository
        self.test_repository = test_repository
    @classmethod
    def get_project_creator(self, project: int) -> Optional[User]:
        """获取项目及其创建者信息
        
        Args:
            project: 项目实体
            
        Returns:
            项目的创建者,如果创建者不存在则返回None
        """
        return self.user_repository.get_by_id(project.creator_id)
    
    def get_project_with_test_runs(self, project_id: int) -> Optional[Project]:
        """获取项目及其测试运行信息
        
        Args:
            project_id: 项目ID
            
        Returns:
            包含测试运行信息的项目实体，如果项目不存在则返回None
        """
        project = self.project_repository.get_by_id(project_id)
        if not project:
            return None
            
        test_runs = self.test_repository.get_by_project_id(project_id)
        project.test_runs = test_runs
            
        return project
    
    def get_project_with_all_relations(self, project_id: int) -> Optional[Project]:
        """获取项目及其所有关联信息（创建者和测试运行）
        
        Args:
            project_id: 项目ID
            
        Returns:
            包含所有关联信息的项目实体，如果项目不存在则返回None
        """
        project = self.get_project_with_creator(project_id)
        if not project:
            return None
            
        test_runs = self.test_repository.get_by_project_id(project_id)
        project.test_runs = test_runs
            
        return project