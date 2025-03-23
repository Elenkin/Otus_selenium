from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginAdminPage(BasePage):
    PATH = "/administration"
    USERNAME_INPUT = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    OPENCART_LINK = (By.XPATH, "//*[text()='OpenCart']")
    FORGOTTEN_PASSWORD = (By.LINK_TEXT, "Forgotten Password")
    LOGOUT_BUTTON = (By.ID, "nav-logout")
    PROFILE_BUTTON = (By.ID, "nav-profile")

    def __init__(self, driver):
        self.driver = driver

    def open_admin_page(self):
        """ Открываем страницу указанную в PATH"""
        self.driver.get(self.driver.url + self.PATH)

    def fill_form_login(self, username, password):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def click_logout_button(self):
        logout_button = self.wait_for_element(self.LOGOUT_BUTTON)
        if logout_button:
            logout_button.click()

    def user_profile_is_visible(self):
        self.wait_for_element(self.PROFILE_BUTTON)
        return True

    def login_button_is_visible(self):
        self.wait_for_element(self.SUBMIT_BUTTON)
        return True



