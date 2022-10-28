from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


@then('Sign in page is shown')
def verify_signin_page(context):
   # context.driver.wait.until(EC.url_contains('ap/signin'), message="Sign in page not found")
    context.app.signin_page.verify_signin()


