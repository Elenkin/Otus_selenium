from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class RegisterPage(BasePage):
    PATH = "/index.php?route=account/register"
    FIRSTNAME_INPUT = (By.ID, "input-firstname")
    LASTNAME_INPUT = (By.ID, "input-lastname")
    EMAIL_INPUT = (By.ID, "input-email")
    PASSWORD_INPUT = (By.ID, "input-password")
    POLICY_CHECKBOX = (By.NAME, "agree")
    REGISTER_FORM_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    LINK = (By.XPATH, "//a[contains(@href, 'account/success')]")

    def __init__(self, driver):
        self.driver = driver

    def open_register_page(self):
        """ Открываем страницу указанную в PATH"""
        self.driver.get(self.driver.url + self.PATH)

    def fill_form_register(self, firstname, lastname, email, password):
        self.driver.find_element(*self.FIRSTNAME_INPUT).send_keys(firstname)
        self.driver.find_element(*self.LASTNAME_INPUT).send_keys(lastname)
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_policy_checkbox(self):
        button = self.driver.find_element(*self.POLICY_CHECKBOX)
        actions = ActionChains(self.driver)
        actions.move_to_element(button).click().perform()

    def click_register_button(self):
        button = self.driver.find_element(*self.REGISTER_FORM_SUBMIT_BUTTON)
        # Создаем объект ActionChains
        actions = ActionChains(self.driver)
        actions.move_to_element(button).click().perform()

    def link_is_present(self):
        self.driver.find_element(*self.LINK)
        return True
