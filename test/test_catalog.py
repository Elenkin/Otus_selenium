from conftest import *
from pages.catalog import Catalog


class TestsCatalog:

    def test_check_element_list_desktops(self, driver):
        catalog = Catalog(driver)
        catalog.open_main_page()
        catalog.check_element_list_desktops()

        assert catalog.check_element_list_desktops()

    def test_check_element_list_laptops(self, driver):
        catalog = Catalog(driver)
        catalog.open_main_page()

        assert catalog.check_element_list_laptops()

    def test_check_element_list_components(self, driver):
        catalog = Catalog(driver)
        catalog.open_main_page()

        assert catalog.check_element_list_components()

    def test_check_element_list_tablets(self, driver):
        catalog = Catalog(driver)
        catalog.open_main_page()

        assert catalog.check_element_list_tablets()

    def test_check_element_list_cameras(self, driver):
        catalog = Catalog(driver)
        catalog.open_main_page()

        assert catalog.check_element_list_cameras()
