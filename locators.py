yandex_url = "https://dzen.ru/?yredirect=true"
main_url = 'https://qa-scooter.praktikum-services.ru/'
order_url = 'https://qa-scooter.praktikum-services.ru/order'

samokat_logo_xpath = "//a[contains(@class, 'Header_LogoScooter')]"
yandex_logo_xpath = "//a[contains(@class, 'Header_LogoYandex')]"
yandex_search_button_xpath = "//button[@type='submit']"

dropdown_list_class = 'accordion__heading'
order_button_header_xpath = ".//div[contains(@class, 'Header_Nav')]/button[contains(@class, 'Button_Button')]"
order_button_body_xpath = "//div[contains(@class, 'Home_FinishButton')]/button"
name_field_xpath = "//input[@placeholder='* Имя']"
surname_field_xpath = "//input[@placeholder='* Фамилия']"
address_field_xpath = "//input[@placeholder='* Адрес: куда привезти заказ']"
metro_field_xpath = "//input[@placeholder='* Станция метро']"
phone_field_xpath = "//input[@placeholder='* Телефон: на него позвонит курьер']"
next_button_xpath = "//div[contains(@class, 'Order_NextButton')]/button"
metro_dropdown_first_xpath = "//li[@data-value='1']"
date_field_xpath = "//input[@placeholder='* Когда привезти самокат']"
date_second_monday_xpath = "//div[@class='react-datepicker__week'][1]/div[1]"
length_field_xpath = "//div[text()='* Срок аренды']"
length_option_xpath = "//div[@class='Dropdown-option' and text()='сутки']"
color_checkbox_grey = "//label[@for='grey']"
message_field_xpath = "//input[@placeholder='Комментарий для курьера']"
order_button_xpath = "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать' and contains(@class, 'Button_Button')]"
order_confirm_button_xpath = "//button[text()='Да']"
order_created_window_xpath = "//div[contains(@class, 'Order_ModalHeader')]"


