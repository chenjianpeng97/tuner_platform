Feature: PM create project
    In oder to start working
    As a PM
    I want to create project

  Scenario: Create project
    Given I login with PM account 'Jack'
    When I create a project with name 'bookstore management system'
    Then I should see the project info
      | project_name                | last_test_runs    | PM |
      | bookstore management system | No test runs | Jack      |
    