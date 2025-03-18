from behave import given, when, then
from domain.models.project.entity import Project
from domain.models.user.entity import User


@given("I login with PM account '{username}'")
def step_given_log_in_with_pm_account(context, username):
    context.user = User(id=1, user_name=username)


@when("I create a project with name '{project_name}'")
def step_when_create_project(context, project_name):
    context.project = Project(creator_id=context.user.id, project_name=project_name)


@then("I should see the project info")
def step_then_see_project_info(context):
    for row in context.table:
        assert context.project.project_name == row["project_name"]
        if row["last_test_runs"] == "No test runs":
            assert context.project.get_last_test_run_status() is None
        else:
            assert context.project.get_last_test_run_status() == row["last_test_runs"]
        assert context.user.user_name, context.project.creator_id == (row["PM"], context.user.id)
