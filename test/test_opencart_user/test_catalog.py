from conftest import *
from pages.catalog import Catalog
import allure


class TestsCatalog:

    @allure.title("Наличие в каталоге ссылки на desktops")
    def test_check_element_list_desktops(self, driver):
        catalog = Catalog(driver)
        catalog.open_main_page()
        catalog.check_element_list_desktops()

        assert catalog.check_element_list_desktops()
