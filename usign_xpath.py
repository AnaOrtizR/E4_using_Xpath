import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class using_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_buscar_por_xpath(self):
        driver = self.driver
        driver.get("https://promusic.cl")
        time.sleep(1)
        xpath =driver.find_element(By.XPATH, "//*[@id='shopify-section-sections--22889054667034__header']/header/div[4]/form/input")
        time.sleep(2)
        xpath.send_keys("batería", Keys.ARROW_DOWN)
        xpath.send_keys(Keys.RETURN)


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()