import logging
import pytest
from time import sleep
from selenium.webdriver.common.by import By

# Настройка для логирования шагов
logging.basicConfig(level=logging.INFO,
                    filename="../../tests/test.log",
                    filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")


# Фикстура для авторизации в приложении.
@pytest.fixture(scope='module', autouse=True)
def authorization_fixture(menu_drawer_fixture):
    driver = menu_drawer_fixture
    login = 'qa.ajax.app.automation@gmail.com'
    password = 'qa_automation_password'
    driver.click_element(By.ID, 'com.ajaxsystems:id/login')
    logging.info('Login page was opened!')
    sleep(2)
    logging.info(f'Try to enter login: {login}')
    driver.send_keys(login, By.ID, 'com.ajaxsystems:id/login')
    logging.info('Success!')
    logging.info(f'Try to enter password: {password}')
    driver.send_keys(password, By.ID, 'com.ajaxsystems:id/password')
    logging.info('Success!')
    logging.info('Click bottom for authorization.')
    driver.click_element(By.ID, 'com.ajaxsystems:id/next')
    logging.info('Authorization success!')
    sleep(5)
    yield


# Элементы sidebar и значения, которые необходимо будет найти
sidebar_elements = [
    ('com.ajaxsystems:id/addHub', 'com.ajaxsystems:id/include'),
    ('com.ajaxsystems:id/settings',
     'com.ajaxsystems:id/accountInfoEditAccountNavigate'),
    ('com.ajaxsystems:id/help', 'com.ajaxsystems:id/navigation'),
    ('com.ajaxsystems:id/logs', 'com.ajaxsystems:id/sendButton'),
    ('com.ajaxsystems:id/camera', 'com.ajaxsystems:id/hikvision'),
    ('com.ajaxsystems:id/documentation_text', 'com.ajaxsystems:id/arrow')
]


# Тест, который проходит по каждому пунтку sidebar и находит элемент соответсвующий
# пункту меню.
@pytest.mark.usefixtures('authorization_fixture')
@pytest.mark.parametrize('resource_id, result_id', sidebar_elements)
def test_sidebar_elements(menu_drawer_fixture, resource_id, result_id):
    driver = menu_drawer_fixture
    logging.info('Open the menuDrawer')
    sleep(2)
    driver.click_element(By.ID, 'com.ajaxsystems:id/menuDrawer')
    sleep(2)
    logging.info(f'Click to bottom with id: {resource_id}')
    driver.click_element(By.ID, resource_id)
    logging.info('Success!')
    sleep(2)
    logging.info(f'Searching the element with id: {result_id}')
    assert driver.search_element(By.ID, result_id)
    logging.info('The element was found!')

    
# Фикстура для возвращения к menuDrawer
@pytest.fixture(scope='function', autouse=True)
def close_sidebar_fixture(menu_drawer_fixture):
    yield
    driver = menu_drawer_fixture
    if driver.search_element(By.ID, 'com.ajaxsystems:id/back'):
        logging.info('Press the bottom to return in menuDrawer')
        driver.click_element(By.ID, 'com.ajaxsystems:id/back')
        return
    if driver.search_element(By.ID, 'com.ajaxsystems:id/backButton'):
        logging.info('Press the bottom to return in menuDrawer')
        driver.click_element(By.ID, 'com.ajaxsystems:id/backButton')
        return
    if driver.search_element(By.ID, 'com.ajaxsystems:id/sendButton'):
        logging.info('Press "delete" to return in menuDrawer')
        driver.click_element(By.ID, 'com.ajaxsystems:id/sendButton')
        return
