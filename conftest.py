import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from utils.config import URL
from utils.config import FIREFOX_LINUX_DRIVER_PATH


@pytest.fixture()
def driver():
    return  webdriver.Chrome()


@pytest.fixture()
def chrome_driver(scope="function"):
    """
    scope="function" is the default one, which means each 
    test_* will have a fresh new instance of driver
    """
    driver = webdriver.Chrome()
    driver.get(URL)
    yield driver
    driver.close()

@pytest.fixture()
def firefox_driver(scope="function"):
    """
    scope="function" is the default one, which means each 
    test_* will have a fresh new instance of driver
    """
    cap = DesiredCapabilities().FIREFOX
    cap["marionette"] = False
    driver = webdriver.Firefox(capabilities=cap, executable_path=FIREFOX_LINUX_DRIVER_PATH)
    driver.get(URL)
    yield driver
    driver.close()

@pytest.fixture()
def some_global_resource(scope="session"):
    """
    whole test session will share this.
    """
    res = "something"
    return res


@pytest.fixture()
def some_module_resource(scope="module"):
    """
    all the tests in one module will share one same instance of this
    """
    res = "something"
    return res


@pytest.fixture()
def some_class_resource(scope="class"):
    """
    all the tests in one class will share one same instance of this
    """
    res = "something"
    return res