from pages.bestsellers_page import BestsellersPage
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from pages.signin_page import Signin
from pages.cart_page import Cart
from pages.amazon_fashion import Fashion


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.bestsellers_page = BestsellersPage(self.driver)
        self.main_page = MainPage(self.driver)
        self.search_results_page = SearchResultsPage(self.driver)
        self.signin_page = Signin(self.driver)
        self.cart_page = Cart(self.driver)
        self.amazon_fashion = Fashion(self.driver)