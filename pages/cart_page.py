from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC


class Cart(Page):

    EMPTY_CART = (By.XPATH, "//*[@class='a-row sc-your-amazon-cart-is-empty']")
    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
    CART = (By.ID, 'nav-cart-count')


    def cart_empty_check(self):
        expected_result = 'Your Amazon Cart is empty'
        actual_result = self.driver.find_element(*self.EMPTY_CART).text
        assert expected_result == actual_result, f'Error! Expected {expected_result}, but got {actual_result}'


    def add_to_cart(self):
        e = self.driver.find_element(*self.ADD_TO_CART_BTN)
        self.driver.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART_BTN)).click()


    def check_cart_count(self, expected_count):
        actual_text = self.driver.find_element(*self.CART).text
        assert expected_count == actual_text, f'Expected {expected_count} but got {actual_text}'

