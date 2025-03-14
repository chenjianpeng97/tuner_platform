from behave import given, when, then
from domain.models.project.entity import Project
from domain.models.auth.entity import User
from domain.services.project import ProjectService
@given("I login with PM account '{username}'")
def step_given_log_in_with_pm_account(context, username):
    context.user = User(user_name=username, id=1)
    context.test_run_repository = TestRunRepository()

@when("I create a project with name '{project_name}'")
def step_when_create_project(context, project_name):
    context.project = Project(project_name=project_name, creator_id=context.user.id)

@then("I should see the project info")
def step_then_see_project_info(context):
    project_service = ProjectService()
    for row in context.table:
        assert context.project.project_name == row['project_name']
        if row['test_runs'] == "No test runs":
            assert context. is None
        else:
            assert context.test_run_repository.get_last_test_run(context.project.id) == row['test_runs']
        assert context.project.get_creator().user_name == row['create_by']

