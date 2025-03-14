# interface/api/orders.py

from fastapi import APIRouter, Depends, HTTPException
from application.services.project import ProjectService
from domain.models.project.entity import Project
from domain.models.test.entity import TestRun
from domain.exceptions import ProjectError
from interface.dependencies import get_project_service
from interface.schemas import CreateProjectRequest, ProjectResponse

router = APIRouter()


@router.post("/projects", response_model=ProjectResponse)
async def create_project(
        request: CreateProjectRequest,
        project_service: ProjectService = Depends(get_project_service)
):
    try:
        project = await project_service.create_project(
            creator=request.current_user,
            project_name=request.project_name
        )
        return ProjectResponse.parse_obj(project)
    except ProjectError as e:
        raise HTTPException(status_code=400, detail=str(e))
