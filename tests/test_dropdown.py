import pytest
from pages.main_page import MainPage
import allure
import locators


class TestDropDown:

    @allure.title('Проверка выпадабщего списка')
    @allure.description('По очереди раскрываем каждый элемент списка')
    @pytest.mark.parametrize('element_number', range(0, 8))
    def test_dropdown_list(self, element_number, driver):
        driver.get(locators.main_url)
        main = MainPage(driver)
        main.dropdown_expand_element(element_number)
        assert main.dropdown_element_get_state(element_number)