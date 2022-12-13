import pytest

from framework.login_page import LoginPage


@pytest.fixture(scope='function')
def user_login_fixture(driver):
    yield LoginPage(driver)

# Автоматическая фикстура для сброса приложения
@pytest.fixture(autouse=True)
def app_reset_fixture(driver):
    yield
    driver.reset()
