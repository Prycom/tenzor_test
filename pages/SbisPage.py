from pages.BasePage import BasePage
from locators.SbisLocators import SbisLocators
from selenium.webdriver import ActionChains
import time
import allure
import os
from config import DOWNLOAD_PATH

class SbisPage(BasePage):

    @allure.step('Открываем вкладку контакты')
    def open_contacts(self):
        contacts = self.find_element(SbisLocators.LOCATOR_CONTACTS)
        contacts.click()

    @allure.step('Кликаем на банер Тензор')
    def click_tensor_baner(self):
        baner = self.find_element(SbisLocators.LOCATOR_TENSOR_BANER)
        baner.click()
    
    @allure.step('Получаем текущую локацию')
    def get_location(self):
        location = self.find_element(SbisLocators.LOCATOR_GEO)
        return location.text
    
    @allure.step('Получаем список партнёров в регионе')
    def get_partners(self):
        partners = self.find_elements(SbisLocators.LOCATOR_PARTNER)
        return [partner.text for partner in partners]
    
    @allure.step('Меняем свою текущую локацию на Камчатский край')
    def change_location(self):
        loc_changer = self.get_clickable_element(SbisLocators.LOCATOR_GEO)
        loc_changer.click()
        cumchatka = self.get_clickable_element(SbisLocators.LOCATOR_GEO_CUMCHATKA)
        cumchatka.click()
        time.sleep(2)

    @allure.step("Ищем кнопку 'Скачать СБИС'")
    def search_download(self):
        download_button = self.find_element(SbisLocators.LOCATOR_DOWNLOAD)
        actions = ActionChains(self.driver)
        actions.scroll_to_element(download_button).scroll_by_amount(0, 175).perform()
        return download_button.text
    
    @allure.step("Закрываем сообщение про cookies")
    def close_cookies_notification(self):
        close = self.find_element(SbisLocators.LOCATOR_COOKIES_CLOSE)
        close.click()

    @allure.step("Кликаем кнопку 'Скачать СБИС'")
    def click_download_sbis(self):
        download = self.get_clickable_element(SbisLocators.LOCATOR_DOWNLOAD)
        download.click()
    
    @allure.step("Кликаем кнопку 'СБИС Плагин'")
    def click_sbis_plugin(self):
        plugin = self.get_clickable_element(SbisLocators.LOCATOR_PLUGIN)
        plugin.click()
        time.sleep(1)
        plugin.click()

    @allure.step("Кликаем кнопку 'Скачать' Веб-установщик")
    def download_web_installer(self):
        download = self.get_clickable_element(SbisLocators.LOCATOR_DOWNLOAD_INSTALLER, time=30)
        download.click()
        return download

    @allure.step("Ждём, пока файл установщика скачается в заданную директорию")
    def wait_until_downloaded(self):
        downloaded = False
        
        while(not downloaded):
            if not downloaded:
                time.sleep(2)
            for filename in os.listdir(DOWNLOAD_PATH):
                if filename.endswith('.crdownload'):
                    downloaded = False
                else:
                    downloaded = True
                