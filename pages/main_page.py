import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    PATH = "/index.php?route=common/home"
    LOGO = (By.ID, "logo")
    PRODUCT_BUTTON_CART = (By.ID, "button-cart")
    CART = (By.XPATH, '//div[@class="nav float-end"]//a[contains(@href, "checkout/cart")]')
    PRODUCT_LINK = (By.XPATH, '//div[@class="content"]//a[contains(@href, "product/macbook")]')
    SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success")
    INPUT_SEARCH = (By.NAME, "search")
    LIST_CURRENCY = (By.ID, "form-currency")
    EURO_LINK = (By.LINK_TEXT, "€ Euro")
    USD_LINK = (By.LINK_TEXT, "$ US Dollar")
    GBP_LINK = (By.LINK_TEXT, "£ Pound Sterling")
    CURRENCY = (By.XPATH, "//*[@id='form-currency']//strong")

    def __init__(self, driver):
        self.driver = driver

    def click_product_link(self):
        """ Перейти на страницу товара по ссылке"""
        product_link = self.driver.find_element(*self.PRODUCT_LINK)
        self.scroll_to_element_and_click(product_link)

    def click_button_cart(self):
        """ Нажать кнопку Добавить в корзину"""
        button_cart = self.element_is_visible(self.PRODUCT_BUTTON_CART)
        self.scroll_to_element_and_click(button_cart)

    def open_dropdown_menu_currency(self):
        """ Открыть список валют"""
        button = self.element_is_visible(self.LIST_CURRENCY)
        self.scroll_to_element_and_click(button)

    def click_eur_currency(self):
        """ Выбрать валюту EUR"""
        button = self.element_is_visible(self.EURO_LINK)
        self.scroll_to_element_and_click(button)

    def click_usd_currency(self):
        """ Выбрать валюту USD"""
        button = self.element_is_visible(self.USD_LINK)
        self.scroll_to_element_and_click(button)

    def get_currency(self):
        """ Получить значение валюты на главной странице"""
        currency = self.driver.find_element(*self.CURRENCY)
        return currency

    def success_alert(self):
        """ наличие уведомления об успехе """
        self.driver.find_element(*self.SUCCESS_ALERT)
        return True

    def check_element_logo(self):
        """ наличие логотипа на странице """
        self.driver.find_element(*self.LOGO)
        return True

    def check_element_cart(self):
        """ наличие корзины в nav баре """
        self.driver.find_element(*self.CART)
        return True

    def check_element_product_link(self):
        """ наличие ссылки на карточку товара """
        self.driver.find_element(*self.PRODUCT_LINK)
        return True

    def check_element_input_search(self):
        """ наличие строки поиска на странице """
        self.driver.find_element(*self.INPUT_SEARCH)
        return True

    def check_element_currency(self):
        """ наличие кнопки смены валюты """
        self.driver.find_element(*self.LIST_CURRENCY)
        return True
