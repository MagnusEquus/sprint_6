from pages.main_page import MainPage
from selenium import webdriver
from selenium.webdriver.common.by import By


# class TestDropDown:
#
#     driver = None
#
#     @classmethod
#     def setup_class(cls):
#         cls.driver = webdriver.Chrome()
#
#     def test_check_email_in_header(self):
#         self.driver.get('https://qa-scooter.praktikum-services.ru/')
#
#         Main = MainPage(self.driver)
#
#         l = len(Main.driver.find_elements(*Main.dropdown_list))
#         for i in l:
#             Main.driver.find_element(Main.dropdown_locator(i)).click()
#             assert Main.is_dropdown_element_expanded_locator(i)
#
#
#     @classmethod
#     def teardown_class(cls):
#         cls.driver.quit()