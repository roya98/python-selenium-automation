from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


from pages.base_page import Page

class Signin(Page):
    ORDER_LINK = (By.ID, 'nav-orders')


    def click_orders_link(self):
        self.driver.find_element(*self.ORDER_LINK).click()


    def verify_signin(self):
         self.driver.wait.until(EC.url_contains('ap/signin'), message="Sign in page not found")
