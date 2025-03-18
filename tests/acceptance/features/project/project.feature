Feature: PM create project
  In oder to start working
  As a PM
  I want to create project

  Scenario: Create project
    Given I login with PM account 'Jack'
    When I create a project with name 'bookstore management system'
    Then I should see the project info
      | project_name                | last_test_runs | PM   |
      | bookstore management system | No test runs   | Jack |

  Scenario: Create project failed cased by duplicate project name
    Given I login with PM account 'Jack'
    And system knows project 'bookstore management system'
    When I create a project with name 'bookstore management system'
    Then I should see the error message 'Project name already exists'

  @todo
  Scenario: PM set collaborators
    Given system knows user
      | user_name | user_e-mail   |
      | Tom       | Tom@test.com  |
      | Jack      | Jack@test.com |
    And I login with PM account 'Jack'
    When I create a project with name 'bookstore management system'
    And I add collaborators for the project<new_user_e-mail>
    Then I should see the project collaborators list
      | user_name | user_e-mail   |
      | Tom       | Tom@test.com  |
      | Jack      | Jack@test.com |