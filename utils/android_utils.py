import subprocess
from utils.exeptions import NoDevicesError

# Создание собственного класса ошибки для оповещения об отсутсвии приложения


# Метод для определения идентификатора устройства
def initialization_udid():
    identify_device = subprocess.getoutput('adb devices').split()
    if len(identify_device) > 4:
        return identify_device[4]
    raise NoDevicesError('Device is not found')

# Получение версии андроид
def android_version():
    version = subprocess.getoutput('adb shell getprop ro.build.version.release ')
    if version:
        return version
    raise NoDevicesError('Device is not found')

def android_get_desired_capabilities():
    return {
        'autoGrantPermissions': True,
        'automationName': 'uiautomator2',
        'newCommandTimeout': 500,
        'noSign': True,
        'platformName': 'Android',
        'platformVersion': android_version(),
        'resetKeyboard': True,
        'systemPort': 8301,
        'takesScreenshot': True,
        'udid': initialization_udid(),
        'appPackage': 'com.ajaxsystems',
        'appActivity': 'com.ajaxsystems.ui.activity.LauncherActivity'
}
