import pytest
from pages.data import Emails, valid_user_already_created
from pages.login_page import LoginPage


link = "http://automationpractice.com/index.php?controller=authentication&back=my-account"


def test_guest_can_open_login_page(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()


@pytest.mark.parametrize("email", [Emails.EMAIL_WITHOUT_DOMEN,
                                   Emails.EMAIL_WITHOUT_COMMERCIAL_AT,
                                   Emails.EMAIL_WITH_SPEC_SYMBOL,
                                   Emails.BLANK_EMAIL])
def test_reg_form_does_not_accept_invalid_mail(browser,email):
    page = LoginPage(browser,link)
    page.open()
    page.should_be_login_page()
    page.enter_mail_to_create_acc(email)
    page.click_create_acc_button_to_start_creation()
    page.should_be_red_message_invalid_email()


@pytest.mark.parametrize("email", [Emails.VALID_EMAIL,
                                   Emails.VALID_EMAIL_WITH_NUM])
def test_reg_form_accepts_valid_email(browser, email):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
    page.enter_mail_to_create_acc(email)
    page.click_create_acc_button_to_start_creation()
    page.creating_account_form_appeared()


@pytest.mark.parametrize("data", [valid_user_already_created])
def test_guest_can_create_user(browser, data):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
    page.enter_mail_to_create_acc(data.email)
    page.click_create_acc_button_to_start_creation()
    page.creating_account_form_appeared()
    page.choose_title()
    page.enter_first_name(data.first_name)
    page.enter_last_name(data.last_name)
    page.enter_password(data.password)
    page.choose_day_of_birth(data.day_of_birth)
    page.choose_month_of_birth(data.month_of_birth)
    page.choose_year_of_birth(data.year_of_birth)
    page.press_signup_for_newsletter_checkbox()
    page.press_receive_special_offers()
    page.enter_company(data.company)
    page.enter_address_street(data.address_street)
    page.enter_city(data.city)
    page.choose_state_from_dropdown(data.state)
    page.enter_postal_code(data.postal_code)
    page.choose_country_from_dropdown(data.country)
    page.enter_additional_info(data.additional_info)
    page.enter_home_phone(data.home_phone)
    page.enter_mobile_phone(data.mobile_phone)
    page.enter_alias(data.alias)
    page.press_submit_button_to_create_acc()
    page.see_welcoming_message_account_created()


@pytest.mark.parametrize("data", [valid_user_already_created])
def test_guest_cant_create_user_with_email_used_earlier(browser, data):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
    page.enter_mail_to_create_acc(data.email)
    page.click_create_acc_button_to_start_creation()
    page.see_red_message_account_already_exists()











