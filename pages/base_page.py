from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import pytest
import uuid


class TimeoutException:
    pass

@pytest.fixture
def generate_random_data():
    uid = uuid.uuid4()
    name = f"Apple " + uid.variant
    title = uid.hex
    model = uid.hex
    keyword = uid.hex

    # Возвращаем сгенерированные данные в виде словаря
    return {
        "name": name,
        "title": title,
        "model": model,
        "keyword": keyword
    }

class  BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = driver.url
        self.wait = WebDriverWait(driver, timeout=5)

    def _text_xpath(self, text):
        return f"//*[text()='{text}']"

    def get_element(self, locator: tuple, timeout=3):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def get_elements(self, locator: tuple, timeout=3):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def click(self, locator: tuple):
        ActionChains(self.driver).move_to_element(self.get_element(locator)).pause(0.3).click().perform()

    def input_value(self, locator: tuple, text: str):
        self.get_element(locator).click()
        self.get_element(locator).clear()
        for l in text:
            self.get_element(locator).send_keys(l)

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
            raise AssertionError(f"Ошибка: элемент {locator} не был найден за {self.timeout} секунд.")

    def element_is_visible(self, locator, timeout=20):
        """ явное ожидание. Ожидаем 20 сек """
        wait = WebDriverWait(self.driver, 20)
        try:
            return wait.until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            raise AssertionError(f"Не дождался видимости элемента {locator}")
