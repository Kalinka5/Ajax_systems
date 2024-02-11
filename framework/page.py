import time

from appium.webdriver import Remote


class Page:

    def __init__(self, driver: Remote):
        self.driver = driver

    def find_element_by_id(self, id: str):
        el = self.driver.find_element_by_id(id)
        return el

    def find_element_by_accessibility_id(self, access_id: str):
        el = self.driver.find_element_by_accessibility_id(access_id)
        return el

    def find_element_by_xpath(self, xpath: str):
        el = self.driver.find_element_by_xpath(xpath)
        return el

    def find_element_by_class(self, class_name: str):
        el = self.driver.find_element_by_class_name(class_name)
        return el

    def click_element(self, el):
        el.click()

    def fill_input(self, el, input_value):
        el.send_keys(input_value)

    def sign_out(self):
        menu = self.driver.find_element_by_id("com.ajaxsystems:id/menuDrawer")
        self.click_element(menu)
        settings = self.driver.find_element_by_id("com.ajaxsystems:id/settings")
        self.click_element(settings)
        sign_out = self.driver.find_element_by_xpath('(//androidx.compose.ui.platform.ComposeView[@resource-id="com.ajaxsystems:id/compose_view"])[6]/android.view.View/android.view.View[1]')
        self.click_element(sign_out)
        time.sleep(3)
