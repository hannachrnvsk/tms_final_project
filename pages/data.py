class Product:

    def __init__(self, name, price ,amount,size):
        self.name = name
        self.price = price
        self.amount = amount
        self.size = size
        self.total_sum = "$" + str((price * amount)) +"0"


class Emails:

    VALID_EMAIL = "ivan_smirnov@gmail.com"
    VALID_EMAIL_WITH_NUM = "ivan_smirnov98@gmail.com"
    EMAIL_WITHOUT_DOMEN = "ivan_smirnov"
    EMAIL_WITHOUT_COMMERCIAL_AT = "ivan_smirnovgmail.com"
    EMAIL_WITH_SPEC_SYMBOL = "ivan#smirnov$@gmail.com"
    BLANK_EMAIL = ""


class Users:
    def __init__(self, first_name=None, last_name=None, email=None, password=None,
                 day_of_birth=None, month_of_birth=None, year_of_birth=None,
                 company=None, address_street=None, address_build=None,
                 city=None, state=None ,postal_code=None, country=None, additional_info=None,home_phone=None,
                 mobile_phone=None, alias=None ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.day_of_birth = day_of_birth
        self.month_of_birth = month_of_birth
        self.year_of_birth = year_of_birth
        self.company = company
        self.address_street = address_street
        self.address_build = address_build
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country
        self.additional_info = additional_info
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.alias = alias


valid_user_already_created = Users("Kate", "Romanova", "romakat@gmail.com", "qwerts37",
                   "23","7", "2000", "TeachMeSkills", "kalinovskogo",
                   "24","Wasrsaw", "Arizona", "45871", "United States",
                   "married", "2345678", "14256379", "romakat")








