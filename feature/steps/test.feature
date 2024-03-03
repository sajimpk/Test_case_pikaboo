Feature: pikaboo testing
    Scenario: Verify Availability and Display of Categories 
        Given go to site
        When Click on the Categories button
        Then Confirm that the Categories are Displayed
        And close browser

    Scenario: Login with valid user and password
        Given go to site
        When go to login page
        And login detials
        And click login button

    Scenario: Validate Availability search
        Given go to site
        When search work

    Scenario: Validate Availability slider
        Given go to site
        Then slider found
        Then Click on slider

    Scenario: Validate Availability and Functionality of Support Button
        Given go to site
        Then Verify the presence of the Support button
        Then Click on the Support button
        
    Scenario: view user cart deteiles
        Given go to site 
        When go to login page
        And login detials
        And click login button
        When click the cart option
        Then Verify the cart option show

