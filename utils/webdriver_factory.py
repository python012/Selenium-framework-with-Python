"""
Return the webdriver object according to browser.vendor
"""

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from utils.configuration import BROWSER_VENDOR
from utils.configuration import BROWSER_DRIVER


def browser_driver():

    if BROWSER_VENDOR == "Firefox":
        cap = DesiredCapabilities().FIREFOX
        # cap["marionette"] = False
        return webdriver.Firefox(capabilities=cap, executable_path=BROWSER_DRIVER)

    elif BROWSER_VENDOR == "Chrome":
        cap = DesiredCapabilities().CHROME
        cap["marionette"] = False
        return webdriver.Chrome(executable_path=BROWSER_DRIVER)
    
    else:
        raise NameError("'BROWSER_VENDOR' is not defined correctly!")