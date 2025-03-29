from conftest import *
from pages.main_page import MainPage


class TestCurrency:

    def test_change_currency_to_eur(self, driver):
        """Переключение валют из верхнего меню opencart"""
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.open_dropdown_menu_currency()
        main_page.click_eur_currency()
        currency = main_page.get_currency()

        assert currency.text == "€"
        print(f"получили значение элемента {currency.text}, ожидаем: == '€'")

    def test_change_currency_to_usd(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.open_dropdown_menu_currency()
        main_page.click_usd_currency()
        currency = main_page.get_currency()

        assert currency.text == "$"
        print(f"получили значение элемента {currency.text}, ожидаем: == '$'")