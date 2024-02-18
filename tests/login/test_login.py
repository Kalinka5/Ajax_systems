import pytest

from logger_init import logger


@pytest.mark.parametrize('login, password', [
    pytest.param('qa.ajax.app.automation@gmail.com', 'qa_automation_password', id='valid_login'),
])
def test_valid_user_login(user_login_fixture, login, password):
    logger.info(f'Attempting login with email: {login}, password: {password}')
    user_login_fixture.full_login_into_account(login, password)

    message = user_login_fixture.wait_for_element_by_id('com.ajaxsystems:id/addFirstHub')
    assert message.is_displayed()

    user_login_fixture.sign_out()


@pytest.mark.parametrize('login, password, error_message_text', [
    pytest.param('invalid@gmail.com', 'invalid_password', 'Wrong login or password', id='wrong_login_or_password'),
    pytest.param('invalid@gmail.com', 'qa_automation_password', 'Wrong login or password', id='wrong_login_or_password'),
    pytest.param('qa.ajax.app.automation@gmail.com', 'invalid_password', 'Wrong login or password', id='wrong_login_or_password'),
    pytest.param('aaaaaaaaaa', 'invalid_password', 'Invalid email format', id='invalid_email_format'),
    pytest.param('@@@@@@@@@@', 'invalid_password', 'Invalid email format', id='invalid_email_format'),
    pytest.param('1234567890', 'invalid_password', 'Invalid email format', id='invalid_email_format'),
    pytest.param('dfsdb2312@', 'invalid_password', 'Invalid email format', id='invalid_email_format'),
    pytest.param('@rtrf53434', 'invalid_password', 'Invalid email format', id='invalid_email_format'),
])
def test_invalid_user_login(user_login_fixture, login, password, error_message_text):
    logger.info(f'Attempting login with email: {login}, password: {password}')
    user_login_fixture.full_login_into_account(login, password)

    logger.error('Login failed.')
    error_message = user_login_fixture.wait_for_element_by_id('com.ajaxsystems:id/snackbar_text')
    assert error_message.is_displayed()

    logger.error(f'Shows window with text "{error_message_text}".')
    assert error_message.text == error_message_text


@pytest.mark.parametrize('login, password', [
    pytest.param('', 'qa_automation_password', id='empty_login_field'),
    pytest.param('', 'invalid_password', id='empty_login_field'),
    pytest.param('qa.ajax.app.automation@gmail.com', '', id='empty_password_field'),
    pytest.param('invalid@gmail.com', '', id='empty_password_field'),
    pytest.param('', '', id='empty_both_fields')
])
def test_empty_email_or_password_fields(user_login_fixture, login, password):
    logger.info(f'Attempting login with email: {login}, password: {password}')
    user_login_fixture.full_login_into_account(login, password)

    logger.error('Login failed.')
    login_button = user_login_fixture.driver.find_element_by_xpath('(//androidx.compose.ui.platform.ComposeView[@resource-id="com.ajaxsystems:id/compose_view"])[4]/android.view.View/android.view.View')
    logger.error('"Log in" button is NOT clickable.')
    assert not login_button.is_enabled()
