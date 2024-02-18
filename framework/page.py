from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver import Remote

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC

from logger_init import logger


class Page:
    """Class of basic functional in the Ajax app."""

    def __init__(self, driver: Remote):
        self.driver = driver

    def wait_for_element_by_id(self, element_id: str) -> WebElement:
        """Waits 10 seconds until it finds a web element by id."""
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((MobileBy.ID, element_id)))

    def wait_for_element_by_xpath(self, xpath: str) -> WebElement:
        """Waits 10 seconds until it finds a web element by xpath."""
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((MobileBy.XPATH, xpath)))

    def wait_for_element_by_accessibility_id(self, access_id: str) -> WebElement:
        """Waits 10 seconds until it finds a web element by accessibility id."""
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((MobileBy.ACCESSIBILITY_ID, access_id)))

    def click_on_login_button(self):
        # If user doesn't see the login button, it will skip it
        try:
            el = self.wait_for_element_by_xpath(
                '//android.widget.TextView[@resource-id="com.ajaxsystems:id/text" and @text="Log In"]')
            el.click()
            logger.info("\"Log in\" button in the main menu was clicked.")
        except NoSuchElementException:
            pass
