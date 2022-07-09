from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "div.header_user_info>a")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, "div.shopping_cart>a")
    PRODUCT_LINK_BLOUSE = (By.CSS_SELECTOR, "a.product_img_link[title=Blouse]")


class LoginPageLocators:
    REG_FORM = (By.CSS_SELECTOR, "form#create-account_form")
    EMAIL_TO_CREATE_ACC_FIELD = (By.CSS_SELECTOR, "input#email_create")
    CREATE_ACC_BUTTON = (By.CSS_SELECTOR, "button#SubmitCreate")
    ACCOUNT_CREATION_FORM = (By.CSS_SELECTOR, "form#account-creation_form")
    SIGNIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    SIGNIN_BUTTON = (By.CSS_SELECTOR, "button#SubmitLogin")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, "div.shopping_cart>a")
    RED_MESSAGE_INVALID_EMAIL_WHILE_CREATING_ACC = (By.CSS_SELECTOR, "div#create_account_error.alert.alert-danger")
    TITLE_RADIOBUTTON = (By.CSS_SELECTOR, "input#id_gender2")
    FIRST_NAME_FIELD = (By.CSS_SELECTOR, "input#customer_firstname")
    LAST_NAME_FIELD = (By.CSS_SELECTOR, "input#customer_lastname")
    PASSWORD_FIELD_REG = (By.CSS_SELECTOR, "input#passwd")
    DAY_OF_BIRTH = (By.CSS_SELECTOR, "select#days")
    MONTH_OF_BIRTH = (By.CSS_SELECTOR, "select#months")
    YEAR_OF_BIRTH = (By.CSS_SELECTOR, "select#years")
    NEWSLETTER_CHECKBOX = (By.CSS_SELECTOR, "input#newsletter")
    SPECIAL_OFFERS_CHECKBOX = (By.CSS_SELECTOR, "input#optin")
    COMPANY_FIELD = (By.CSS_SELECTOR, "input#company")
    ADDRESS_STREET_FIELD = (By.CSS_SELECTOR, "input#address1")
    ADDRESS_BUILDING_FIELD = (By.CSS_SELECTOR, "input#address2")
    CITY_FIELD = (By.CSS_SELECTOR, "input#city")
    STATE_DROPDOWN = (By.CSS_SELECTOR, "select#id_state")
    POSTAL_CODE_FIELD = (By.CSS_SELECTOR, "input#postcode")
    COUNTRY_DROPDOWN = (By.CSS_SELECTOR, "select#id_country")
    ADDITIONAL_INFO_FIELD = (By.CSS_SELECTOR, "textarea#other")
    HOME_PHONE_FIELD = (By.CSS_SELECTOR, "input#phone")
    MOBILE_PHONE_FIELD = (By.CSS_SELECTOR, "input#phone_mobile")
    ALIAS_FIELD = (By.CSS_SELECTOR, "input#alias")
    SUBMIT_CREATION_OF_ACCOUNT = (By.CSS_SELECTOR, "button#submitAccount")
    WELCOMING_MESSAGE_ACCOUNT_CREATED = (By.CSS_SELECTOR, "p.info-account")
    RED_MESSAGE_ACCOUNT_ALREADY_EXISTS = (By.CSS_SELECTOR, "div#create_account_error.alert.alert-danger li")


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button[name='Submit']")
    PRODUCT_QUANTITY_UP = (By.CSS_SELECTOR, "a.product_quantity_up")
    PRODUCT_IMAGE = (By.CSS_SELECTOR, "img#bigpic")
    PRODUCT_INFO_FIELD = (By.CSS_SELECTOR, "div[class='pb-center-column col-xs-12 col-sm-4']")
    ADD_TO_CART_FIELD =(By.CSS_SELECTOR, "div[class='box-info-product']" )
    VIEW_CART_BUTTON = (By.CSS_SELECTOR , "div.shopping_cart>a")
    SUCCESS_MESSAGE_PRODUCT_ADDED = (By.CSS_SELECTOR, "div#layer_cart>div.clearfix")
    TOTAL_SUM_OF_ADDED_PRODUCT_IN_MESSAGE = (By.CSS_SELECTOR, "span#layer_cart_product_price")
    SELECT_PRODUCT_SIZE = (By.CSS_SELECTOR, "select#group_1")
    CHOSEN_SIZE_IN_MESSAGE = (By.CSS_SELECTOR, "span#layer_cart_product_attributes")
