import unittest
from selenium import webdriver


class A(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='D:\qa\chromedrive\chromedriver')
        self.url = self.driver.get('https://www.seleniumeasy.com/test/basic-checkbox-demo.html')

    def test_single_checkbox(self):
        button_checkbox = self.driver.find_element_by_id('isAgeSelected')
        button_checkbox.click()

    def test_multiply_checkbox(self):
        button_option_one = self.driver.find_element_by_xpath('//button[contains(text(), "Option 1")]')
        button_option_one.click()

        button_check_all = self.driver.find_element_by_id('check1')
        button_check_all.click()


