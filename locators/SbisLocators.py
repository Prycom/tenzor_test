from selenium.webdriver.common.by import By

class SbisLocators():
    LOCATOR_CONTACTS = (By.XPATH, '//*[@id="wasaby-content"]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/a')
    LOCATOR_TENSOR_BANER = (By.XPATH, '//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a')
    LOCATOR_GEO = (By.XPATH, '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span')
    LOCATOR_PARTNER = (By.CLASS_NAME, 'sbisru-Contacts-List__name')
    LOCATOR_GEO_CUMCHATKA = (By.XPATH, '//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span')
    LOCATOR_DOWNLOAD = (By.XPATH, '//*[@id="container"]/div[2]/div[1]/div[3]/div[10]/ul/li[6]/a')
    LOCATOR_PLUGIN = (By.XPATH, "//div[text()='СБИС Плагин']/../../..")
    LOCATOR_COOKIES_CLOSE = (By.XPATH, '//*[@id="wasaby-content"]/div/div/div[2]/div[1]/div[3]/div[2]/div[2]')
    LOCATOR_DOWNLOAD_INSTALLER = (By.XPATH, "//h3[text()='Веб-установщик ']/../..//a")