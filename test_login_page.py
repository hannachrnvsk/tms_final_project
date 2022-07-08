import pytest
from pages.data import Emails, UserInfoToCreateAccount
from  pages.login_page import LoginPage

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
    page.click_create_acc_button()
    page.should_be_red_message_invalid_email()


@pytest.mark.parametrize("email", [Emails.VALID_EMAIL,
                                   Emails.VALID_EMAIL_WITH_NUM])
def test_reg_form_accepts_valid_email(browser, email):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
    page.enter_mail_to_create_acc(email)
    page.click_create_acc_button()
    page.creating_account_form_appeared()


@pytest.mark.parametrize("data", [UserInfoToCreateAccount.ALL_POSIBLE_VALID_DATA_1])
def test_can_create_user(browser,data):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
    page.enter_mail_to_create_acc(Emails.VALID_EMAIL)
    page.click_create_acc_button()
    page.creating_account_form_appeared()







