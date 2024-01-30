from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage():
    def __init__(self, driver) -> None:
        self.driver = driver
        self.base_url = 'https://sbis.ru/'

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator), message=f'Не удалось найти элемент {locator}')
    
    def find_elements(self, locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(locator), message=f"Не удалось найти элементы {locator}")

    def switch_tab(self, idx=-1):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[idx]) # switch selenium to new tab

    def get_clickable_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator))

    def go_to_site(self):
        return self.driver.get(self.base_url)