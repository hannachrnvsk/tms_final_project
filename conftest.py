import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import fake_useragent

user = fake_useragent.UserAgent().random


# def pytest_addoption(parser):
#     """Opportunity to run tests in different languages"""
#     parser.addoption('--language', action='store', default="en",
#                       help="Choose lang: en or ru")


@pytest.fixture(scope="function")
def browser(request):
    # language = request.config.getoption("language")
    print("\nstart browser for test..")
    options = Options()
    options.binary_location = "/usr/bin/google-chrome"
    # options.add_experimental_option('prefs', {'intl.accept_languages': language})
    options.add_argument("--headless") # change to "chrome" to see
    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-setuid-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1980,1080")
    options.add_argument(f"user-agent = {user}")
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    yield browser
    print("\nmust quit browser..")
    browser.quit()

