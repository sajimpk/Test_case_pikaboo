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
        And submit search
        And click on product

    Scenario: Validate Availability slider
        Given go to site
        Then slider found
        Then Click on slider

    Scenario: Validate Availability and Functionality of Support Button
        Given go to site
        Then Verify the presence of the Support button
        Then Click on the Support button

    Scenario: Add product on cart 
        Given go to site
        When go to login page
        And login detials
        And click login button
        When search work
        And submit search
        And click on product
        And select a color
        And click on add to cart


    Scenario: view user cart deteiles
        Given go to site 
        When go to login page
        And login detials
        And click login button
        When click the cart option
        Then Verify the cart option show
        When I click remove

    Scenario: Check Smartphones Categories
        Given go to site
        When go to login page
        And login detials
        And click login button
        And Click the Smartphones Categories button
        And Click the Camera phone
        And Click the Samsung Galaxy S24
        And select a color
        And click on Buy Now

    Scenario: Explore Mobile Accessories Categories
        Given go to site
        Given Click the Mobile Accessories button
        When click on Category for filter
        And click on smart watch
        And click on Haylou Solar Pro Sport Smart Watch
        And select a color
        And click on Buy Now

    Scenario: Explore Lifestyle Categories
        Given go to site
        Given Click the LifeStyle button
        When click on Category for filter
        And click on saver&trimmar
        And click on HTC AT-530 Beard Trimmer for Men
        And click on Buy Now

    Scenario: Check Availability of Refrigerator Items and Add to Cart
        Given go to site
        Given Click the Electronics & Appliances button
        When Click the Refrigerator
        And Click the Singer BEKO 275
        And select a color
        And click on Buy Now

    Scenario: wish list functions
        Given go to site
        When go to login page
        And login detials
        And click login button
        And go to cart for Add to wish list
        And click to Save for later
    
    Scenario: Check Availability of Tv Items and Add to Cart
        Given go to site
        Given Click the Electronics & Appliances button
        When Click the Television
        And Click the Xiaomi A Pro 55
        And click on Buy Now

    Scenario: Check Smartphones Categories
        Given go to site
        When go to login page
        And login detials
        And click login button
        And Click the Smartphones Categories button
        And Click the gaming phone
        And Click the TECNO Spark 20 Pro
        And select a color
        And click on Buy Now
    Scenario: Check mobile Mobile Accessories Data cable
        Given go to site
        Given Click the Mobile Accessories button
        When click on Category for filter
        And Click the view more
        And Click the Data Cable
        And Click to select Data Cable
        And click on Buy Now

    Scenario: chack update accounts information
        Given go to site
        When go to login page
        And login detials
        And click login button
        And Click on my account
        And Click on Manage Account
        Then click on edit
        When update my information
        And click on save
    Scenario: chack computer slide
        Given go to site
        When go to login page
        And login detials
        And click login button
        And Click the computer button
        When Click the HONOR Pad 8
        And select a color
        And click on Buy Now
    Scenario: chack Computer Accessories information
        Given go to site
        When go to login page
        And login detials
        And click login button
        And Click the Computer Accessories
        And click on Category for filter
        And Click on pen drive
        And Click on Lexar JumpDrive M35
        And click on Buy Now

    Scenario: chack product review send
        Given go to site
        When go to login page
        And login detials
        And click login button
        And Click the Computer Accessories
        And click on Category for filter
        And Click on pen drive
        And Click on Lexar JumpDrive M35
        And add product review
        And Enter my review
        And I click on submit button

    Scenario: Check cart Option Proceed to checkout
        Given go to site
        When go to login page
        And login detials
        And click login button
        When click the cart option
        And I click on Proceed to checkout
        And I click on CONTINUE
        And I click on bKash Payment
        And I click on PLACE ORDER
        