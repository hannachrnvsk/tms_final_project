from .base_page import BasePage
from .data import Product
from .locators import ProductPageLocators

# Creating product object to execute test
blouse = Product("Blouse", 27.00, 2, "M")


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_info()
        self.should_be_button_addtocart()

    def should_be_product_info(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_INFO_FIELD), "Product info field is not present"

    def should_be_button_addtocart(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON), "Button 'Add to basket' is not present"

    def click_addtocart_button(self):
        self.click_button(*ProductPageLocators.ADD_TO_CART_BUTTON)

    def add_one_more_unit(self):
        self.click_button(*ProductPageLocators.PRODUCT_QUANTITY_UP)

    def go_to_cart(self):
        self.click_button(*ProductPageLocators.VIEW_CART_BUTTON)

    def see_success_message_after_adding_product_to_cart(self):
        result = self.element_is_visible(*ProductPageLocators.SUCCESS_MESSAGE_PRODUCT_ADDED)
        assert result is True, "No success message after adding product to cart!"

    def sum_of_added_product_is_equal_to_expected(self):
        assert (
            self.return_element_located(*ProductPageLocators.TOTAL_SUM_OF_ADDED_PRODUCT_IN_MESSAGE).text
            == blouse.total_sum
        )

    def select_size_of_product(self):
        size = self.select_from_dropdown(*ProductPageLocators.SELECT_PRODUCT_SIZE)
        size.select_by_visible_text(blouse.size)

    def size_in_message_is_equal_to_expected(self):
        assert blouse.size in self.return_element_located(*ProductPageLocators.CHOSEN_SIZE_IN_MESSAGE).text
