import random
import string


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
    def __init__(self, first_name=None, last_name=None, email= None, password=None,
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

user_invalid_password = Users("Gloria", "Bronson", "nonsons@mail.ru", "q",
                   "15","6", "1996", "TeachMeSkills", "mirskogo",
                   "24","New-York", "California", "45871", "United States",
                   "married", "2342178", "14356379", "bronialex")

user_invalid_postalcode = Users("Gloria", "Bronson", "lion@mail.ru", "q234567",
                   "15","6", "1996", "TeachMeSkills", "mirskogo",
                   "24","New-York", "California", "45871th8ui", "United States",
                   "married", "2342178", "14356379", "bronialex")

user_invalid_date_of_birth = Users("Gloria", "Bronson", "anson@mail.ru", "gloriab",
                   "31","2", "1996", "TeachMeSkills", "mirskogo",
                   "24","New-York", "California", "45871", "United States",
                   "married", "2342178", "14356379", "bronialex")

user_invalid_mobile_phone = Users("Gloria", "Bronson", "abrumio@mail.ru", "qgtytjt",
                   "15","6", "1996", "TeachMeSkills", "mirskogo",
                   "24","New-York", "California", "45871", "United States",
                   "married", "2342178", "rdghynu8yh", "bronialex")

user_invalid_name = Users("123456", "Bronson", "ayro@mail.ru", "qgtytjt",
                   "15","6", "1996", "TeachMeSkills", "mirskogo",
                   "24","New-York", "California", "45871", "United States",
                   "married", "2342178", "14356379", "bronialex")

user_invalid_homephone = Users("123456", "Bronson", "ay67o@mail.ru", "qgtytjt",
                   "15","6", "1996", "TeachMeSkills", "mirskogo",
                   "24","New-York", "California", "45871", "United States",
                   "married", "djgnkj", "14356379", "bronialex")



class RandomUsers:
    def __init__(self, state=None, country=None):
        self.first_name = ''.join(random.choice(string.ascii_lowercase) for i in range(8))
        self.last_name = ''.join(random.choice(string.ascii_lowercase) for i in range(8))
        self.email = self.first_name + "@gmail.com"
        self.password = random.randint(10000, 999999)
        self.day_of_birth = str(random.randint(1, 28))
        self.month_of_birth = str(random.randint(1, 12))
        self.year_of_birth = str(random.randint(1965, 2004))
        self.company = ''.join(random.choice(string.ascii_lowercase) for i in range(8))
        self.address_street = ''.join(random.choice(string.ascii_lowercase) for i in range(8))
        self.address_build = random.randint(1, 999)
        self.city = ''.join(random.choice(string.ascii_lowercase) for i in range(7))
        self.state = state
        self.postal_code = random.randint(10000, 99999)
        self.country = country
        self.additional_info = ''.join(random.choice(string.ascii_lowercase) for i in range(8))
        self.home_phone = random.randint(10000, 999999)
        self.mobile_phone = random.randint(100000, 9999999)
        self.alias = ''.join(random.choice(string.ascii_lowercase) for i in range(8))




