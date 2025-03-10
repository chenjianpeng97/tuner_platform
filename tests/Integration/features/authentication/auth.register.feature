Feature: /auth/register

  Scenario Outline: 新用户注册流程
    Given 后端认证服务正常运行
    When 用户使用<username>和<password>进行注册
    Then 应该返回状态码<status_code>
    And 响应包含<response_message>

    Examples:
      | username      | password       | status_code | response_message |
      | testuser_001  | Test@1234       | 201         | 注册成功          |
      | testuser_001  | weakpass        | 400         | 密码强度不足      |
      | existing_user | Existing@123   | 400         | 用户名已存在      |

  Scenario: 用户登录流程验证
    Given 已注册用户 testuser_002 密码为 Test@1234
    When 使用正确凭证登录
    Then 返回登录成功状态
    When 使用错误密码登录 testuser_002 输入登录密码 wrongpassword