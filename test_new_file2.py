import unittest
from selenium import webdriver


class AA(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='D:\qa\chromedrive\chromedriver')
        self.url = self.driver.get('https://www.seleniumeasy.com/test/basic-radiobutton-demo.html')

    def test_group_male_zero_five(self):
        click_on_male = self.driver.find_element_by_xpath('//input[@value="Male"][@name="gender"]')
        click_on_male.click()

        click_on_age = self.driver.find_element_by_xpath('//input[@name="ageGroup"][@value="0 - 5"]')
        click_on_age.click()

        click_on_button = self.driver.find_element_by_xpath('//button[@class="btn btn-default"][text()="Get values"]')
        click_on_button.click()

        show_message = self.driver.find_element_by_xpath(
            '//p[@class="groupradiobutton"][text()="Sex : Male"][text()=" Age group: 0 - 5"]')
        assert show_message.is_displayed()

    def test_group_male_five_fifteen(self):
        click_on_male = self.driver.find_element_by_xpath('//input[@value="Male"][@name="gender"]')
        click_on_male.click()

        click_on_age = self.driver.find_element_by_xpath('//input[@name="ageGroup"][@value="5 - 15"]')
        click_on_age.click()

        click_on_button = self.driver.find_element_by_xpath('//button[@class="btn btn-default"][text()="Get values"]')
        click_on_button.click()

        show_message = self.driver.find_element_by_xpath(
            '//p[@class="groupradiobutton"][text()="Sex : Male"][text()=" Age group: 5 - 15"]')
        assert show_message.is_displayed()

    def test_group_male_fifteen_fifty(self):
        click_on_male = self.driver.find_element_by_xpath('//input[@value="Male"][@name="gender"]')
        click_on_male.click()

        click_on_age = self.driver.find_element_by_xpath('//input[@name="ageGroup"][@value="15 - 50"]')
        click_on_age.click()

        click_on_button = self.driver.find_element_by_xpath('//button[@class="btn btn-default"][text()="Get values"]')
        click_on_button.click()

        show_message = self.driver.find_element_by_xpath(
            '//p[@class="groupradiobutton"][text()="Sex : Male"][text()=" Age group: 15 - 50"]')
        assert show_message.is_displayed()

    def test_group_female_zero_five(self):
        click_on_male = self.driver.find_element_by_xpath('//input[@value="Female"][@name="gender"]')
        click_on_male.click()

        click_on_age = self.driver.find_element_by_xpath('//input[@name="ageGroup"][@value="0 - 5"]')
        click_on_age.click()

        click_on_button = self.driver.find_element_by_xpath('//button[@class="btn btn-default"][text()="Get values"]')
        click_on_button.click()

        show_message = self.driver.find_element_by_xpath(
            '//p[@class="groupradiobutton"][text()="Sex : Female"][text()=" Age group: 0 - 5"]')
        assert show_message.is_displayed()

    def test_group_female_five_fifteen(self):
        click_on_male = self.driver.find_element_by_xpath('//input[@value="Female"][@name="gender"]')
        click_on_male.click()

        click_on_age = self.driver.find_element_by_xpath('//input[@name="ageGroup"][@value="5 - 15"]')
        click_on_age.click()

        click_on_button = self.driver.find_element_by_xpath('//button[@class="btn btn-default"][text()="Get values"]')
        click_on_button.click()

        show_message = self.driver.find_element_by_xpath(
            '//p[@class="groupradiobutton"][text()="Sex : Female"][text()=" Age group: 5 - 15"]')
        assert show_message.is_displayed()

    def test_group_female_fifteen_fifty(self):
        click_on_male = self.driver.find_element_by_xpath('//input[@value="Female"][@name="gender"]')
        click_on_male.click()

        click_on_age = self.driver.find_element_by_xpath('//input[@name="ageGroup"][@value="15 - 50"]')
        click_on_age.click()

        click_on_button = self.driver.find_element_by_xpath('//button[@class="btn btn-default"][text()="Get values"]')
        click_on_button.click()

        show_message = self.driver.find_element_by_xpath(
            '//p[@class="groupradiobutton"][text()="Sex : Female"][text()=" Age group: 15 - 50"]')
        assert show_message.is_displayed()

    def tearDown(self):
        self.driver.close()


