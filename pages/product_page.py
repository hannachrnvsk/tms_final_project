from .base_page import BasePage
from .data import blouse
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import Select


class ProductPage(BasePage):

    def should_be_product_page(self):
        self.should_be_product_info()
        self.should_be_button_addtocart()

    def should_be_product_info(self):
        assert self.is_element_present(
            *ProductPageLocators.PRODUCT_INFO_FIELD), "Product info field is not present"

    def should_be_button_addtocart(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_CART_BUTTON), "Button 'Add to basket' is not present"

    def click_addtocart_button(self):
        self.click_button(*ProductPageLocators.ADD_TO_CART_BUTTON)

    def add_one_more_unit(self):
        self.click_button(*ProductPageLocators.PRODUCT_QUANTITY_UP)

    def go_to_cart(self):
        self.click_button(*ProductPageLocators.VIEW_CART_BUTTON)

    def see_success_message_after_adding_product_to_cart(self):
        self.element_is_visible(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_ADDED)

    def sum_of_added_product_is_equal_to_expected(self):
        assert self.return_element_located(*ProductPageLocators.TOTAL_SUM_OF_ADDED_PRODUCT_IN_MESSAGE).text == blouse.total_sum

    def select_size_of_product(self):
        size = Select(self.browser.find_element(*ProductPageLocators.SELECT_PRODUCT_SIZE))
        size.select_by_visible_text(blouse.size)

    def size_in_message_is_equal_to_expected(self):
        assert blouse.size in self.return_element_located(*ProductPageLocators.CHOSEN_SIZE_IN_MESSAGE).text
