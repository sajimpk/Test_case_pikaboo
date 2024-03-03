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
    time.sleep(1)

@when(U'Click on the Categories button')
def step_impl2(context):
    context.driver.find_element(By.XPATH, "//img[@alt='humber']").click()
    time.sleep(1)

@then(U'Confirm that the Categories are Displayed')
def step_impl2(context):
    context.driver.find_element(By.XPATH,"//div[@class='home-banner__menu']//a[@class='a-tag'][normalize-space()='Computers']")

@then(U'close browser')
def step_impl2(context):
    context.driver.close()

# sinario 2
    
@when(U'go to login page')
def step_impl2(context):
    try:
        context.driver.find_element(By.CLASS_NAME, "eUtGXp").click()
        time.sleep(2)

    except:
       assert False

@when(U'login detials')
def step_impl2(context):
    context.driver.find_element(By.XPATH, '//*[@placeholder="Mobile Number/Email"]').send_keys('01861766157')
    context.driver.find_element(By.XPATH, '//*[@placeholder="Password"]').send_keys('sajimpk09')
    time.sleep(2)

@when(U'click login button')
def valid_Login_Attempt(context):
   context.driver.find_element(By.CLASS_NAME, 'custom-buttons').click()
   time.sleep(5)

# sinario 3
@when('search work')
def search(context):
    try:
        context.driver.find_element(By.CLASS_NAME, "searchInput ").send_keys('Laptop')
        context.driver.find_element(By.CLASS_NAME, "searchInput ").submit()
        time.sleep(5)
        context.driver.find_element(By.XPATH, "//*[@id='__next']/main/section/div[2]/div/div[2]/div[2]/div[7]").click()
        time.sleep(5)
    except Exception as a:
        print(a)

# sinario 4
@then('slider found')
def Slider(context):
    context.driver.find_element(By.XPATH, "//div[@class='slick-slide slick-active slick-current']//div//div[@class='home-banner__slider__single a-tag']")
    assert True
@then('Click on slider')
def Slider(context):
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
    time.sleep(5)

# sinario 6
@when('click the cart option')
def cart_view(context):
    time.sleep(5)
    context.driver.find_element(By.XPATH,"//p[normalize-space()='cart']").click()
    time.sleep(2)

@then('Verify the cart option show')
def cart_get(context):
    time.sleep(5)
    context.driver.find_element(By.XPATH,"//h2[@class='Title__StyledTitle-sc-gk5zya-0 fjIree title']")
    assert True