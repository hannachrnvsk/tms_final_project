from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.support.ui import Select


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

    def click_create_acc_button_to_start_creation(self):
        self.click_button(*LoginPageLocators.CREATE_ACC_BUTTON)

    def creating_account_form_appeared(self):
        self.is_element_present(*LoginPageLocators.ACCOUNT_CREATION_FORM), "Account creation form didn't appear! "

    def choose_title(self):
        self.click_button(*LoginPageLocators.TITLE_RADIOBUTTON)

    def enter_first_name(self, data):
        first_name = self.return_element_located(*LoginPageLocators.FIRST_NAME_FIELD)
        first_name.send_keys(data)

    def enter_last_name(self, data):
        last_name = self.return_element_located(*LoginPageLocators.LAST_NAME_FIELD)
        last_name.send_keys(data)

    def enter_password(self, data):
        password = self.return_element_located(*LoginPageLocators.PASSWORD_FIELD_REG)
        password.send_keys(data)

    def choose_day_of_birth(self,data):
        day_of_birth = self.select_from_dropdown(*LoginPageLocators.DAY_OF_BIRTH)
        day_of_birth.select_by_value(data)

    def choose_month_of_birth(self, data):
        month_of_birth = self.select_from_dropdown(*LoginPageLocators.MONTH_OF_BIRTH)
        month_of_birth.select_by_value(data)

    def choose_year_of_birth(self,data):
        year_of_birth = self.select_from_dropdown(*LoginPageLocators.YEAR_OF_BIRTH)
        year_of_birth.select_by_value(data)

    def press_signup_for_newsletter_checkbox(self):
        self.click_button(*LoginPageLocators.NEWSLETTER_CHECKBOX)

    def press_receive_special_offers(self):
        self.click_button(*LoginPageLocators.SPECIAL_OFFERS_CHECKBOX)

    def enter_company(self, data):
        company = self.return_element_located(*LoginPageLocators.COMPANY_FIELD)
        company.send_keys(data)

    def enter_address_street(self, data):
        address_street = self.return_element_located(*LoginPageLocators.ADDRESS_STREET_FIELD)
        address_street.send_keys(data)

    def enter_address_build(self, data):
        address_build = self.return_element_located(*LoginPageLocators.ADDRESS_BUILDING_FIELD)
        address_build.send_keys(data)

    def enter_city(self,data):
        city = self.return_element_located(*LoginPageLocators.CITY_FIELD)
        city.send_keys(data)

    def choose_state_from_dropdown(self,data):
        state = self.select_from_dropdown(*LoginPageLocators.STATE_DROPDOWN)
        state.select_by_visible_text(data)

    def enter_postal_code(self,data):
        postal_code = self.return_element_located(*LoginPageLocators.POSTAL_CODE_FIELD)
        postal_code.send_keys(data)

    def choose_country_from_dropdown(self, data):
        country = self.select_from_dropdown(*LoginPageLocators.COUNTRY_DROPDOWN)
        country.select_by_visible_text(data)

    def enter_additional_info(self,data):
        additional_info = self.return_element_located(*LoginPageLocators.ADDITIONAL_INFO_FIELD)
        additional_info.send_keys(data)

    def enter_home_phone(self,data):
        home_phone = self.return_element_located(*LoginPageLocators.HOME_PHONE_FIELD)
        home_phone.send_keys(data)

    def enter_mobile_phone(self,data):
        mobile_phone = self.return_element_located(*LoginPageLocators.MOBILE_PHONE_FIELD)
        mobile_phone.send_keys(data)

    def enter_alias(self,data):
        alias = self.return_element_located(*LoginPageLocators.ALIAS_FIELD)
        alias.clear()
        alias.send_keys(data)

    def press_submit_button_to_create_acc(self):
        self.click_button(*LoginPageLocators.SUBMIT_CREATION_OF_ACCOUNT)

    def see_welcoming_message_account_created(self):
        self.is_element_present(*LoginPageLocators.WELCOMING_MESSAGE_ACCOUNT_CREATED)
        welcome_message = self.return_element_located(*LoginPageLocators.WELCOMING_MESSAGE_ACCOUNT_CREATED).text
        assert "Welcome to your account" in welcome_message

    def see_red_message_account_already_exists(self):
        self.is_element_present(*LoginPageLocators.RED_MESSAGE_ACCOUNT_ALREADY_EXISTS)
        acc_exists = self.return_element_located(*LoginPageLocators.RED_MESSAGE_ACCOUNT_ALREADY_EXISTS)
        assert "An account using this email address has already been registered." in acc_exists.text






