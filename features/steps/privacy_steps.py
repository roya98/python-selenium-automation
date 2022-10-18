from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@then('Verify Amazon Privacy Notice page is opened')
def privacy_page_is_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/'))


@then('User can close new window and switch back to original')
def close_window_return(context):
    context.driver.close()
    context.driver.switch_to.window(context.original_window)
    sleep(2)


