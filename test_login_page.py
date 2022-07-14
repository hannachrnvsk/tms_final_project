import allure
import pytest

from pages import data
from pages.data import Emails, RandomUsers, login_page_link_a, valid_user_already_created
from pages.login_page import LoginPage

link = login_page_link_a.link
# POSITIVE TESTS


@allure.feature("Check guest can open login page")
def test_guest_can_open_login_page(browser):
    """Tests that login page exists"""
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()


@allure.feature("Check registration form accepts valid email")
@pytest.mark.parametrize("email", [Emails.VALID_EMAIL, Emails.VALID_EMAIL_WITH_NUM])
def test_reg_form_accepts_valid_email(browser, email):
    """Tests that registration form accepts valid emails"""
    with allure.step("Open login page"):
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_page()
    with allure.step("Enter valid email"):
        page.enter_mail_to_create_acc(email)
    with allure.step("Click create account button"):
        page.click_create_acc_button_to_start_creation()
    with allure.step("Check if account creation form appeared"):
        page.creating_account_form_appeared()


@allure.feature("Check registration form accepts valid data")
@pytest.mark.parametrize("data_u", [RandomUsers("Kansas", "United States")])
def test_guest_can_create_user_with_all_valid_data(browser, data_u):
    """Tests that guest can create account by filling all possible fields with valid data."""
    with allure.step("Open login page"):
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_page()
    with allure.step("Enter valid email"):
        page.enter_mail_to_create_acc(data_u.email)
    with allure.step("Click create account button"):
        page.click_create_acc_button_to_start_creation()
    with allure.step("Check if account creation form appeared"):
        page.creating_account_form_appeared()
    with allure.step("Fill in all possible fields with valid data"):
        page.choose_title()
        page.enter_first_name(data_u.first_name)
        page.enter_last_name(data_u.last_name)
        page.enter_password(data_u.password)
        page.choose_day_of_birth(data_u.day_of_birth)
        page.choose_month_of_birth(data_u.month_of_birth)
        page.choose_year_of_birth(data_u.year_of_birth)
        page.press_signup_for_newsletter_checkbox()
        page.press_receive_special_offers()
        page.enter_company(data_u.company)
        page.enter_address_street(data_u.address_street)
        page.enter_city(data_u.city)
        page.choose_state_from_dropdown(data_u.state)
        page.enter_postal_code(data_u.postal_code)
        page.choose_country_from_dropdown(data_u.country)
        page.enter_additional_info(data_u.additional_info)
        page.enter_home_phone(data_u.home_phone)
        page.enter_mobile_phone(data_u.mobile_phone)
        page.enter_alias(data_u.alias)
    with allure.step("Click submit button"):
        page.press_submit_button_to_create_acc()
    with allure.step("Check welcoming message appeared"):
        page.see_welcoming_message_account_created()


@allure.feature("Check if fields which are not marked as mandatory, really are not obligatory")
@pytest.mark.parametrize("data_u", [RandomUsers("Kansas", "United States")])
def test_guest_can_create_user_with_only_data_marked_as_mandatory(browser, data_u):
    """Tests that guest can create account by only filling fields marked as mandatory"""
    with allure.step("Open login page"):
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_page()
    with allure.step("Enter valid email"):
        page.enter_mail_to_create_acc(data_u.email)
    with allure.step("Click create account button"):
        page.click_create_acc_button_to_start_creation()
    with allure.step("Check if account creation form appeared"):
        page.creating_account_form_appeared()
    with allure.step("Fill in only those fields which are marked as mandatory with valid data"):
        page.enter_first_name(data_u.first_name)
        page.enter_last_name(data_u.last_name)
        page.enter_password(data_u.password)
        page.enter_address_street(data_u.address_street)
        page.enter_city(data_u.city)
        page.choose_state_from_dropdown(data_u.state)
        page.enter_postal_code(data_u.postal_code)
        page.choose_country_from_dropdown(data_u.country)
        page.enter_mobile_phone(data_u.mobile_phone)
        page.enter_alias(data_u.alias)
    with allure.step("Click submit button"):
        page.press_submit_button_to_create_acc()
    with allure.step("Check welcoming message appeared"):
        page.see_welcoming_message_account_created()


@allure.feature("Check if already registered user can sign in")
@pytest.mark.parametrize("data_u", [valid_user_already_created])
def test_guest_can_sign_in(browser, data_u):
    """Tests that user can sign in"""
    with allure.step("Open login page"):
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_page()
    with allure.step("Enter email"):
        page.enter_email_to_sign_in(data_u.email)
    with allure.step("Enter password"):
        page.enter_password_to_sign_in(data_u.password)
    with allure.step("Press sign in button"):
        page.press_signin_button()
    with allure.step("Check welcoming message appeared"):
        page.see_welcoming_message_signed_in()


# NEGATIVE TESTS


@allure.feature("Check if system doesn't allow to create account using email which has been used before")
@pytest.mark.parametrize("data_u", [valid_user_already_created])
def test_guest_cant_create_user_with_email_used_earlier(browser, data_u):
    """Tests that guest can't create account using email which has been used before"""
    with allure.step("Open login page"):
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_page()
    with allure.step("Enter email which was used before"):
        page.enter_mail_to_create_acc(data_u.email)
    with allure.step("Click create account button"):
        page.click_create_acc_button_to_start_creation()
    with allure.step("Check system returns red message that account already exists"):
        page.see_red_message_account_already_exists()


@allure.feature("Check registration form doesn't accept invalid email")
@pytest.mark.parametrize(
    "email",
    [Emails.EMAIL_WITHOUT_DOMEN, Emails.EMAIL_WITHOUT_COMMERCIAL_AT, Emails.EMAIL_WITH_SPEC_SYMBOL, Emails.BLANK_EMAIL],
)
def test_reg_form_does_not_accept_invalid_mail(browser, email):
    """Tests that registration form doesn't accept invalid emails"""
    with allure.step("Open login page"):
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_page()
    with allure.step("Enter invalid email"):
        page.enter_mail_to_create_acc(email)
    with allure.step("Click create account button"):
        page.click_create_acc_button_to_start_creation()
    with allure.step("Check if system returns message that email is invalid"):
        page.should_be_red_message_invalid_email()


@allure.feature("Check if guest cant create account with invalid data")
@pytest.mark.parametrize(
    "data_u",
    [
        data.user_invalid_name,
        data.user_invalid_date_of_birth,
        data.user_invalid_homephone,
        data.user_invalid_password,
        data.user_invalid_mobile_phone,
        data.user_invalid_postalcode,
    ],
)
def test_guest_cant_create_account_with_invalid_data(browser, data_u):
    """Tests that guest can't create account using invalid data"""
    with allure.step("Open login page"):
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_page()
    with allure.step("Enter valid email"):
        page.enter_mail_to_create_acc(data_u.email)
    with allure.step("Click create account button"):
        page.click_create_acc_button_to_start_creation()
    with allure.step("Check if account creation form appeared"):
        page.creating_account_form_appeared()
    with allure.step("Enter invalid data to the form"):
        page.choose_title()
        page.enter_first_name(data_u.first_name)
        page.enter_last_name(data_u.last_name)
        page.enter_password(data_u.password)
        page.choose_day_of_birth(data_u.day_of_birth)
        page.choose_month_of_birth(data_u.month_of_birth)
        page.choose_year_of_birth(data_u.year_of_birth)
        page.press_signup_for_newsletter_checkbox()
        page.press_receive_special_offers()
        page.enter_company(data_u.company)
        page.enter_address_street(data_u.address_street)
        page.enter_city(data_u.city)
        page.choose_state_from_dropdown(data_u.state)
        page.enter_postal_code(data_u.postal_code)
        page.choose_country_from_dropdown(data_u.country)
        page.enter_additional_info(data_u.additional_info)
        page.enter_home_phone(data_u.home_phone)
        page.enter_mobile_phone(data_u.mobile_phone)
        page.enter_alias(data_u.alias)
    with allure.step("Click submit button"):
        page.press_submit_button_to_create_acc()
    with allure.step("Check if system returns error message that entered data is invalid"):
        page.see_error_message_invalid_data()
