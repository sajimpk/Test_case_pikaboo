from selenium import webdriver
import time 
from behave import *

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given(U'go to site')
def open_picabo(context):
    context.driver= webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://www.pickaboo.com/")
    context.driver.find_element(By.ID,'rcc-confirm-button').click()
    time.sleep(1)

@when(U'Click on the Categories button')
def step_impl5(context):
    context.driver.find_element(By.XPATH, "//img[@alt='humber']").click()
    time.sleep(5)

@then(U'Confirm that the Categories are Displayed')
def step_impl4(context):
    context.driver.find_element(By.XPATH,"//div[@class='home-banner__menu']//a[@class='a-tag'][normalize-space()='Computers']")
    time.sleep(4)

@then(U'close browser')
def step_impl23(context):
    context.driver.close()

# sinario 2
    
@when(U'go to login page')
def step_impl2(context):
    try:
        context.driver.find_element(By.CLASS_NAME, "eUtGXp").click()
        time.sleep(5)

    except:
       assert False

@when(U'login detials')
def step_impl1(context):
    context.driver.find_element(By.XPATH, '//*[@placeholder="Mobile Number/Email"]').send_keys('01861766157')
    context.driver.find_element(By.XPATH, '//*[@placeholder="Password"]').send_keys('sajimpk09')
    time.sleep(4)

@when(U'click login button')
def valid_Login_Attempt(context):
   context.driver.find_element(By.CLASS_NAME, 'custom-buttons').click()
   time.sleep(7)

# sinario 3
@when('search work')
def search(context):
    context.driver.find_element(By.CLASS_NAME, "searchInput ").send_keys('Laptop')
    time.sleep(5)

@when('submit search')
def search1(context):
    context.driver.find_element(By.CLASS_NAME, "searchInput ").submit()
    time.sleep(6)

@when('click on product')
def search2(context):
    context.driver.find_element(By.XPATH, "//*[@id='__next']/main/section/div[2]/div/div[2]/div[2]/div[7]").click()
    time.sleep(6)

# sinario 4
@then('slider found')
def Slider(context):
    context.driver.find_element(By.XPATH, "//div[@class='slick-slide slick-active slick-current']//div//div[@class='home-banner__slider__single a-tag']")
    assert True

@then('Click on slider')
def Slider2(context):
    context.driver.find_element(By.XPATH, "//button[normalize-space()='3']").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//button[normalize-space()='3']").click()
    time.sleep(1)

# sinario 5
@then('Verify the presence of the Support button')
def Support1(context):
    context.driver.find_element(By.XPATH, "//section[@class='LogoHomeSlider__StyledSlider-sc-1drhg8f-0 kXbXVo logo-slider pt-10 pb-20 shadow-bottom']//div[@class='swiper-container swiper-container-initialized swiper-container-horizontal']")
    assert True

@then('Click on the Support button')
def Support2(context):
    context.driver.find_element(By.XPATH, "//img[@src='https://storage.googleapis.com/pickaboo-prod/media/dcastalia_hybridslider/image/EMI.png']").click()
    time.sleep(7)

# sinario 6

@when('select a color')
def add_cart(context):
    try:
        context.driver.find_element(By.XPATH,"//div[@class='parent-row'][1]/div[@class='views']/div[1]/center").click()
        time.sleep(5)
    except:
        assert False

@when('click on add to cart')
def add_cart2(context):
    context.driver.find_element(By.XPATH,"//span[normalize-space()='ADD TO CART']").click()
    time.sleep(5)

# sinario 7
@when('click the cart option')
def cart_view(context):
    time.sleep(5)
    context.driver.find_element(By.XPATH,"//p[normalize-space()='cart']").click()
    time.sleep(5)

@then('Verify the cart option show')
def cart_get(context):
    time.sleep(5)
    context.driver.find_element(By.XPATH,"//h2[@class='Title__StyledTitle-sc-gk5zya-0 fjIree title']")
    assert True

@when('I click remove')
def remove_cart(context):
    context.driver.find_element(By.XPATH,"(//div[@class='save-button'])[3]").click()
    time.sleep(5)

# sinario 8
@When('Click the Smartphones Categories button')
def cate_w(context):
    context.driver.find_element(By.XPATH,"//div[@class='home-banner__menu']//a[@class='a-tag'][normalize-space()='Smartphones']").click()
    time.sleep(5)

@When('Click the Camera phone')
def cate_w1(context):
    time.sleep(5)
    context.driver.find_element(By.XPATH,"//body/div[@id='__next']/main/section[@class='ProductTwo__StyledProductTwo-sc-1cxokfi-0 fwGDQy product-layout-two pt-30 pb-30']/div[@class='container']/div[@class='row']/div[1]").click()
    time.sleep(5)

@When('Click the Samsung Galaxy S24')
def cate_w2(context):
    context.driver.find_element(By.XPATH,"//h4[normalize-space()='Samsung Galaxy S24 Ultra 5G 12GB/256GB']").click()
    time.sleep(5)

@when('click on Buy Now')
def add_cart(context):
    context.driver.find_element(By.XPATH,"//span[normalize-space()='BUY NOW']").click()
    time.sleep(5)

# sinario 9
@given('Click the Mobile Accessories button')
def add_cart2(context):
    context.driver.find_element(By.XPATH,"//div[@class='home-banner__menu']//a[@class='a-tag'][normalize-space()='Mobile Accessories']").click()
    time.sleep(5)

@when('click on Category for filter')
def catagory_filter(context):
    context.driver.find_element(By.XPATH,"//span[normalize-space()='Category']").click()
    time.sleep(5)

@when('click on smart watch')
def catagory_filter1(context):
    context.driver.find_element(By.XPATH,"//div[@class='accordion-collapse collapse show']//li[1]").click()
    time.sleep(5)

@when('click on Haylou Solar Pro Sport Smart Watch')
def catagory_filter2(context):
    time.sleep(5)
    context.driver.find_element(By.XPATH,"//h4[normalize-space()='Haylou Solar Pro Sport Smart Watch']").click()
    time.sleep(5)

# sinario 10
@when('go to cart for Add to wish list')
def add_wish_list1(context):
    context.driver.find_element(By.XPATH,"//div[@class='cart']").click()
    time.sleep(5)

@when('click to Save for later')
def add_wish_list2(context):
    context.driver.find_element(By.XPATH,"//div[normalize-space()='Save for later']").click()
    time.sleep(5)
    context.driver.find_element(By.XPATH,"//p[normalize-space()='My Account']").click()
    time.sleep(5)
    context.driver.find_element(By.XPATH,"//a[normalize-space()='My Wishlist']").click()
    time.sleep(5)

# sinario 11
@given('Click the LifeStyle button')
def Lifestyle(context):
    context.driver.find_element(By.XPATH,"//div[@class='home-banner__menu']//a[@class='a-tag'][normalize-space()='Lifestyle']").click()
    time.sleep(5)

@when('click on saver&trimmar')
def Lifestyle_catagory_filter1(context):
    context.driver.find_element(By.XPATH,"//div[@class='product-filter__sidebar__single__content']//li[contains(text(),'Shaver & Trimmer')]").click()
    time.sleep(5)

@when('click on HTC AT-530 Beard Trimmer for Men')
def Lifestyle_catagory_filter2(context):
    context.driver.find_element(By.XPATH,"//h4[normalize-space()='HTC AT-530 Beard Trimmer for Men']").click()
    time.sleep(5)

# sinario 12
@given('Click the Electronics & Appliances button')
def Lifestyle(context):
    context.driver.find_element(By.XPATH,"//div[@class='home-banner__menu']//a[@class='a-tag'][normalize-space()='Electronics & Appliances']").click()
    time.sleep(5)

@When('Click the Refrigerator')
def Refrigerator(context):
    time.sleep(5)
    context.driver.find_element(By.XPATH,"//section[@class='ProductTwo__StyledProductTwo-sc-1cxokfi-0 fwGDQy product-layout-two pt-30 pb-30']//div[2]//div[1]//div[1]//img[1]").click()
    time.sleep(5)

@When('Click the Singer BEKO 275')
def pud_item(context):
    context.driver.find_element(By.XPATH,"//h4[contains(text(),'Singer BEKO 275 Liter No Frost Refrigerator (BOREF')]").click()
    time.sleep(5)

# sinario 13
@When('Click the Television')
def Television(context):
    time.sleep(5)
    context.driver.find_element(By.XPATH,"//section[@class='ProductTwo__StyledProductTwo-sc-1cxokfi-0 fwGDQy product-layout-two pt-30 pb-30']//div[@class='row']//div[1]//div[1]//div[1]//img[1]").click()
    time.sleep(5)

@When('Click the Xiaomi A Pro 55')
def pud_item(context):
    context.driver.find_element(By.XPATH,"//h4[normalize-space()='Xiaomi A Pro 55 Inch 4K UHD Google TV']").click()
    time.sleep(5)

# sinario 14
@When('Click the gaming phone')
def gaming_phone(context):
    time.sleep(5)
    context.driver.find_element(By.XPATH,"//img[@src='https://storage.googleapis.com/pickaboo-prod/media/dcastalia_hybridslider/image/Gaming_phone.jpg']").click()
    time.sleep(5)

@When('Click the TECNO Spark 20 Pro')
def cate_w2(context):
    context.driver.find_element(By.XPATH,"//h4[normalize-space()='TECNO Spark 20 Pro KJ6 8GB/256GB']").click()
    time.sleep(5)

# sinario 15

@When('Click the view more')
def cate_w1(context):
    time.sleep(5)
    context.driver.find_element(By.XPATH,"//div[@class='accordion-collapse collapse show']//p[@class='show-more-button'][normalize-space()='view more']").click()
    time.sleep(5)

@When('Click the Data Cable')
def cate_w2(context):
    context.driver.find_element(By.XPATH,"//li[contains(text(),'Data Cable')]").click()
    time.sleep(5)

@When('Click to select Data Cable')
def select_cable(context):
    context.driver.find_element(By.XPATH,"//h4[contains(text(),'Baseus Cafule 2.4A 1M USB to Lightning Data Cable')]").click()
    time.sleep(5)

# sinario 16
@When('Click on my account')
def account_manage(context):
    context.driver.find_element(By.XPATH,"//p[normalize-space()='My Account']").click()
    time.sleep(5)

@When('Click on Manage Account')
def Manage_Account(context):
    context.driver.find_element(By.XPATH,"//a[normalize-space()='Manage Account']").click()
    time.sleep(5)

@then('click on edit')
def click_edit(context):
    context.driver.find_element(By.XPATH,"//div[@class='Button__StyledBtn-sc-55nib8-0 hTAfjy dc-btn']//a").click()
    time.sleep(2)
    
@when('update my information')
def update_acc(context):
    context.driver.find_element(By.XPATH,"//input[@placeholder='Enter your first name']").clear()
    context.driver.find_element(By.XPATH,"//input[@placeholder='Enter your first name']").send_keys('test')
    time.sleep(2)
    context.driver.find_element(By.XPATH,"//input[@placeholder='Enter your last name']").clear()
    context.driver.find_element(By.XPATH,"//input[@placeholder='Enter your last name']").send_keys('case')
    time.sleep(2)

@when('click on save')
def click_edit(context):
    context.driver.find_element(By.XPATH,"//span[normalize-space()='Save']").click()
    time.sleep(2)

# sinario 17
    
@when('Click the computer button')
def computer(context):
    context.driver.find_element(By.XPATH,"//div[@class='home-banner__menu']//a[@class='a-tag'][normalize-space()='Computers']").click()
    time.sleep(5)

@When('Click the HONOR Pad 8')
def Refrigerator(context):
    time.sleep(5)
    context.driver.find_element(By.XPATH,"//h4[normalize-space()='HONOR Pad 8 6GB/128GB (2023)']").click()
    time.sleep(5)

# sinario 18
@when('Click the Computer Accessories')
def computer(context):
    context.driver.find_element(By.XPATH,"//div[@class='home-banner__menu']//a[@class='a-tag'][normalize-space()='Computer Accessories']").click()
    time.sleep(5)

@When('Click on pen drive')
def pendrive(context):

    context.driver.find_element(By.XPATH,"//div[@class='product-filter__sidebar__single__content']//li[contains(text(),'Pen Drive')]").click()
    time.sleep(5)

@When('Click on Lexar JumpDrive M35')
def JumpDrive(context):
    context.driver.find_element(By.XPATH,"//h4[normalize-space()='Lexar JumpDrive M35 128GB USB 3.0 Pen Drive']").click()
    time.sleep(5)

#sinario 19
@when('add product review')
def add_review(context):
    context.driver.find_element(By.XPATH,"//h2[@class='Title__StyledTitle-sc-gk5zya-0 sVsjp title']").click()
    time.sleep(5)

@when('Enter my review')
def review_value(context):
    context.driver.find_element(By.XPATH,'(//*[@id="outlined-multiline-static"])[1]').send_keys('hellow')
    time.sleep(1)
    context.driver.find_element(By.XPATH,'(//*[@id="outlined-multiline-static"])[2]').send_keys('World')
    time.sleep(5)
@when('I click on submit button')
def submit_review(context):
    context.driver.find_element(By.XPATH,'//div[@class="Button__StyledBtn-sc-55nib8-0 htvFVc dc-btn"]//a').click()
    time.sleep(5)

# sinario 20
@when('I click on Proceed to checkout')
def cart_chackuot(context):
    context.driver.find_element(By.XPATH,"//span[normalize-space()='Proceed to checkout']").click()
    time.sleep(5)

@when('I click on CONTINUE')
def cart_chackuot_CONTINUE(context):
    context.driver.find_element(By.XPATH,"//span[normalize-space()='CONTINUE']").click()
    time.sleep(5)

@when('I click on bKash Payment')
def bKash_Payment(context):
    context.driver.find_element(By.XPATH,"//input[@value='bKash Payment']").click()
    time.sleep(10)

@when('I click on PLACE ORDER')
def PLACE_ORDER(context):
    context.driver.find_element(By.XPATH,"//span[normalize-space()='PLACE ORDER']").click()
    time.sleep(20)