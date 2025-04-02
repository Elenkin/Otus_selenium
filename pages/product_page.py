from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class ProductPage(BasePage):
    PATH = "/index.php?route=product/product&language=en-gb&product_id=43"
    PRICE = (By.CSS_SELECTOR, ".price-new")
    PRODUCT_BUTTON_CART = (By.ID, "button-cart")

    def open_page_product(self):
        """ Открываем страницу продукта указанную в PATH"""
        with allure.step(f"Открываем страницу продукта указанную в PATH"):
            self.driver.get(self.driver.url + self.PATH)

    def check_element_price_of_page(self):
        """ Проверка наличия элемента PRICE на странице PATH"""
        with allure.step(f"Проверяем наличие элемента PRICE на странице"):
            element = self.element_is_visible(self.PRICE)
            return element

    def click_button_cart(self):
        """ Нажать кнопку Добавить в корзину"""
        with allure.step(f"Нажимаем кнопку Добавить в корзину"):
            button_cart = self.element_is_visible(self.PRODUCT_BUTTON_CART)
            self.scroll_to_element_and_click(button_cart)
