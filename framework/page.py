from selenium.common.exceptions import NoSuchElementException

class Page:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *remote):
        return self.driver.find_element(*remote)

    def click_element(self, *remote):
        return self.driver.find_element(*remote).click()

    def search_element(self, *remote):
        try:
            self.find_element(*remote)
        except NoSuchElementException:
            return False
        return True

    def send_keys(self, value, *remote):
        element = self.find_element(*remote)
        element.clear()
        element.set_value(value)

