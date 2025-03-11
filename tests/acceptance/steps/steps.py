from behave import given,when,then
from pydantic import BaseModel
from typing import List

from backend.domain.models.project.entity import Project

class User(BaseModel):
    id:int = None
    user_name:str = ...
    
    
@given("I login with PM account '{username}'")
def step_given_log_in_with_pm_account(context, username):
    # Here you would implement the actual login logic
    context.user=User(user_name = username,id=1)
    


@when("I create a project with name '{project_name}'")
def step_when_create_project(context, project_name):
    # Here you would implement the actual project creation logic
    context.project = Project(project_name = project_name,creator_id=context.user.id)
    


@then("I should see the project info")

def step_then_see_project_info(context):
    for row in context.table:
        assert context.project.project_name == row['project_name']
        if row['test_runs'] == "No test runs":
            assert context.project.test_runs == None
        else:
            assert context.project.test_runs == row['test_runs']
        assert context.project.name == row['create_by']

