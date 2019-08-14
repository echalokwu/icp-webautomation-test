import time
from Locators.Locators import Locators
from selenium.webdriver.support.ui import Select


class BasicDetailsPage:

    def __init__(self, driver):
        self.driver = driver
        self.click_application_type_dropdown_xpath = Locators.click_application_type_dropdown_xpath
        self.select_direct_payment_xpath = Locators.select_direct_payment_xpath
        self.wa_number_textbox_css = Locators.wa_number_textbox_css
        self.application_currency_xpath = Locators.application_currency_xpath
        self.select_application_currency_xpath = Locators.select_application_currency_xpath
        self.finance_dropdown_xpath = Locators.finance_dropdown_xpath
        self.select_finance_xpath = Locators.select_finance_xpath
        self.click_add_finance_xpath = Locators.click_add_finance_xpath
        self.amount_textbox_css = Locators.amount_textbox_css
        self.confirm_proceed_button_xpath = Locators.confirm_proceed_button_xpath

    def selectDirectPaymentAPPType(self):
        self.driver.find_element_by_xpath(Locators.click_application_type_dropdown_xpath).click()
        self.driver.find_element_by_xpath(Locators.select_direct_payment_xpath).click()

    def enterWANumber(self):
        wa = self.driver.find_element_by_css_selector(Locators.wa_number_textbox_css)
        wa.send_keys("test-" + repr(time.time()))

    def enterAppCurrency(self):
        currency = self.driver.find_element_by_xpath(Locators.application_currency_xpath)
        currency.send_keys("USD")
        self.driver.find_element_by_xpath(Locators.select_application_currency_xpath).click()

    def selectFinance(self):
        self.driver.find_element_by_xpath(Locators.finance_dropdown_xpath).click()
        self.driver.find_element_by_xpath(Locators.select_finance_xpath).click()
        self.driver.find_element_by_xpath(Locators.click_add_finance_xpath).click

    def enterAmount(self, amount):
        self.driver.find_element_by_css_selector(Locators.amount_textbox_css).send_keys(amount)

    def confirmAndProceed(self):
        self.driver.find_element_by_xpath(Locators.confirm_proceed_button_xpath).click()

