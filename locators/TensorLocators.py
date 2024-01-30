from selenium.webdriver.common.by import By

class TensorLocators():
    LOCATOR_BLOCK_TITLE = (By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[1]')
    LOCATOR_ABOUT = (By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a')
    LOCATOR_WORKING = (By.XPATH, '//*[@id="container"]/div[1]/div/div[4]/div[1]/h2')
    LOCATOR_IMAGES = (By.CLASS_NAME, 'tensor_ru-About__block3-image')