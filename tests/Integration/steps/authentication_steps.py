from behave import given, when, then, step
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

@given('后端认证服务正常运行')
def step_impl(context):
    context.client = TestClient(app)

@when('用户使用{username}和{password}进行注册')
def step_impl(context, username, password):
    context.response = context.client.post(
        "/auth/register",
        json={"username": username, "email": f"{username}@test.com", "password": password}
    )

@then('应该返回状态码{status_code:d}')
def step_impl(context, status_code):
    assert context.response.status_code == status_code, \
        f"预期状态码{status_code}，实际收到{context.response.status_code}"

@then('响应包含{response_message}')
def step_impl(context, response_message):
    assert response_message in context.response.text, \
        f"响应中未找到预期消息'{response_message}'"

@given('已注册用户 {username} 密码为 {password}')
def step_impl(context, username, password):
    context.username = username
    context.password = password
    client.post("/auth/register", json={"username": username, "email": f"{username}@test.com", "password": password})

@when('使用正确凭证登录')
def step_impl(context):
    context.response = client.post(
        "/auth/login",
        data={"username": context.username, "password": context.password}
    )

@then('返回登录成功状态')
def step_impl(context):
    assert context.response.status_code == 200
    assert "Login successful" in context.response.text

@when('使用错误密码登录 {username} 输入登录密码 {password}')
def step_impl(context, username, password):
    context.response = client.post(
        "/auth/login",
        json={"username": username, "password": password}
    )

@then('返回认证失败状态')
def step_impl(context):
    assert context.response.status_code == 401
    assert "Invalid credentials" in context.response.text