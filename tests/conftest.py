import logging
import subprocess
import time
import pytest
from appium import webdriver

from utils.android_utils import android_get_desired_capabilities

logging.basicConfig(level=logging.INFO,
                    filename="../../tests/test.log",
                    filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")


@pytest.fixture(scope='session')
def run_appium_server():
    logging.info('Appium server is loading')
    subprocess.Popen(
        ['appium', '-a', '0.0.0.0', '-p', '4723', '--allow-insecure',
         'adb_shell'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=True
    )
    time.sleep(5)
    logging.info('Connected successfully')


@pytest.fixture(scope='session')
def driver(run_appium_server):
    logging.info('Connecting to UiAutomator2')
    driver = webdriver.Remote('http://localhost:4723/wd/hub',
                              android_get_desired_capabilities())
    logging.info('Connected to UiAutomator2')
    yield driver
