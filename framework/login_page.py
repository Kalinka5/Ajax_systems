from selenium.common.exceptions import NoSuchElementException

import time

from .page import Page
from logger_init import logger


class LoginPage(Page):
    """Class of elements in login page. This class used to find some elements in a login page."""

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_login_button(self):
        # If user doesn't see the login button, it will skip it
        try:
            el = self.find_element_by_xpath('//android.widget.TextView[@resource-id="com.ajaxsystems:id/text" and @text="Log In"]')
            self.click_element(el)
            logger.info("\"Log in\" button in the main menu was clicked.")
            time.sleep(2)
        except NoSuchElementException:
            pass
    
    def fill_email_input(self, email):
        el = self.find_element_by_id('com.ajaxsystems:id/authLoginEmail')
        el.clear()
        self.fill_input(el, email)
        logger.info("\"Email\" field was filled.")

    def fill_password_input(self, password):
        el = self.find_element_by_id('com.ajaxsystems:id/authLoginPassword')
        el.clear()
        self.fill_input(el, password)
        logger.info("\"Password\" field was filled.")

    def login(self):
        el = self.find_element_by_xpath('//android.widget.TextView[@resource-id="com.ajaxsystems:id/text" and @text="Log In"]')
        self.click_element(el)
        logger.info("Log in to account.")

    def full_login_into_account(self):
        logger.info("Start log in to account.")
        self.click_on_login_button()
        self.fill_email_input("qa.ajax.app.automation@gmail.com")
        self.fill_password_input("qa_automation_password")
        self.login()
        logger.info("Log in was successful.")
        time.sleep(3)
