# infrastructure/repositories/project.py

import logging
from typing import Optional

import aiosqlite
from aiosqlite.core import Error as SqliteError
from domain.models.project.entity import Project
from domain.repositories.project import ProjectRepository
from domain.exceptions import ProjectCreationError

logger = logging.getLogger(__name__)


class SqliteProjectRepository(ProjectRepository):
    def __init__(self, db_path: str):
        self._db_path = db_path

    async def save(self, project: Project) -> None:
        async with aiosqlite.connect(self._db_path) as conn:
            await conn.execute("BEGIN")
            try:
                cursor = await conn.execute('''
                    INSERT INTO project (
                        project_name, description, creator_id, created_at, updated_at
                    ) VALUES (?, ?, ?, ?, ?)
                ''', (
                    project.project_name,
                    project.description,
                    project.user_id,
                    project.created_at,
                    project.updated_at
                ))
                project.id = cursor.lastrowid
                await conn.commit()
            except SqliteError as e:
                await conn.rollback()
                logger.exception("Project Saving failed")
                raise ProjectCreationError("Failed to create project")
            except Exception as e:
                await conn.rollback()
                logger.exception("Unexpected error while creating project")
                raise ProjectCreationError("Failed to create project")

    async def get_project_by_id(self, project_id: int) -> Optional[Project]:
        async with aiosqlite.connect(self._db_path) as conn:
            try:
                cursor = await conn.execute('''
                    SELECT id, name, description, created_at, updated_at 
                    FROM projects 
                    WHERE id = ?
                ''', (project_id))
                row = await cursor.fetchone()

                if row is None:
                    return None

                return Project(
                    id=row[0],
                    name=row[1],
                    description=row[2],
                    created_at=row[3],
                    updated_at=row[4],
                    user_id=user_id
                )
            except SqliteError as e:
                logger.exception("Failed to fetch project")
                return None
