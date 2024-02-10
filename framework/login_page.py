from selenium.common.exceptions import NoSuchElementException

import time

from .page import Page


class LoginPage(Page):

    def __init__(self, driver):
        super().__init__(driver)

    def click_on_login_button(self):
        try:
            el = self.find_element_by_xpath('//android.widget.TextView[@resource-id="com.ajaxsystems:id/text" and @text="Log In"]')
            self.click_element(el)
            time.sleep(2)
        except NoSuchElementException:
            pass
    
    def fill_email_input(self, email):
        el = self.find_element_by_id('com.ajaxsystems:id/authLoginEmail')
        el.clear()
        self.fill_input(el, email)

    def fill_password_input(self, password):
        el = self.find_element_by_id('com.ajaxsystems:id/authLoginPassword')
        el.clear()
        self.fill_input(el, password)

    def login(self):
        el = self.find_element_by_xpath('//android.widget.TextView[@resource-id="com.ajaxsystems:id/text" and @text="Log In"]')
        self.click_element(el)
