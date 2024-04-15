@Navigation
Feature: Test Google search functionality

  Background: I am on the Google web
    Given I navigate to www.google.cl

  @SearchTest
  Scenario: As a user I enter a search criteria in Google
    When I enter a search criteria
    And click on the search button
    Then the result match the criteria
