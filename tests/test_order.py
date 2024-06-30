import data
from pages.order_page import OrderPage
from selenium import webdriver
import allure


class TestOrder:

    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка создания заказа')
    @allure.description('Заполняем все поля у заказа и проверяем что он создался')
    def test_create_order(self):
        self.driver.get(OrderPage.url)
        order = OrderPage(self.driver)
        order.fill_order(
            data.name, data.surname, data.address, order.metro_dropdown_first, data.phone,
            order.date_second_monday, order.length_option, order.color_checkbox_grey, data.message
        )
        assert order.check_if_order_is_created()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
