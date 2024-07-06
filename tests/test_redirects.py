import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.common_page import CommonPage
import allure
import locators


class TestOrder:

    @allure.title('Проверяем переход на страницу заказа по кнопке "Заказать" с центра страницы')
    @allure.description('Отматываем заглавную страницу вниз чтобы появилась кнопка и проверяем переход по ней')
    def test_body_redirect_to_order(self, driver):
        driver.get(locators.main_url)
        page = CommonPage(driver)
        driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(*MainPage.dropdown_header_by_num_locator(0)))
        page.redirect(MainPage.order_button_body, OrderPage.name_field)
        assert driver.current_url == locators.order_url

    @allure.title('Проверка переходов на сайте')
    @allure.description('Проверяем несколько переходов внутри сайта и один на заглавную страницу яндекса')
    @pytest.mark.parametrize('start_url, end_url, button, wait_element', [
        [locators.main_url, locators.order_url, MainPage.order_button_header, OrderPage.name_field],
        [locators.order_url, locators.main_url, CommonPage.samokat_logo, MainPage.dropdown_header_by_num_locator(0)],
        [locators.order_url, locators.yandex_url, CommonPage.yandex_logo, CommonPage.yandex_search_button]
    ])
    def test_redirects(self, start_url, end_url, button, wait_element, driver):
        driver.get(start_url)
        page = CommonPage(driver)
        page.redirect(button, wait_element)
        assert driver.current_url == end_url
