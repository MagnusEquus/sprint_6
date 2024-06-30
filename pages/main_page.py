from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


class MainPage:

    dropdown_list = [By.CLASS_NAME, 'accordion__heading']

    # def __init__(self, driver):
    #     self.driver = driver
    #
    # def dropdown_element_locator(self, n):
    #     return [By.id, f'accordion__heading-{n}']
    #
    # def is_dropdown_element_expanded_locator(self, n):
    #     dropdown_state = self.dropdown_element_locator(n).__getattribute__("aria-expanded")
    #     return dropdown_state == 'true'
    #
    # # def test_dropdown_click(self):
    # #     self.driver.get('https://qa-scooter.praktikum-services.ru/')
    # #     l = len(self.driver.find_elements(*self.dropdown_list))
    # #     for i in l:
    # #         self.driver.find_element(self.dropdown_locator(i)).click()
    # #         assert self.is_dropdown_element_expanded_locator(i)
    #
