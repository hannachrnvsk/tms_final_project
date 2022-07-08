from pages.product_page import ProductPage

import pytest

link = "http://automationpractice.com/index.php?id_product=2&controller=product"

def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser,link)
    page.open()
    page.should_be_product_page()
    page.click_addtocart_button()
    page.see_success_message_after_adding_product_to_cart()

def test_guest_can_add_two_units_of_product(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.add_one_more_unit()
    page.click_addtocart_button()
    page.see_success_message_after_adding_product_to_cart()
    page.sum_of_added_product_is_equal_to_expected()

def test_guest_can_choose_different_size_of_product(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    page.select_size_of_product()
    page.click_addtocart_button()
    page.see_success_message_after_adding_product_to_cart()
    page.size_in_message_is_equal_to_expected()







