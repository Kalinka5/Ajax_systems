import pytest
import time

from logger_init import logger


@pytest.mark.parametrize("action, expected_text", [
    ("settings_button", "App Settings"),
    ("help_button", "Help"),
    ("report_button", "Report a Problem"),
    ("add_hub_button", "Add Hub"),
])
def test_sidebar_buttons_displayed_and_enabled(user_sidebar_fixture, action, expected_text):
    if action == "settings_button":
        user_sidebar_fixture.full_login_into_account()
    user_sidebar_fixture.click_menu_button()
    logger.info(f"Testing {action.replace('_', ' ')}")
    element = getattr(user_sidebar_fixture, action)()
    assert element.is_displayed()
    assert element.is_enabled()


@pytest.mark.parametrize("action, expected_text", [
    ("settings_text_view", "App Settings"),
    ("help_text_view", "Help"),
    ("report_text_view", "Report a Problem"),
    ("add_hub_text_view", "Add Hub"),
    ("terms_of_service_text_view", "Terms of Service"),
    ("version_text_view", "v 2.35.2 (build #6333)"),
])
def test_sidebar_text_view_displayed(user_sidebar_fixture, action, expected_text):
    user_sidebar_fixture.click_menu_button()
    logger.info(f"Testing {action.replace('_', ' ')}")
    element = getattr(user_sidebar_fixture, action)()
    assert element.text == expected_text
    assert element.is_displayed()


@pytest.mark.parametrize("action, button", [
    ("click_settings_button", "Settings"),
    ("click_help_button", "Help"),
    ("click_add_hub_button", "Add Hub"),
    ("click_report_button", "Report a Problem"),
])
def test_sidebar_click_buttons(user_sidebar_fixture, action, button):
    user_sidebar_fixture.click_menu_button()
    logger.info(f"Testing {action.replace('_', ' ')}")
    getattr(user_sidebar_fixture, action)()
    if button == "Settings":
        items = user_sidebar_fixture.find_element_by_id('com.ajaxsystems:id/items')
        assert items.is_displayed()
        back = user_sidebar_fixture.find_element_by_id('com.ajaxsystems:id/back')
        back.click()
    elif button == "Help":
        title = user_sidebar_fixture.find_element_by_id("com.ajaxsystems:id/toolbarTitle")
        assert title.text == "Installation Manuals"
        button_item = user_sidebar_fixture.find_element_by_accessibility_id("Button")
        assert button_item.is_displayed()
        button_s_jeweller_item = user_sidebar_fixture.find_element_by_accessibility_id("Button S Jeweller")
        assert button_s_jeweller_item.is_displayed()
        combi_protect_item = user_sidebar_fixture.find_element_by_accessibility_id("CombiProtect")
        assert combi_protect_item.is_displayed()
        back = user_sidebar_fixture.find_element_by_id('com.ajaxsystems:id/back')
        back.click()
    elif button == "Add Hub":
        title = user_sidebar_fixture.find_element_by_id('com.ajaxsystems:id/title')
        assert title.text == "Add Hub"
        body = user_sidebar_fixture.find_element_by_id('com.ajaxsystems:id/body')
        assert body.text == "You can add the hub using step-by-step tutorial or manually"
        back = user_sidebar_fixture.find_element_by_id('com.ajaxsystems:id/backButton')
        back.click()
    else:
        title = user_sidebar_fixture.find_element_by_xpath('//android.widget.TextView[@resource-id="com.ajaxsystems:id/title" and @text="Report a Problem"]')
        assert title.text == "Report a Problem"
    time.sleep(3)
