import os
import sys
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


def setup_module(module):
    """ setup any state specific to the execution of the given module."""
    print("------ setup before module ------")

def teardown_module(module):
    """ teardown any state that was previously setup with a setup_module
    method.
    """
    print("------ setup after module ------")

class TestBaidu(object):

    def test_login(self):
        print("->>> test baidu login function.")
        assert True == True

class TestSohu(object):

    def test_login(self):
        print("->>> test sohu login function.")
        assert True == True
    
    def test_logout(self):
        print("->>> test sohu logout function.")


# class TestBaidu(object):
#     # URL = Config().get('URL')
#     URL = "http://www.baidu.com"

#     locator_kw = (By.ID, 'kw')
#     locator_su = (By.ID, 'su')
#     locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

#     def setUp(self):
#         self.driver = webdriver.Chrome() # need add the dirver path to PATH of the system
#         self.driver.get(self.URL)

#     def tearDown(self):
#         self.driver.quit()

#     def test_search_0(self):
#         self.driver.find_element(*self.locator_kw).send_keys('selenium 测试')
#         self.driver.find_element(*self.locator_su).click()
#         time.sleep(2)
#         links = self.driver.find_elements(*self.locator_result)
#         for link in links:
#             print(link.text)

#     def test_search_1(self):
#         self.driver.find_element(*self.locator_kw).send_keys('Python selenium')
#         self.driver.find_element(*self.locator_su).click()
#         time.sleep(2)
#         links = self.driver.find_elements(*self.locator_result)
#         for link in links:
#             print(link.text)

