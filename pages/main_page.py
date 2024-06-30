from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure


class MainPage:

    url = 'https://qa-scooter.praktikum-services.ru/'

    dropdown_list = [By.CLASS_NAME, 'accordion__heading']
    order_button_header = [By.XPATH, ".//button[@class='Button_Button__ra12g' and text()='Заказать']"]
    order_button_body = [By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']"]

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    @allure.step('Находим элемент заголовка строчки выпадающего списка по его номеру')
    def dropdown_header_by_num_locator(n):
        return [By.XPATH, f"//div[@id='accordion__heading-{n}']"]

    @staticmethod
    @allure.step('Получаем элемент тела строчки выпадающего списка по его номеру')
    def dropdown_body_by_num_locator(n):
        return [By.ID, f"accordion__panel-{n}"]

    @allure.step('Узнаем раскрыт ли элемент списка')
    def dropdown_element_get_state(self, n):
        element = self.driver.find_element(*self.dropdown_header_by_num_locator(n))
        dropdown_state = element.get_attribute("aria-expanded")
        return dropdown_state == 'true'

    @allure.step('Раскрываем элемент списка')
    def dropdown_expand_element(self, element_number):
        list_element = self.driver.find_element(*self.dropdown_header_by_num_locator(element_number))
        self.driver.execute_script("arguments[0].scrollIntoView();", list_element)
        WebDriverWait(self.driver, 2).until(
            expected_conditions.visibility_of_element_located(self.dropdown_header_by_num_locator(element_number)))
        list_element.click()
        WebDriverWait(self.driver, 2).until(
            expected_conditions.visibility_of_element_located(self.dropdown_body_by_num_locator(element_number)))
