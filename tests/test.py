from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.TensorPage import TensorPage
from pages.SbisPage import SbisPage
import allure

@pytest.fixture()
def driver():
    opts = webdriver.ChromeOptions()
    #opts.add_argument("--no-sandbox")
    #opts.add_argument("--disable-dev-shm-usage")
    #opts.add_argument("--disable-blink-features=AutomationControlled")
    #opts.add_argument("--disable-notifications")
    opts.enable_downloads = True
    opts.add_experimental_option("prefs", {
        "download.default_directory": r"C:\Users\downloads",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": False
    })
    driver = webdriver.Chrome(options=opts)
    driver.maximize_window()
    
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

        sbis_page.download_web_installer()

        sleep(20)




