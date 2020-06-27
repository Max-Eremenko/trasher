import unittest
from selenium import webdriver


class AA(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='D:\qa\chromedrive\chromedriver')
        self.url = self.driver.get('https://www.seleniumeasy.com/test/basic-radiobutton-demo.html')

    def test_radio_button_male(self):
        click_on_male = self.driver.find_element_by_xpath('//input[@value="Male"][@name="optradio"]')
        click_on_male.click()

        click_on_button = self.driver.find_element_by_id('buttoncheck')
        click_on_button.click()

        show_message = self.driver.find_element_by_xpath('//p[@class="radiobutton"][contains(text(), "Male")]')
        assert show_message.is_displayed()

    def test_radio_button_female(self):
        click_on_female = self.driver.find_element_by_xpath('//label[text()="Female"]//input[@name="optradio"]')
        click_on_female.click()

        click_on_button = self.driver.find_element_by_id('buttoncheck')
        click_on_button.click()

        show_message = self.driver.find_element_by_xpath('//p[@class="radiobutton"][contains(text(), "Female")]')
        assert show_message.is_displayed()

    def test_group_male(self):
        click_on_male = self.driver.find_element_by_xpath('//input[@name="gender"][@value="Male"]')
        click_on_male.click()

        age_group = self.driver.find_elements_by_xpath('//input[@name="ageGroup"]')
        list = []
        for age in age_group:
            list.append(age)

        zero_to_five = list[0].click()
        five_to_fifteen = list[1].click()
        fifteen_to_fifty = list[2].click()

        click_on_button = self.driver.find_element_by_xpath('//button[@class="btn btn-default"][text()="Get values"]')
        click_on_button.click()

        show_message = self.driver.find_element_by_xpath('//p[@class="groupradiobutton"]')
        assert show_message.is_displayed()

    def test_group_female(self):
        click_on_female = self.driver.find_element_by_xpath('//input[@name="gender"][@value="Female"]')
        click_on_female.click()

        age_group = self.driver.find_elements_by_xpath('//input[@name="ageGroup"]')
        list = []
        for age in age_group:
            list.append(age)

        zero_to_five = list[0].click()
        five_to_fifteen = list[1].click()
        fifteen_to_fifty = list[2].click()

        click_on_button = self.driver.find_element_by_xpath('//button[@class="btn btn-default"][text()="Get values"]')
        click_on_button.click()

        show_message = self.driver.find_element_by_xpath('//p[@class="groupradiobutton"]')
        assert show_message.is_displayed()

    def tearDown(self):
        self.driver.close()

