from conftest import *
from pages.main_page import MainPage


class TestsMain:

    def test_add_product_to_cart(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_product_link()
        main_page.click_button_cart()

        assert main_page.success_alert()

    def test_check_element_logo_from_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        assert main_page.check_element_logo()

    def test_check_element_cart_from_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        assert main_page.check_element_cart()

    def test_check_element_product_link_from_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        assert main_page.check_element_product_link()

    def test_check_element_input_search(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        assert main_page.check_element_input_search()

    def test_check_element_element_currency(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        assert main_page.check_element_currency()
