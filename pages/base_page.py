from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from conftest import *



class TimeoutException:
    pass

class  BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = driver.url
        self.wait = WebDriverWait(driver, timeout=5)

    def open_main_page(self):
        """ Открыть страницу заданную как URL """
        self.driver.get(self.driver.url)

    def scroll_to_element_and_click(self, button):
        """ Поиск элемента при маленьком разрешении экрана"""
        actions = ActionChains(self.driver)
        actions.move_to_element(button).click().perform()

    def wait_for_element(self, locator, timeout=20):
        """ Ожидает появления элемента на странице. """
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((locator))
            )
        except TimeoutException:
            print(f"Ошибка: элемент {locator} не был найден за {self.timeout} секунд.")
            return None

    def element_is_visible(self, locator, timeout=20):
        """ явное ожидание. Ожидаем 20 сек """
        wait = WebDriverWait(self.driver, 20)
        try:
            return wait.until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            raise AssertionError(f"Не дождался видимости элемента {locator}")
