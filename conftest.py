import pytest

from utils.webdriver_factory import browser_driver
from utils.configuration import URL


@pytest.fixture()
def driver_fixture(scope="function"):
    """
    scope="function" is the default one, which means each 
    test_* will have a fresh new instance of driver
    """
    driver = browser_driver()
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
