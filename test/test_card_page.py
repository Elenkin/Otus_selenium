from conftest import *
from pages.card_page import CardPage


class TestsCardProduct:

    def test_check_element_price(self, driver):
        card_pages = CardPage(driver)
        card_pages.open_page_product()

        assert card_pages.check_element_price_of_page()

    def test_check_element_specification(self, driver):
        card_pages = CardPage(driver)
        card_pages.open_page_product()

        assert card_pages.find_element_specification_of_page()

    def test_check_element_review(self, driver):
        card_pages = CardPage(driver)
        card_pages.open_page_product()

        assert card_pages.find_element_review_of_page()

    def test_check_element_wishlist_add(self, driver):
        card_pages = CardPage(driver)
        card_pages.open_page_product()

        assert card_pages.find_element_wishlist_add_button_of_page()

    def test_check_element_cart_button(self, driver):
        card_pages = CardPage(driver)
        card_pages.open_page_product()

        assert card_pages.find_element_cart_button_of_page()