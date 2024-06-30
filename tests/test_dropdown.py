import pytest
from pages.main_page import MainPage
from selenium import webdriver
import allure


class TestDropDown:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка выпадабщего списка')
    @allure.description('По очереди раскрываем каждый элемент списка')
    @pytest.mark.parametrize('element_number', range(0, 8))
    def test_dropdown_list(self, element_number):
        self.driver.get(MainPage.url)
        main = MainPage(self.driver)
        main.dropdown_expand_element(element_number)
        assert main.dropdown_element_get_state(element_number)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
