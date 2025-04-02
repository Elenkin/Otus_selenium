from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class ProductAdminPage(BasePage):
    PATH = "/administration"
    # навигация в каталог продукции
    PRODUCTS_LIST = (By.ID, "product")
    CATALOG_MENU_LINK = (By.LINK_TEXT, "Catalog")
    CATALOG_PRODUCTS_MENU_LINK = (By.LINK_TEXT, "Products")
    # поля формы создания продукта
    FORM_PRODUCT = (By.ID, "form-product")
    PRODUCT_NAME_INPUT = (By.ID, "input-name-1")
    META_TAG_TITLE_INPUT = (By.ID, "input-meta-title-1")
    META_TAG_DESCRIPTION_TEXTAREA = (By.ID, "input-meta-description-1")
    META_TAG_KEYWORDS_TEXTAREA = (By.ID, "input-meta-keyword-1")
    PRODUCT_TAGS_INPUT = (By.ID, "input-tag-1")
    MODEL_INPUT = (By.ID, "input-model")
    KEYWORD_INPUT = (By.ID, "input-keyword-0-1")
    SAVE_PRODUCT_BUTTON = (By.CSS_SELECTOR, "button[title='Save']")
    # кнопки управления продуктами создание/удаление
    ADD_NEW_BUTTON = (By.CSS_SELECTOR, "a[title='Add New']")
    DELETE = (By.CLASS_NAME, "btn-danger")
    CHECKBOX = (By.CSS_SELECTOR, '[type="checkbox"]')

    def open_admin_page(self):
        """ Открываем страницу указанную в PATH"""
        self.driver.get(self.driver.url + self.PATH)

    def open_catalog_products(self):
        with allure.step(f"Открываем каталог продуктов"):
            self.driver.find_element(*self.CATALOG_MENU_LINK).click()
            self.driver.find_element(*self.CATALOG_PRODUCTS_MENU_LINK).click()

    def checkout_products_page(self):
        return self.wait_for_element(self.PRODUCTS_LIST)

    def click_add_new_button(self):
        with allure.step(f"Нажимаем кнопку Добавить продукт"):
            self.driver.find_element(*self.ADD_NEW_BUTTON).click()
            self.wait_for_element(self.FORM_PRODUCT)

    def fill_form_product_tab_general(self, name, title, description=None,
                                      keyword=None, tags=None):
        with allure.step(f"Заполняем форму создания продукта раздел GENERAL"):
            self.driver.find_element(*self.PRODUCT_NAME_INPUT).send_keys(name)
            self.driver.find_element(*self.META_TAG_TITLE_INPUT).send_keys(title)
            self.driver.find_element(*self.META_TAG_TITLE_INPUT).send_keys(title)
            if description:
                self.driver.find_element(*self.META_TAG_DESCRIPTION_TEXTAREA).send_keys(description)
            if keyword:
                self.driver.find_element(*self.META_TAG_KEYWORDS_TEXTAREA).send_keys(keyword)
            if tags:
                self.driver.find_element(*self.PRODUCT_TAGS_INPUT).send_keys(tags)

    def fill_form_product_tab_data(self, model):
        with allure.step(f"Заполняем форму создания продукта раздел DATA"):
            self.driver.find_element(*self.MODEL_INPUT).send_keys(model)

    def fill_form_product_tab_seo(self, keyword):
        with allure.step(f"Заполняем форму создания продукта раздел SEO"):
            self.driver.find_element(*self.KEYWORD_INPUT).send_keys(keyword)

    def click_save_product_button(self):
        with allure.step(f"Нажимаем кнопку Сохранить продукт"):
            self.driver.find_element(*self.SAVE_PRODUCT_BUTTON).click()
            self.wait_for_element(self.FORM_PRODUCT)

    def get_tab_locator(self, tab_name):
        """Метод для генерации локатора с переменной"""
        return (By.LINK_TEXT, f"{tab_name}")

    def change_tab_in_form_product(self, tab_name):
        with allure.step(f"Переключаем TAB на {tab_name} в форме создания продукта"):
            # Генерируем локатор, передав переменную tab_name
            tab_locator = self.get_tab_locator(tab_name)
            # Находим элемент с этим локатором и кликаем по нему
            self.driver.find_element(*tab_locator).click()

    def delete_product(self):
        with allure.step(f"Включаем checkbox у первого продукта в списке и нажимаем кнопку Удалить"):
            self.driver.find_elements(*self.CHECKBOX)[1].click()
            self.driver.find_element(*self.DELETE).click()
            alert = self.driver.switch_to.alert
            alert.accept()
