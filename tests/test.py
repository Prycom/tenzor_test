from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.TensorPage import TensorPage
from pages.SbisPage import SbisPage
import allure
from config import CHROME_PREFS, DOWNLOAD_PATH
import os

@pytest.fixture()
def driver():
    opts = webdriver.ChromeOptions()
    opts.add_argument("headless")
    opts.add_experimental_option("prefs", CHROME_PREFS)
    driver = webdriver.Chrome(options=opts)
    
    yield driver
    
    driver.close()
    driver.quit()

@allure.feature("Тестовые сценарии")
class Tests():
    @allure.title("Тест 1")
    @allure.severity("critical")
    def test_1(self, driver):
        
        sbis_page = SbisPage(driver)
        sbis_page.go_to_site()
        assert "СБИС" in driver.title
        assert "https://sbis.ru/" in driver.current_url
        
        sbis_page.open_contacts()
        assert "Контакты" in driver.title
        assert "sbis.ru/contacts" in driver.current_url
        
        sbis_page.click_tensor_baner()
        tensor_page = TensorPage(driver)
        tensor_page.switch_tab()
        assert "https://tensor.ru/" in driver.current_url
        assert "Сила в людях" in tensor_page.find_title()
        
        tensor_page.click_about()
        assert "https://tensor.ru/about" in driver.current_url

        assert "Работаем" in tensor_page.get_working_block()

        assert tensor_page.is_images_equal_size()
    
    @allure.title("Тест 2")
    @allure.severity("critical")
    def test_2(self, driver):
        
        sbis_page = SbisPage(driver)
        sbis_page.go_to_site()
        assert "СБИС" in driver.title
        assert "https://sbis.ru/" in driver.current_url
        
        sbis_page.open_contacts()
        assert "Контакты" in driver.title
        assert "sbis.ru/contacts" in driver.current_url
        
        partners = sbis_page.get_partners()
        assert "Новосибирская обл." in sbis_page.get_location()
        assert partners is not None
        
        sbis_page.change_location()
        assert "Камчатский край" in driver.title
        assert "41-kamchatskij-kraj" in driver.current_url
        assert partners is not sbis_page.get_partners()
    
    @allure.title("Тест 3")
    @allure.severity("minor")
    def test_3(self, driver):
        
        sbis_page = SbisPage(driver)
        sbis_page.go_to_site()
        assert "СБИС" in driver.title
        assert "https://sbis.ru/" in driver.current_url

        sbis_page.close_cookies_notification()

        assert "Скачать СБИС" in sbis_page.search_download()
        sbis_page.click_download_sbis()
        assert "download?tab=ereport" in driver.current_url

        sbis_page.click_sbis_plugin()
        assert "tab=plugin" in driver.current_url

        # Получвем размер Веб-установщика
        installer_size = sbis_page.download_web_installer().text.split()[2]
        installer_size = float(installer_size)
        
        sbis_page.wait_until_downloaded()
        
        # Получаем размер скачанного файла
        downloaded_size = os.stat(DOWNLOAD_PATH+'sbisplugin-setup-web.exe').st_size / (1024 * 1024)
        
        assert abs(downloaded_size - installer_size) < 0.001
        
        
        
        




