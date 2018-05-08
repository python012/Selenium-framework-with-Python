import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.log import logger
from utils.config import get_url


class TestBaiDu(object):
    URL = get_url()

    locator_kw = (By.ID, 'kw')
    locator_su = (By.ID, 'su')
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        # self.driver = webdriver.Firefox()
        self.driver.get(self.URL)

    def teardown_method(self, method):
        self.driver.quit()

    def test_search_0(self):
        self.driver.find_element(*self.locator_kw).send_keys(u'selenium 测试')
        self.driver.find_element(*self.locator_su).click()
        time.sleep(2)
        links = self.driver.find_elements(*self.locator_result)
        for link in links:
            logger.info(link.text)

    def test_search_1(self):
        self.driver.find_element(*self.locator_kw).send_keys('Python selenium')
        self.driver.find_element(*self.locator_su).click()
        time.sleep(2)
        links = self.driver.find_elements(*self.locator_result)
        for link in links:
            logger.info(link.text)

