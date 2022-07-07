from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as  EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self,method, locator):
        try:
            WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((method,locator)))
        except NoSuchElementException:
            return False
        return True

    def return_element_located(self,method,locator):
        elt = self.browser.find_element(method,locator)
        return elt

    def get_current_url(self):
        cur_url = self.browser.current_url
        return cur_url

    def click_button(self, method, locator):
        self.browser.find_element(method, locator).click()

    def get_text_of_element(self,method, locator):
        self.browser.find_element(method,locator).text()

    def is_disappeared(self, method, locator, timeout=4):
        """проверяет, что элемент исчезает в течение заданного времени"""
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((method, locator)))
        except TimeoutException:
            return False
        return True

    def is_not_element_present(self, method, locator, timeout=4):
        """проверяет, что элемент не появляется на странице в течение заданного времени"""
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((method, locator)))
        except TimeoutException:
            return True
        return False