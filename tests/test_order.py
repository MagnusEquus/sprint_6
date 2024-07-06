import data
from pages.order_page import OrderPage
import allure
from conftest import driver
import locators

class TestOrder:

    @allure.title('Проверка создания заказа')
    @allure.description('Заполняем все поля у заказа и проверяем что он создался')
    def test_create_order(self, driver):
        driver.get(locators.order_url)
        order = OrderPage(driver)
        order.fill_order(
            data.NAME, data.SURNAME, data.ADDRESS, order.metro_dropdown_first, data.PHONE,
            order.date_second_monday, order.length_option, order.color_checkbox_grey, data.MESSAGE
        )
        assert order.check_if_order_is_created()
