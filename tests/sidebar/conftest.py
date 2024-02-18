import pytest

from framework.login_page import LoginPage


@pytest.fixture(scope='module')
def user_sidebar_fixture(driver):
    yield LoginPage(driver)
