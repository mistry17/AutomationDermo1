import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--browser",default = "chrome", action = "store",help = "run slow test"
    )

@pytest.fixture
def driver_initialize(request):
        browser = request.config.getoption("browser")
        if browser == "chrome":
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()
        driver.maximize_window()
        driver.implicitly_wait(15)
        driver.get("https://opensource-demo.orangehrmlive.com/")
        yield driver
        driver.close()