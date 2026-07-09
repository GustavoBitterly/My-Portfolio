@Amazon
Feature: Test Amazon search functionality

  Rule: The user can access to Amazon Website.

    Background: I am on the Amazon web page.
      Given I navigate to www.amazon.com

    @CartTest
    Scenario Outline: As a Customer when I search for Alexa, I want to see if the third option on the second page is available for purcharse and can be added to the cart.
      And Searches for Alexa
      And navigates to the second page
      And selects the third item
      Then the user is able to add it to the cart
