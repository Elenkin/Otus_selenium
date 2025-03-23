from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CardPage(BasePage):
    PATH = "/index.php?route=product/product&language=en-gb&product_id=43"
    PRICE = (By.CSS_SELECTOR, ".price-new")
    SPECIFICATION_TAB = (By.XPATH, '//a[@href="#tab-specification"]')
    REVIEW_TAB = (By.CSS_SELECTOR, "a[href='#tab-review']")
    WISHLIST_ADD_BUTTON = (By.XPATH, "//button[contains(@formaction, 'account/wishlist.add')]")
    CART_BUTTON = (By.ID, "button-cart")

    def open_page_product(self):
        """ Открываем страницу продукта указанную в PATH"""
        self.driver.get(self.driver.url + self.PATH)

    def check_element_price_of_page(self):
        """ Проверка наличия элемента PRICE на странице PATH"""
        element = self.driver.find_element(*self.PRICE)
        return element

    def find_element_specification_of_page(self):
        """ Проверка наличия элемента SPECIFICATION_TAB на странице PATH"""
        element = self.driver.find_element(*self.SPECIFICATION_TAB)
        return element

    def find_element_review_of_page(self):
        """ Проверка наличия элемента REVIEW_TAB на странице PATH"""
        element = self.driver.find_element(*self.REVIEW_TAB)
        return element

    def find_element_wishlist_add_button_of_page(self):
        """ Проверка наличия элемента WISHLIST_ADD_BUTTON на странице PATH"""
        element = self.driver.find_element(*self.WISHLIST_ADD_BUTTON)
        return element

    def find_element_cart_button_of_page(self):
        """ Проверка наличия элемента CART_BUTTON на странице PATH"""
        element = self.driver.find_element(*self.CART_BUTTON)
        return element
