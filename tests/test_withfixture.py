import time
from selenium.webdriver.common.by import By
from utils.log import logger


class TestBaiDu(object):

    locator_kw = (By.ID, 'kw')
    locator_su = (By.ID, 'su')
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    def test_search_0(self, chrome_driver): # chrome_driver from /conftest.py
        chrome_driver.find_element(*self.locator_kw).send_keys(u'selenium 测试')
        chrome_driver.find_element(*self.locator_su).click()
        time.sleep(2)
        links = chrome_driver.find_elements(*self.locator_result)
        for link in links:
            logger.info(link.text)

    def test_search_1(self, chrome_driver):
        chrome_driver.find_element(*self.locator_kw).send_keys('Python selenium')
        chrome_driver.find_element(*self.locator_su).click()
        time.sleep(2)
        links = chrome_driver.find_elements(*self.locator_result)
        for link in links:
            logger.info(link.text)
