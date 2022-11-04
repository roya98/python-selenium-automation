from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.ui import Select

class MainPage(Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    CART_ICON = (By.XPATH, "//span[@class='nav-cart-icon nav-sprite']")
    DEPARTMENT_SELECTION = (By.ID, 'searchDropdownBox')

    def open_main(self):
        self.open_url()

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BTN)



    def click_on_cart(self):
        self.driver.find_element(*self.CART_ICON).click()



    def select_department(self, selection_value):
        select = Select(self.find_element(*self.DEPARTMENT_SELECTION))
        select.select_by_value(f"search-alias={selection_value}")

