import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UsingUnittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Opera(executable_path = './operadriver')

    def test_hidden_content(self):
        driver = self.driver
        driver.get("http://the-internet.herokuapp.com")
        excercise = driver.find_element_by_link_text("Dynamic Loading")
        excercise.click()

        hiddent_content_test = driver.find_element_by_link_text("Example 1: Element on page that is hidden")
        hiddent_content_test.click()

        start_btn = driver.find_element_by_tag_name("button")
        start_btn.click()
        

    def test_rendered_content(self):
        driver = self.driver

    def tearDown(self):
        print('Browser is about to close...')
        sleep(3)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()