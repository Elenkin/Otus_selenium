import time

from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    PATH = "/index.php?route=common/home"
    LOGO = (By.ID, "logo")
    INPUT_SEARCH = (By.NAME, "search")
    LIST_CURRENCY = (By.ID, "form-currency")
    EURO_LINK = (By.LINK_TEXT, "€ Euro")
    USD_LINK = (By.LINK_TEXT, "$ US Dollar")
    GBP_LINK = (By.LINK_TEXT, "£ Pound Sterling")
    CURRENCY = (By.XPATH, "//*[@id='form-currency']//strong")


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
        currency = self.wait_for_element(self.CURRENCY)
        return currency

    def check_element_logo(self):
        """ наличие логотипа на странице """
        self.driver.find_element(*self.LOGO)
        return True

    def check_element_currency(self):
        """ наличие кнопки смены валюты """
        self.driver.find_element(*self.LIST_CURRENCY)
        return True
