from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage
from .product_page import ProductPage


class MainPage(BasePage):

    def go_to_login_page(self):
        self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()
        #return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_product_page(self):
        self.browser.find_element(*MainPageLocators.PRODUCT_LINK_BLOUSE).click()
        #return ProductPage(browser=self.browser, url=self.browser.current_url)
        assert self.browser.get_current_url() == "http://automationpractice.com/index.php?id_product=2&controller=product"
