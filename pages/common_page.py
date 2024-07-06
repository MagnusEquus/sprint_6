from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure
import locators


class CommonPage:

    samokat_logo = [By.XPATH, locators.samokat_logo_xpath]
    yandex_logo = [By.XPATH, locators.yandex_logo_xpath]
    yandex_search_button = [By.XPATH, locators.yandex_search_button_xpath]

    def __init__(self, driver):
        self.driver = driver

    @allure.step('переходим на новую страницу по кнопке и ждем загрузки')
    def redirect(self, button, wait_element):
        self.driver.find_element(*button).click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(wait_element))