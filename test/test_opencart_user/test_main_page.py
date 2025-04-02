from conftest import *
from helpers import create_random_user
from pages.main_page import MainPage
from pages.user_page import UserPage
import allure


class TestsMain:

    @allure.title("Авторизация созданным юзером на странице /en-gb?route=account/login")
    def test_login_user(self, driver, db_connection):
        user_page = UserPage(driver)
        user_page.open_user_page()
        user_page.login(*create_random_user(db_connection))
        user_page.wait_logged_in()

    @allure.title("Проверка элемента LOGO на странице /en-gb?route=account/login")
    def test_check_element_logo_from_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        assert main_page.check_element_logo()
