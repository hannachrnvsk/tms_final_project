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


class UserInfoToCreateAccount:
    """ Contains data necessary to create user in format
    0. First Name
    1. Last Name
    2. Password
    3. Company
    4. Address
    5. Address (Building)
    6. City
    7. Postal Code
    8. Additional Info
    9. Home Phone
    10. Mobile Phone
    11. Alias
     """

    ALL_POSIBLE_VALID_DATA_1 = ["Ivan", "Ivanov", "qwert67*", "TeachMeSkills", "Sikorskego", "65", "Warsaw", "12345", "Married", "456821", "4521893", "ivanushka"]

# class Links:
#     PRODUCT_LINK = "http://automationpractice.com/index.php?id_product=2&controller=product"


blouse = Product("Blouse", 27.00 , 2, "M")

