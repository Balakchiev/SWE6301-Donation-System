Feature: Donation Management System
  As a non-profit organisation
  I want to record donations
  So that I can track financial support from donors

  Scenario: Successful donation
    Given the donation system is running
    When a donor named "Mario" contributes 50
    Then the total donations should be 50
    And the donation count should be 1

  Scenario: Multiple donations
    Given the donation system is running
    When a donor named "Mario" contributes 50
    And a donor named "John" contributes 20
    Then the total donations should be 70
    And the donation count should be 2

  Scenario: Invalid donation amount
    Given the donation system is running
    When a donor named "Mario" contributes -10
    Then an error message should be displayed