from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure


class CommonPage:

    samokat_logo = [By.CLASS_NAME, "Header_LogoScooter__3lsAR"]
    yandex_logo = [By.CLASS_NAME, "Header_LogoYandex__3TSOI"]
    yandex_url = "https://dzen.ru/?yredirect=true"
    yandex_search_button = [By.XPATH, "//div[@class='p55ff40a6']"]

    def __init__(self, driver):
        self.driver = driver

    @allure.step('переходим на новую страницу по кнопке и ждем загрузки')
    def redirect(self, button, wait_element):
        self.driver.find_element(*button).click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(wait_element))