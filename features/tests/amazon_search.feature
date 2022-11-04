# Created by roya at 10/6/22
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: User can add a product to the cart
    Given Open Amazon Page
     When Search for Dress
     And Click on the first product
     And Click on Add to cart button
     And Open cart page
     Then Verify cart has 1 item(s)




  Scenario: User can search for coffee
    Given Open amazon page
    When Search for coffee
    Then Search results for "coffee" are shown

  Scenario: User can search for mug
    Given Open amazon page
    When Search for mug
    Then Search results for "mug" are shown


  Scenario Outline: User can select and search in a department
    Given Open amazon page
    When Select department by value <value>
    And Search for Alexa
    Then Verify <department> department is selected
    Examples:
      | value               |department |
      | amazon-devices      |amazon-devices |
      | alexa-skills       | digital-skills   |

