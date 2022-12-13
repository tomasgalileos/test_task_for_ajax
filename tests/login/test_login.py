import pytest
from time import sleep
from selenium.webdriver.common.by import By
import logging

# Настройка для логирования шагов
logging.basicConfig(level=logging.INFO,
                    filename="../../tests/test.log",
                    filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")


# Фикстура для нажатия на кнопку авторизации
@pytest.fixture
def click_bottom_auth_fixture(user_login_fixture):
    driver = user_login_fixture
    driver.click_element(By.ID, 'com.ajaxsystems:id/login')
    logging.info('Login page was opened!')
    sleep(2)


@pytest.mark.usefixtures('click_bottom_auth_fixture')
class TestProfileAuthorization:
    # Позитивный тест и проверка наличия sideBar и hubApp
    @pytest.mark.parametrize('login, password',
                             [('qa.ajax.app.automation@gmail.com', 'qa_automation_password')])
    def test_positive_login(self, user_login_fixture, login, password):
        driver = user_login_fixture
        logging.info(f'Try to enter login: {login}')
        driver.send_keys(login, By.ID, 'com.ajaxsystems:id/login')
        logging.info('Success!')
        logging.info(f'Try to enter password: {password}')
        driver.send_keys(password, By.ID, 'com.ajaxsystems:id/password')
        logging.info('Success!')
        logging.info('Click bottom for authorization.')
        driver.click_element(By.ID, 'com.ajaxsystems:id/next')
        sleep(5)
        logging.info('Searching the elements on the page...')
        assert driver.search_element(By.ID, 'com.ajaxsystems:id/hubAdd') and \
               driver.search_element(By.ID, 'com.ajaxsystems:id/menuDrawer')
        logging.info('Authorization success!')

    # Негативный тест и проверка остался ли пользователь на страничке после
    # авторизации
    @pytest.mark.parametrize('login, password',
                             [('some_log', 'some_pas'),
                              ('some_log', 'qa_automation_password'),
                              ('qa.ajax.app.automation@gmail.com', 'some_pas'),
                              ('', '')])
    def test_negative_login(self, user_login_fixture, login, password):
        driver = user_login_fixture
        logging.info(f'Try to enter login: {login}')
        driver.send_keys(login, By.ID, 'com.ajaxsystems:id/login')
        logging.info('Success!')
        logging.info(f'Try to enter password: {password}')
        driver.send_keys(password, By.ID, 'com.ajaxsystems:id/password')
        logging.info('Success!')
        logging.info('Click bottom for authorization.')
        driver.click_element(By.ID, 'com.ajaxsystems:id/next')
        sleep(2)
        logging.info('Searching the elements on the page...')
        assert driver.search_element(By.ID, 'com.ajaxsystems:id/login') and \
               driver.search_element(By.ID, 'com.ajaxsystems:id/password')
        logging.info('User stay at page!')


