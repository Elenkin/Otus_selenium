from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Catalog(BasePage):
    DESkTOPS_LIST_BUTTON = (By.XPATH, '//*[@class="nav navbar-nav"]//a[contains(@href, "catalog/desktops")]')
    LAPTOPS_LIST_BUTTON = (By.LINK_TEXT, "Laptops & Notebooks")
    COMPONENTS_LIST_BUTTON = (By.LINK_TEXT, "Components")
    CAMERAS_LIST_BUTTON = (By.LINK_TEXT, "Cameras")
    TABLETS_LIST_BUTTON = (By.LINK_TEXT, "Tablets")

    def __init__(self, driver):
        self.driver = driver

    def check_element_list_desktops(self):
        """ наличие в каталоге ссылки на  desktops"""
        self.driver.find_element(*self.DESkTOPS_LIST_BUTTON).click()
        return True

    def check_element_list_laptops(self):
        """ наличие в каталоге ссылки на  Laptops & Notebooks"""
        self.driver.find_element(*self.LAPTOPS_LIST_BUTTON)
        return True

    def check_element_list_components(self):
        """ наличие в каталоге ссылки на  components"""
        self.driver.find_element(*self.COMPONENTS_LIST_BUTTON)
        return True

    def check_element_list_cameras(self):
        """ наличие в каталоге ссылки на  список cameras"""
        self.driver.find_element(*self.CAMERAS_LIST_BUTTON)
        return True

    def check_element_list_tablets(self):
        """ наличие в каталоге ссылки на  список tablets"""
        self.driver.find_element(*self.TABLETS_LIST_BUTTON)
        return True
