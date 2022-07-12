import allure

from pages.product_page import ProductPage

import pytest

link = "http://automationpractice.com/index.php?id_product=2&controller=product"


@allure.feature("Check if guest can see success message after he'd just added product to basket")
def test_guest_can_see_success_message_after_adding_product_to_basket(browser):
    with allure.step('Open product page'):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_product_page()
    with allure.step('Click add to cart button'):
        page.click_addtocart_button()
    with allure.step('Check if success message appeared'):
        page.see_success_message_after_adding_product_to_cart()


@allure.feature("Check if guest can add two units of product and more")
def test_guest_can_add_two_units_of_product(browser):
    with allure.step('Open product page'):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_product_page()
    with allure.step('Click add one more unit'):
        page.add_one_more_unit()
    with allure.step('Click add to cart button'):
        page.click_addtocart_button()
    with allure.step('Check if success message appeared'):
        page.see_success_message_after_adding_product_to_cart()
    with allure.step('Check if sum in message is twice higher than price'):
        page.sum_of_added_product_is_equal_to_expected()


@allure.feature("Check if guest can choose size of product")
def test_guest_can_choose_different_size_of_product(browser):
    with allure.step('Open product page'):
        page = ProductPage(browser, link)
        page.open()
        page.should_be_product_page()
    with allure.step('Choose size of product'):
        page.select_size_of_product()
    with allure.step('Click add to cart button'):
        page.click_addtocart_button()
    with allure.step('Check if success message appeared'):
        page.see_success_message_after_adding_product_to_cart()
    with allure.step('Check if size in message is equal to expected'):
        page.size_in_message_is_equal_to_expected()
