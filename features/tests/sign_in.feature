# Created by roya at 10/12/22
Feature: Sign in test cases
  # Enter feature description here

  Scenario: Sign In page can be opened from SignIn popup
    Given Open Amazon page
    When Click on button from SignIn popup
    Then Verify Sign in page opened

   Scenario: Amazon user see sign in page
     Given Open Amazon Page
     Then Verify Sign In is clickable
     When Wait for 5 sec
    # Then Verify Sign is clickable
     Then Verify Sign In disappears





