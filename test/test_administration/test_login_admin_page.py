import pytest
from conftest import *
from pages import *


class TestsAdminPage:

    def test_success_login(self, driver, username, password):
        admin_page = LoginAdminPage(driver)
        admin_page.open_admin_page()
        admin_page.fill_form_login(username, password)
        admin_page.click_login_button()

        assert admin_page.user_profile_is_visible()

    def test_success_logout(self, driver, username, password):
        admin_page = LoginAdminPage(driver)
        self.test_success_login(driver, username, password)
        admin_page.click_logout_button()

        assert admin_page.login_button_is_visible()
