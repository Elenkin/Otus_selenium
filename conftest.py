import pytest

from selenium import webdriver
from selenium.webdriver.chromium.service import ChromiumService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FFOptions


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--headless", action="store_true")
    parser.addoption("--url", action="store", default="http://192.168.31.240:8081")

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

    if browser_name in ["chrome", "ch"]:
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)
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

    # yield driver
    #
    # driver.quit()
    request.addfinalizer(driver.close)
    #не явное ожидание элемента 2 секунды
    driver.implicitly_wait(2)
    # driver.get(url)
    driver.url = base_url

    return driver