from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class BaseObject:
    def __init__(self, driver: Chrome, wait: WebDriverWait):
        self.driver = driver
        self.wait = wait