from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class UserPage(BasePage):
    PATH = "/en-gb?route=account/login"
    LOGIN_INPUT = By.CSS_SELECTOR, "#input-email"
    PASSWORD_INPUT = By.CSS_SELECTOR, "#input-password"
    SUBMIT_LOGIN_BUTTON = By.CSS_SELECTOR, "#form-login button"
    LOGOUT_LINK = By.LINK_TEXT, "Logout"


    def open_user_page(self):
        """ Открываем страницу указанную в PATH"""
        with allure.step(f"Открываем страницу указанную в PATH"):
            self.driver.get(self.driver.url + self.PATH)

    def login(self, username, password):
        with allure.step(f"Заполняем форму авторизации"):
            self.input_value(self.LOGIN_INPUT, username)
            self.input_value(self.PASSWORD_INPUT, password)
            self.click(self.SUBMIT_LOGIN_BUTTON)
            return self

    def wait_logged_in(self):
        with allure.step(f"Проверяем наличие кнопки Logout на странице"):
            self.get_element(self.LOGOUT_LINK)
            return self
