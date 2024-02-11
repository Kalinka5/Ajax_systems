import pytest

from framework.sidebar import SideBar


@pytest.fixture(scope='function')
def user_sidebar_fixture(driver):
    yield SideBar(driver)
