from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_signin_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        cur_url = self.get_current_url()
        assert "authentication" in cur_url, "Current URL doesn't contain word 'authentication'!"

    def should_be_signin_form(self):
        assert self.is_element_present(*LoginPageLocators.SIGNIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Registration form is not present"

    def enter_mail_to_create_acc(self, email):
        email_field = self.return_element_located(*LoginPageLocators.EMAIL_TO_CREATE_ACC_FIELD)
        email_field.send_keys(email)

    def should_be_red_message_invalid_email(self):
        self.is_element_present(*LoginPageLocators.RED_MESSAGE_INVALID_EMAIL_WHILE_CREATING_ACC), " No message, that email is invalid. System accepted invalid email"

    def click_create_acc_button(self):
        self.click_button(*LoginPageLocators.CREATE_ACC_BUTTON)

    def creating_account_form_appeared(self):
        self.is_element_present(*LoginPageLocators.ACCOUNT_CREATION_FORM), "Account creation form didn't appear! "

    def choose_title(self):
        pass

    def enter_first_name(self, data):
        pass


