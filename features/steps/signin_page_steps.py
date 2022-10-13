from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


@then('Verify Sign in page opened')
def verify_sign_in_opened(context):
    context.driver.wait.until(EC.url_contains('ap/signin'), message='Sign in URL did not open')