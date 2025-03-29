from pages.administration.admin_product_page import ProductAdminPage
from pages.alerts import AlertPage
from pages.administration.login_admin_page import login_admin_ui, LoginAdminPage

from faker import Faker
import uuid

f = Faker()
uid = uuid.uuid4()
name = f"Apple " + uid.variant
title = uid.hex
model = uid.hex
keyword = uid.hex


class TestAdministration:

    def test_open_catalog_products(self, driver, login_admin_ui):
        product_admin_page = ProductAdminPage(driver)
        login_admin_ui
        product_admin_page.open_catalog_products()

        assert product_admin_page.checkout_products_page()

    def test_create_new_product(self, driver, login_admin_ui):
        """Добавление нового товара в разделе администратора"""
        product_admin_page = ProductAdminPage(driver)
        self.test_open_catalog_products(driver, login_admin_ui)
        product_admin_page.click_add_new_button()
        product_admin_page.fill_form_product_tab_general(name=name, title=title)
        product_admin_page.change_tab_in_form_product(tab_name="Data")
        product_admin_page.fill_form_product_tab_data(model=model)
        product_admin_page.change_tab_in_form_product(tab_name="SEO")
        product_admin_page.fill_form_product_tab_seo(keyword=keyword)
        product_admin_page.click_save_product_button()

        assert AlertPage(driver).success_alert()

    def test_delete_product(self, driver, login_admin_ui):
        """Удаление товара из списка в разделе администратора"""
        product_admin_page = ProductAdminPage(driver)
        self.test_open_catalog_products(driver, login_admin_ui)
        product_admin_page.delete_product()

        assert AlertPage(driver).success_alert()
