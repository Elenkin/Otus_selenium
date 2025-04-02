from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class AlertPage(BasePage):
    SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success")


    def success_alert(self):
        """ наличие уведомления об успехе """
        with allure.step(f"Проверяем наличие уведомления об успехе"):
            self.driver.find_element(*self.SUCCESS_ALERT)
            return True