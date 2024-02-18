from appium.webdriver import Remote

from selenium.common.exceptions import NoSuchElementException

from .page import Page
from logger_init import logger


class LoginPage(Page):
    """Class of elements in login page. This class used to find some elements in a login page."""

    def __init__(self, driver: Remote):
        super().__init__(driver)
    
    def fill_email_input(self, email: str):
        el = self.driver.find_element_by_id('com.ajaxsystems:id/authLoginEmail')

        el.clear()
        el.send_keys(email)

        logger.info(f"\"Email\" field with \"{email}\" value was filled.")

    def fill_password_input(self, password: str):
        el = self.driver.find_element_by_id('com.ajaxsystems:id/authLoginPassword')

        el.clear()
        el.send_keys(password)

        logger.info(f"\"Password\" field with \"{password}\" was filled.")

    def login(self):
        el = self.driver.find_element_by_xpath('//android.widget.TextView[@resource-id="com.ajaxsystems:id/text" and @text="Log In"]')
        el.click()

    def full_login_into_account(self, email: str, password: str):
        logger.info("Start log in to account.")

        self.click_on_login_button()
        self.fill_email_input(email)
        self.fill_password_input(password)
        self.login()

        logger.info("Log in was successful.")

    def sign_out(self):
        logger.info("Start to sign out of account.")

        menu = self.driver.find_element_by_id("com.ajaxsystems:id/menuDrawer")
        menu.click()

        settings = self.driver.find_element_by_id("com.ajaxsystems:id/settings")
        settings.click()

        sign_out = self.driver.find_element_by_xpath('(//androidx.compose.ui.platform.ComposeView[@resource-id="com.ajaxsystems:id/compose_view"])[6]/android.view.View/android.view.View[1]')
        sign_out.click()

        logger.info("Sign out was successful.")

    def click_menu_button(self):
        # If user doesn't see the menu button, it will skip it
        try:
            menu = self.wait_for_element_by_id('com.ajaxsystems:id/menuDrawer')
            menu.click()
            logger.info("\"Menu\" button was clicked.")
        except NoSuchElementException:
            pass
