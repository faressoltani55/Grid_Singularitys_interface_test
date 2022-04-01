# Created by fares at 31/03/2022

Feature: Testing the Login Flow
  # Enter feature description here

  Scenario Outline: Login to Grid Singularity Dashboard success test
    Given launch browser
    When login tab is open
    And enter email "<email>" and password "<password>"
    And click on login button
    Then user must successfully connect to the dashboard page
    Examples:
      | email | password |
      | valid_email | valid_password |
      | valid_email | invalid_password |
      | invalid_email | valid_password |