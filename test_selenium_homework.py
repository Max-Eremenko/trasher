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
        button_option_one = self.driver.find_element_by_xpath('//label[text()="Option 1"]')
        button_option_one.click()

        button_option_two = self.driver.find_element_by_xpath('//label[text()="Option 2"]')
        button_option_two.click()

        button_option_three = self.driver.find_element_by_xpath('//label[text()="Option 3"]')
        button_option_three.click()

        button_option_four = self.driver.find_element_by_xpath('//label[text()="Option 4"]')
        button_option_four.click()

        button_check_all = self.driver.find_element_by_id('check1')
        button_check_all.click()


