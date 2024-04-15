@Navigation
Feature: Test Google search functionality

  Rule: The user can write a criteria in the textbox from Google Search.

    Background: I am on the Google web
      Given I navigate to www.google.cl

    @SearchTest
    Scenario: As a user I enter a search criteria in Google
      When I enter a search criteria
      And click on the search button
      Then the result match the criteria
