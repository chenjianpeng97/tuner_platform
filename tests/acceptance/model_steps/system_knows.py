from behave import given, when, then
from domain.models.project.entity import Project


@given("system knows project '{project_name}'")
def step_impl(context, project_name):
    context.known_project = Project(project_name=project_name)
