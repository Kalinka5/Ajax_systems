import pytest

import logging
import time


logger = logging.getLogger(__name__)


@pytest.mark.parametrize("login, password, expect_login", [
    ("qa.ajax.app.automation@gmail.com", "qa_automation_password", True),
    ("invalid@gmail.com", "invalid_password", "Wrong login or password"),
    ("invalid@gmail.com", "qa_automation_password", "Wrong login or password"),
    ("qa.ajax.app.automation@gmail.com", "invalid_password", "Wrong login or password"),
    ("aaaaaaaaaa", "invalid_password", "Invalid email format"),
    ("", "qa_automation_password", "Not clickable button"),
    ("", "invalid_password", "Not clickable button"),
    ("qa.ajax.app.automation@gmail.com", "", "Not clickable button"),
    ("invalid@gmail.com", "", "Not clickable button"),
    ("", "", "Not clickable button")
])
def test_user_login(user_login_fixture, login, password, expect_login):
    logger.info(f"Attempting login with email: {login}, password: {password}")
    user_login_fixture.click_on_login_button()
    user_login_fixture.fill_email_input(login)
    user_login_fixture.fill_password_input(password)
    user_login_fixture.login()
    time.sleep(2)
    if expect_login is True:
        time.sleep(3)
        message = user_login_fixture.find_element_by_id("com.ajaxsystems:id/addFirstHub")
        assert message.is_displayed()
        logger.info("Login successful.")
        logger.info("Starting to sign out.")
        user_login_fixture.sign_out()
        logger.info("Sign out successful.")
    elif expect_login == "Wrong login or password":
        error_message = user_login_fixture.find_element_by_id("com.ajaxsystems:id/snackbar_text")
        assert error_message.is_displayed()
        logger.error("Login failed.")
        assert error_message.text == "Wrong login or password"
        logger.error("Shows window with text \"Wrong login or password\".")
    elif expect_login == "Invalid email format":
        error_message = user_login_fixture.find_element_by_id("com.ajaxsystems:id/snackbar_text")
        assert error_message.is_displayed()
        logger.error("Login failed.")
        assert error_message.text == "Invalid email format"
        logger.error("Shows window with text \"Invalid email format\".")
    elif expect_login == "Not clickable button":
        login_button = user_login_fixture.find_element_by_xpath('(//androidx.compose.ui.platform.ComposeView[@resource-id="com.ajaxsystems:id/compose_view"])[4]/android.view.View/android.view.View')
        assert not login_button.is_enabled()
        logger.error("Login failed. \"Log in\" button is NOT clickable.")
