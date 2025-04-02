from conftest import *
from pages.alerts import AlertPage
from pages.product_page import ProductPage
import allure


class TestsCardProduct:

    @allure.title("Проверка элемента PRICE на странице ProductPage")
    def test_check_element_price(self, driver):
        product_page = ProductPage(driver)
        product_page.open_page_product()

        assert product_page.check_element_price_of_page()

    @allure.title("Проверка кнопки 'Добавить в корзину' на странице ProductPage")
    def test_add_product_to_cart(self, driver):
        product_page = ProductPage(driver)
        product_page.open_page_product()
        product_page.click_button_cart()

        assert AlertPage(driver).success_alert()
