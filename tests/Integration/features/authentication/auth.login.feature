Feature: /auth/login/

    Background:
        Given system knows user "user1" with password "pass1"
    Scenario Outline:
        When modify params = {}
        Then status 201
        And 
        
