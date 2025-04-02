from pages.administration.admin_product_page import ProductAdminPage
from pages.alerts import AlertPage
from pages.administration.login_admin_page import login_admin_ui
from pages.base_page import generate_random_data

import pytest
import allure

@pytest.fixture
def product_admin_page(driver):
    product_admin_page = ProductAdminPage(driver)
    return product_admin_page


class TestAdministration:

    @allure.title("Открытие каталога продуктов")
    def test_open_catalog_products(self, driver, login_admin_ui, product_admin_page):
        login_admin_ui
        product_admin_page.open_catalog_products()

        assert product_admin_page.checkout_products_page()

    @allure.title("Добавление нового продукта в разделе администратора")
    def test_create_new_product(self, driver, login_admin_ui, product_admin_page, generate_random_data):

        # Извлекаем данные из фикстуры
        name = generate_random_data["name"]
        title = generate_random_data["title"]
        model = generate_random_data["model"]
        keyword = generate_random_data["keyword"]

        self.test_open_catalog_products(driver, login_admin_ui, product_admin_page)
        product_admin_page.click_add_new_button()
        product_admin_page.fill_form_product_tab_general(name=name, title=title)
        product_admin_page.change_tab_in_form_product(tab_name="Data")
        product_admin_page.fill_form_product_tab_data(model=model)
        product_admin_page.change_tab_in_form_product(tab_name="SEO")
        product_admin_page.fill_form_product_tab_seo(keyword=keyword)
        product_admin_page.click_save_product_button()

        assert AlertPage(driver).success_alert()

    @allure.title("Удаление продукта в разделе администратора")
    def test_delete_product(self, driver, login_admin_ui, product_admin_page):
        """Удаление товара из списка в разделе администратора"""
        self.test_open_catalog_products(driver, login_admin_ui, product_admin_page)
        product_admin_page.delete_product()

        assert AlertPage(driver).success_alert()
