# interface/dependencies.py

from fastapi import Depends
from application.services.project import ProjectService
from infrastructure.repositories.project import SqliteProjectRepository

db_path = './db.sqlite3'


async def get_project_service(
        db_path: str = Depends(lambda: db_path)
) -> ProjectService:
    return ProjectService(
        order_repository=SqliteProjectRepository(db_path=db_path),
    )
