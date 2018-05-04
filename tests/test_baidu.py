import os
import sys
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestBaiDu(unittest.TestCase):
    # URL = Config().get('URL')
    URL = "http://www.baidu.com"

    locator_kw = (By.ID, 'kw')
    locator_su = (By.ID, 'su')
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    def setUp(self):
        base_path = None
        if os.name == 'nt':
            base_path = os.path.dirname(os.path.abspath(__file__)) + '\\..\\'
        else:
            base_path = os.path.dirname(os.path.abspath(__file__)) + '/'

        sys.path.append(base_path)
        # from utils.config_reader import ConfigReader
        # config = ConfigReader(base_path)
        #self.driver = webdriver.Chrome(executable_path=config.get_win_chrome_driver())
        self.driver = webdriver.Chrome() # need add the dirver path to PATH of the system
        self.driver.get(self.URL)

    def tearDown(self):
        self.driver.quit()

    def test_search_0(self):
        self.driver.find_element(*self.locator_kw).send_keys('selenium 测试')
        self.driver.find_element(*self.locator_su).click()
        time.sleep(2)
        links = self.driver.find_elements(*self.locator_result)
        for link in links:
            print(link.text)

    def test_search_1(self):
        self.driver.find_element(*self.locator_kw).send_keys('Python selenium')
        self.driver.find_element(*self.locator_su).click()
        time.sleep(2)
        links = self.driver.find_elements(*self.locator_result)
        for link in links:
            print(link.text)


if __name__ == '__main__':
    unittest.main()
