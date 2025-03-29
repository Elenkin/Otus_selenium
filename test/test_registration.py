import pytest
from conftest import *
from pages.registration_page import RegisterPage
from faker import Faker

f = Faker()
firstname = f.first_name()
lastname = f.last_name()
email = f.email()
password = f.password()


class TestsRegister:

    def test_registration_user(self, driver):
        """Регистрация нового пользователя в магазине opencart"""
        register_page = RegisterPage(driver)
        register_page.open_register_page()
        register_page.fill_form_register(firstname, lastname, email, password)
        register_page.click_policy_checkbox()
        register_page.click_register_button()

        assert register_page.link_is_present()