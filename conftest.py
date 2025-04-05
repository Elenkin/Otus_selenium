import logging
import pytest
import allure
import json
import mysql.connector
import os
import datetime

from selenium import webdriver
from selenium.webdriver.chromium.service import ChromiumService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FFOptions


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--url", action="store", default="http://192.168.31.240:8081")
    parser.addoption("--log_level", "-L", default="INFO")
    parser.addoption("--executor", action="store", default=None),

@pytest.fixture
def username():
    return "user"

@pytest.fixture
def password():
    return "bitnami"

@pytest.fixture()
def url(request):
    return request.config.getoption("--url")


@pytest.fixture()
def driver(request):
    browser_name = request.config.getoption("browser")
    headless = request.config.getoption("headless")  # True - False
    base_url = request.config.getoption("--url")
    log_level = request.config.getoption("--log_level")
    test_name = request.node.name
    logger = logging.getLogger(test_name)
    executor = request.config.getoption("--executor")

    # Создаём каталог log, проверяем существует ли папка (exist_ok=True)
    os.makedirs("log", exist_ok=True)
    #Создаём обработчик для записи журналов в файл. Файл будет называться по имени теста
    file_handler = logging.FileHandler(f"log/{test_name}.log", encoding='utf-8')
    #Задаём формат для журналов
    file_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
    logger.addHandler(file_handler)
    logger.setLevel(log_level)
    logger.info("===> Test '%s' started at %s" % (test_name, datetime.datetime.now()))


    if browser_name in ["chrome", "ch"]:
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        # Если указан executor, запускаем на удалённом сервере Selenium иначе запуск локально
        # (pytest --executor=192.168.31.240 --browser=chrome)
        if executor:
                caps = {
                    "browserName": browser_name,
                    #Можно добавить другие опции selenoid, если это необходимо
                    # "browserVersion": version,
                    # "selenoid:options": {
                    #     "enableVNC": vnc,
                    #     "name": request.node.name,
                    #     "screenResolution": "1280x2000",
                    #     "enableVideo": video,
                    #     "enableLog": logs,
                    #     "timeZone": "Europe/Moscow",
                    #     "env": ["LANG=ru_RU.UTF-8", "LANGUAGE=ru:en", "LC_ALL=ru_RU.UTF-8"]
                    # },
                    # "acceptInsecureCerts": True,
                }

                for k, v in caps.items():
                    options.set_capability(k, v)

                driver = webdriver.Remote(
                    command_executor=f"http://{executor}:4444/wd/hub",
                    options=options
                )
        else:
            driver = webdriver.Chrome(options=options)
            allure.attach(
                name=driver.session_id,
                body=json.dumps(driver.capabilities, indent=4, ensure_ascii=False),
                attachment_type=allure.attachment_type.JSON)


    elif browser_name in ["firefox", "ff"]:
        options = FFOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    elif browser_name in ["yandex", "ya"]:
        service = ChromiumService(
            executable_path="C:/Users/Администратор/PycharmProjects/drivers/yandexdriver.exe"
        )
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        options.binary_location = "C:/Users/Администратор/yandex-browser"
        driver = webdriver.Chrome(service=service, options=options)
    elif browser_name in ["safari", "sf"]:
        driver = webdriver.Safari()

    driver.maximize_window()

    request.addfinalizer(driver.close)
    # не явное ожидание элемента 2 секунды
    driver.implicitly_wait(2)
    driver.url = base_url
    driver.logger = logger
    driver.log_level = logging.DEBUG
    # yield driver

    return driver


@pytest.fixture(scope="session")
def db_connection(request):
    connection = mysql.connector.connect(
        user='bn_opencart',
        password='',
        host='127.0.0.1',
        database='bitnami_opencart',
        port='3306'
    )
    request.addfinalizer(connection.close)
    return connection