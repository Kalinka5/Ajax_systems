from selenium.common.exceptions import NoSuchElementException

from .login_page import LoginPage


class SideBar(LoginPage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_menu_button(self):
        try:
            menu = self.find_element_by_id('com.ajaxsystems:id/menuDrawer')
            menu.click()
        except NoSuchElementException:
            pass

    def settings_button(self):
        el = self.find_element_by_id('com.ajaxsystems:id/settings')
        return el

    def settings_text_view(self):
        el = self.find_element_by_xpath('//android.widget.TextView[@resource-id="com.ajaxsystems:id/title" and @text="App Settings"]')
        return el

    def help_button(self):
        el = self.find_element_by_id('com.ajaxsystems:id/help')
        return el

    def help_text_view(self):
        el = self.find_element_by_xpath('//android.widget.TextView[@resource-id="com.ajaxsystems:id/title" and @text="Help"]')
        return el

    def report_button(self):
        el = self.find_element_by_id('com.ajaxsystems:id/logs')
        return el

    def report_text_view(self):
        el = self.find_element_by_xpath('//android.widget.TextView[@resource-id="com.ajaxsystems:id/title" and @text="Report a Problem"]')
        return el

    def add_hub_button(self):
        el = self.find_element_by_class('android.widget.Button')
        return el

    def add_hub_text_view(self):
        el = self.find_element_by_xpath('(//android.widget.TextView[@resource-id="com.ajaxsystems:id/text"])[2]')
        return el

    def terms_of_service_text_view(self):
        el = self.find_element_by_id('com.ajaxsystems:id/documentation_text')
        return el

    def version_text_view(self):
        el = self.find_element_by_id('com.ajaxsystems:id/build')
        return el

    def click_settings_button(self):
        self.settings_button().click()

    def click_help_button(self):
        self.help_button().click()

    def click_report_button(self):
        self.report_button().click()

    def click_add_hub_button(self):
        self.add_hub_button().click()
