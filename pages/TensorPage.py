from pages.BasePage import BasePage
from selenium.webdriver import ActionChains
from locators.TensorLocators import TensorLocators
import allure

class TensorPage(BasePage):
    @allure.step('Ищем заголовок банера')
    def find_title(self):
        """Поиск заголовка 'Сила в людях'"""
        title = self.find_element(TensorLocators.LOCATOR_BLOCK_TITLE)
        actions = ActionChains(self.driver)
        actions.scroll_to_element(title).scroll_by_amount(0, 500).perform()
        return title.text
    
    @allure.step('Кликаем подробнее')
    def click_about(self):
        """Клик по кнопке подробнее"""
        about = self.get_clickable_element(TensorLocators.LOCATOR_ABOUT)
        about.click()
    
    @allure.step("Ищем блок 'Работаем'")
    def get_working_block(self):
        """Ищем раздел 'Работаем'"""
        working = self.find_element(TensorLocators.LOCATOR_WORKING)
        actions = ActionChains(self.driver)
        actions.scroll_to_element(working).scroll_by_amount(0, 700).perform()
        return working.text

    @allure.step("Сравниваем размер картинок в блоке 'Работаем'")
    def is_images_equal_size(self):
        """Сравнивание размеров картинок"""
        imgs = self.find_elements(TensorLocators.LOCATOR_IMAGES)
        sizes = []
        for img in imgs:
            sizes.append((img.size['height'], img.size['width']))
        return all(sizes[0] == size for size in sizes)
    
