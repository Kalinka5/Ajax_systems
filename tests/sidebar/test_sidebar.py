import pytest

from logger_init import logger


@pytest.fixture(scope='module', autouse=True)
def login_to_app(user_sidebar_fixture):
    user_sidebar_fixture.full_login_into_account('qa.ajax.app.automation@gmail.com', 'qa_automation_password')
    yield


@pytest.mark.parametrize('button_name, find_by, selector', [
    pytest.param('App Settings', 'xpath', '//android.widget.TextView[@resource-id="com.ajaxsystems:id/title" and @text="App Settings"]'),
    pytest.param('Help', 'xpath', '//android.widget.TextView[@resource-id="com.ajaxsystems:id/title" and @text="Help"]'),
    pytest.param('Report a Problem', 'xpath', '//android.widget.TextView[@resource-id="com.ajaxsystems:id/title" and @text="Report a Problem"]'),
    pytest.param('Add Hub', 'id', 'com.ajaxsystems:id/text'),
    pytest.param('Terms of Service', 'id', 'com.ajaxsystems:id/documentation_text'),
    pytest.param('v 2.35.2 (build #6333)', 'id', 'com.ajaxsystems:id/build'),
])
def test_sidebar_text_views(user_sidebar_fixture, button_name, find_by, selector):
    user_sidebar_fixture.click_menu_button()

    logger.info(f'Testing text view of "{button_name}" button')
    if find_by == 'id':
        element = user_sidebar_fixture.wait_for_element_by_id(selector)
    else:
        element = user_sidebar_fixture.wait_for_element_by_xpath(selector)

    assert element.is_displayed()

    logger.info(f'Text of the button is "{element.text}"')
    assert element.text == button_name


@pytest.mark.parametrize('button_name, button_xpath, page_title, find_by, back_button', [
    pytest.param('App Settings', '//android.view.View[@resource-id="com.ajaxsystems:id/settings"]', 'Settings', 'id', 'com.ajaxsystems:id/back'),
    pytest.param('Help', '//android.view.View[@resource-id="com.ajaxsystems:id/help"]', 'Installation Manuals', 'id', 'com.ajaxsystems:id/back'),
    pytest.param('Report a problem', '//android.widget.Button', 'Add Hub', 'id', 'com.ajaxsystems:id/backButton'),
    pytest.param('Add Hub', '//android.view.View[@resource-id="com.ajaxsystems:id/logs"]', 'Report a Problem', 'xpath', 'com.ajaxsystems:id/touch_outside'),
])
def test_sidebar_click_buttons(user_sidebar_fixture, button_name, button_xpath, page_title, find_by, back_button):
    user_sidebar_fixture.click_menu_button()

    logger.info(f'Testing "{button_name}" button')
    element = user_sidebar_fixture.wait_for_element_by_xpath(button_xpath)

    assert element.is_displayed()
    assert element.is_enabled()
    logger.info(f'The "{button_name}" button is enabled')

    element.click()
    logger.info(f'The "{button_name}" button was clicked')

    if find_by == "id":
        title = user_sidebar_fixture.wait_for_element_by_id('com.ajaxsystems:id/toolbarTitle')
    else:
        title = user_sidebar_fixture.wait_for_element_by_xpath('//android.widget.TextView[@resource-id="com.ajaxsystems:id/title" and @text="Report a Problem"]')

    logger.info(f'The page title is "{title.text}"')
    assert title.text == page_title

    logger.info('Back to Main menu')
    back = user_sidebar_fixture.wait_for_element_by_id(back_button)
    back.click()
