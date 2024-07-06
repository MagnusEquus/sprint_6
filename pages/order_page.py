from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure
import locators


class OrderPage:

    name_field = [By.XPATH, locators.name_field_xpath]
    surname_field = [By.XPATH, locators.surname_field_xpath]
    address_field = [By.XPATH, locators.address_field_xpath]
    metro_field = [By.XPATH, locators.metro_field_xpath]
    phone_field = [By.XPATH, locators.phone_field_xpath]
    next_button = [By.XPATH, locators.next_button_xpath]
    metro_dropdown_first = [By.XPATH, locators.metro_dropdown_first_xpath]
    date_field = [By.XPATH, locators.date_field_xpath]
    date_second_monday = [By.XPATH, locators.date_second_monday_xpath]
    length_field = [By.XPATH, locators.length_field_xpath]
    length_option = [By.XPATH, locators.length_option_xpath]
    color_checkbox_grey = [By.XPATH, locators.color_checkbox_grey]
    message_field = [By.XPATH, locators.message_field_xpath]
    order_button = [By.XPATH, locators.order_button_xpath]
    order_confirm_button = [By.XPATH, locators.order_confirm_button_xpath]
    order_created_window = [By.XPATH, locators.order_created_window_xpath]

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Вводим имя')
    def input_name(self, name):
        self.driver.find_element(*self.name_field).send_keys(name)

    @allure.step('Вводим фамилию')
    def input_surname(self, surname):
        self.driver.find_element(*self.surname_field).send_keys(surname)

    @allure.step('Вводим адрес')
    def input_address(self, address):
        self.driver.find_element(*self.address_field).send_keys(address)

    @allure.step('Вводим станцию метро')
    def input_metro(self, station_locator):
        self.driver.find_element(*self.metro_field).click()
        self.driver.find_element(*station_locator).click()

    @allure.step('Вводим номер телефона')
    def input_phone(self, phone):
        self.driver.find_element(*self.phone_field).send_keys(phone)

    @allure.step('Вводим дату')
    def input_date(self, date):
        self.driver.find_element(*self.date_field).click()
        self.driver.find_element(*date).click()

    @allure.step('Вводим срок')
    def input_length(self, input_option):
        self.driver.find_element(*self.length_field).click()
        self.driver.find_element(*input_option).click()

    @allure.step('Вводим цвет')
    def input_color(self, color_element):
        self.driver.find_element(*color_element).click()

    @allure.step('Вводим сообщение')
    def input_message(self, message):
        self.driver.find_element(*self.message_field).send_keys(message)

    @allure.step('Создаем заказ')
    def fill_order(self, name, surname, address, metro, phone, date, length_elem, color_elem, message):
        self.input_name(name)
        self.input_surname(surname)
        self.input_address(address)
        self.input_metro(metro)
        self.input_phone(phone)
        self.driver.find_element(*self.next_button).click()
        WebDriverWait(self.driver, 2).until(
            expected_conditions.visibility_of_element_located(self.date_field))
        self.input_date(date)
        self.input_length(length_elem)
        self.input_color(color_elem)
        self.input_message(message)
        self.driver.find_element(*self.order_button).click()
        WebDriverWait(self.driver, 2).until(
            expected_conditions.visibility_of_element_located(self.order_confirm_button))
        self.driver.find_element(*self.order_confirm_button).click()
        WebDriverWait(self.driver, 2).until(
            expected_conditions.visibility_of_element_located(self.order_created_window))

    @allure.step('Проверяем что заказ создался')
    def check_if_order_is_created(self):
        return self.driver.find_element(*self.order_created_window).is_displayed()
