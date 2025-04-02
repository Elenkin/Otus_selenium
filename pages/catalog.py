from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class Catalog(BasePage):
    DESkTOPS_LIST_BUTTON = (By.XPATH, '//*[@class="nav navbar-nav"]//a[contains(@href, "catalog/desktops")]')
    LAPTOPS_LIST_BUTTON = (By.LINK_TEXT, "Laptops & Notebooks")
    COMPONENTS_LIST_BUTTON = (By.LINK_TEXT, "Components")
    CAMERAS_LIST_BUTTON = (By.LINK_TEXT, "Cameras")
    TABLETS_LIST_BUTTON = (By.LINK_TEXT, "Tablets")


    def check_element_list_desktops(self):
        """ наличие в каталоге ссылки на  desktops"""
        with allure.step(f"Проверяем наличие ссылки на список desktops в catalog"):
            self.driver.find_element(*self.DESkTOPS_LIST_BUTTON).click()
            return True
