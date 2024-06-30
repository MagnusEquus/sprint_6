import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.common_page import CommonPage
from selenium import webdriver
import allure


class TestOrder:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Проверяем переход на страницу заказа по кнопке "Заказать" с центра страницы')
    @allure.description('Отматываем заглавную страницу вниз чтобы появилась кнопка и проверяем переход по ней')
    def test_body_redirect_to_order(self):
        self.driver.get(MainPage.url)
        page = CommonPage(self.driver)
        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*MainPage.dropdown_header_by_num_locator(0)))
        page.redirect(MainPage.order_button_body, OrderPage.name_field)
        assert self.driver.current_url == OrderPage.url

    @allure.title('Проверка переходов на сайте')
    @allure.description('Проверяем несколько переходов внутри сайта и один на заглавную страницу яндекса')
    @pytest.mark.parametrize('start_url, end_url, button, wait_element', [
        [MainPage.url, OrderPage.url, MainPage.order_button_header, OrderPage.name_field],
        [OrderPage.url, MainPage.url, CommonPage.samokat_logo, MainPage.dropdown_header_by_num_locator(0)],
        [OrderPage.url, CommonPage.yandex_url, CommonPage.yandex_logo, CommonPage.yandex_search_button]
    ])
    def test_redirects(self, start_url, end_url, button, wait_element):
        self.driver.get(start_url)
        page = CommonPage(self.driver)
        page.redirect(button, wait_element)
        assert self.driver.current_url == end_url

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
