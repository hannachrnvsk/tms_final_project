import pytest
from pages.data import Emails, valid_user_already_created
from pages.login_page import LoginPage
from pages.data import RandomUsers
from pages import data


link = "http://automationpractice.com/index.php?controller=authentication&back=my-account"


def test_guest_can_open_login_page(browser):
    """Tests that login page exists"""
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()


@pytest.mark.parametrize("email", [Emails.EMAIL_WITHOUT_DOMEN,
                                   Emails.EMAIL_WITHOUT_COMMERCIAL_AT,
                                   Emails.EMAIL_WITH_SPEC_SYMBOL,
                                   Emails.BLANK_EMAIL])
def test_reg_form_does_not_accept_invalid_mail(browser,email):
    """Tests that registration form doesn't accept invalid emails"""
    page = LoginPage(browser,link)
    page.open()
    page.should_be_login_page()
    page.enter_mail_to_create_acc(email)
    page.click_create_acc_button_to_start_creation()
    page.should_be_red_message_invalid_email()


@pytest.mark.parametrize("email", [Emails.VALID_EMAIL,
                                   Emails.VALID_EMAIL_WITH_NUM])
def test_reg_form_accepts_valid_email(browser, email):
    """Tests that registration form accepts valid emails"""
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
    page.enter_mail_to_create_acc(email)
    page.click_create_acc_button_to_start_creation()
    page.creating_account_form_appeared()



@pytest.mark.parametrize("data", [RandomUsers("Kansas","United States")])
def test_guest_can_create_user_with_all_valid_data(browser, data):
    """Tests that guest can create account using all possible valid data."""
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
    """Tests that guest can't create account using email which has been used before"""
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
    page.enter_mail_to_create_acc(data.email)
    page.click_create_acc_button_to_start_creation()
    page.see_red_message_account_already_exists()


@pytest.mark.parametrize("data", [RandomUsers("Kansas","United States")])
def test_guest_can_create_user_with_only_data_marked_as_mandatory(browser, data):
    """Tests that guest can create account by only filling fields marked as mandatory"""
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
    page.enter_mail_to_create_acc(data.email)
    page.click_create_acc_button_to_start_creation()
    page.creating_account_form_appeared()
    page.enter_first_name(data.first_name)
    page.enter_last_name(data.last_name)
    page.enter_password(data.password)
    page.enter_address_street(data.address_street)
    page.enter_city(data.city)
    page.choose_state_from_dropdown(data.state)
    page.enter_postal_code(data.postal_code)
    page.choose_country_from_dropdown(data.country)
    page.enter_mobile_phone(data.mobile_phone)
    page.enter_alias(data.alias)
    page.press_submit_button_to_create_acc()
    page.see_welcoming_message_account_created()


@pytest.mark.parametrize("data", [valid_user_already_created])
def test_guest_can_sign_in(browser, data):
    """Tests that user can sign in"""
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
    page.enter_email_to_sign_in(data.email)
    page.enter_password_to_sign_in(data.password)


@pytest.mark.parametrize("data_u",[data.user_invalid_name,
                                   data.user_invalid_date_of_birth,
                                   data.user_invalid_homephone,
                                   data.user_invalid_password,
                                   data.user_invalid_mobile_phone,
                                   data.user_invalid_postalcode])
def test_guest_cant_create_account_with_invalid_data(browser, data_u):
    """Tests that guest can't create account using invalid data"""
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
    page.enter_mail_to_create_acc(data_u.email)
    page.click_create_acc_button_to_start_creation()
    page.creating_account_form_appeared()
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
    page.press_submit_button_to_create_acc()
    page.see_error_message_invalid_data()











