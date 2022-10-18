from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

URL_Use = 'https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088'
#$$('a[href="https://www.amazon.com/privacy"]')
PRIVACY_LINK = (By.CSS_SELECTOR,'a[href="https://www.amazon.com/privacy"]')


@given('Open Amazon T&C page')
def open_amazon_condition(context):
    context.driver.get(URL_Use)



@when('Store original windows')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle
    print('original: ', context.original_window)



@when('Click on Amazon Privacy Notice Link')
def open_amazon_privacy(context):
    context.driver.find_element(*PRIVACY_LINK).click()


@when('Switch to the newly opened window')
def switch_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    current_windows = context.driver.window_handles
    print('current windows ', current_windows)
    context.driver.switch_to.window(current_windows[1])






