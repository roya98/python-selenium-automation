from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Amazon Page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Find returns & orders')
def click_orders(context):
    context.driver.find_element(By.ID, 'nav-orders').click()

