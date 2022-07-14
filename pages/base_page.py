from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select, WebDriverWait


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, method, locator):
        """Makes sure element is present"""
        try:
            WebDriverWait(self.browser, 10).until(ec.presence_of_element_located((method, locator)))
        except NoSuchElementException:
            return False
        return True

    def return_element_located(self, method, locator):
        elt = self.browser.find_element(method, locator)
        return elt

    def get_current_url(self):
        cur_url = self.browser.current_url
        return cur_url

    def click_button(self, method, locator):
        self.browser.find_element(method, locator).click()

    def get_text_of_element(self, method, locator):
        self.browser.find_element(method, locator).text()

    def is_disappeared(self, method, locator, timeout=4):
        """makes sure that element disappears within a given time"""
        try:
            WebDriverWait(self.browser, timeout, 1, [TimeoutException]).until_not(
                ec.presence_of_element_located((method, locator))
            )
        except TimeoutException:
            return False
        return True

    def is_not_element_present(self, method, locator, timeout=4):
        """makes sure that element doesn"t appear within a given time"""
        try:
            WebDriverWait(self.browser, timeout).until(ec.presence_of_element_located((method, locator)))
        except TimeoutException:
            return True
        return False

    def element_is_visible(self, method, locator, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(ec.visibility_of_element_located((method, locator)))
        except TimeoutException:
            return False
        return True

    def select_from_dropdown(self, method, locator):
        element = Select(self.return_element_located(method, locator))
        return element
