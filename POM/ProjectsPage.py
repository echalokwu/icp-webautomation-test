from Locators.Locators import Locators
import time


class ClickProjectsPage:

    def __init__(self, driver):
        self.driver = driver
        self.click_financial_dropdwon_link_xpath = Locators.click_financial_dropdown_link_xpath
        self.click_projects_link_xpath = Locators.click_projects_link_xpath
        self.click_big_action_button_link_xpath = Locators.click_big_action_button_link_xpath
        self.click_wa_link_xpath = Locators.click_wa_link_xpath

    def click_financial_dropdown_tabs(self):
        self.driver.find_element_by_xpath(Locators.click_financial_dropdown_link_xpath).click()

    def projects_tabs(self):
        self.driver.find_element_by_xpath(Locators.click_projects_link_xpath).click()

    def click_big_actions_button(self):
        self.driver.find_element_by_xpath(Locators.click_big_action_button_link_xpath).click()

    def click_wa(self):
        self.driver.find_element_by_xpath(Locators.click_wa_link_xpath).click()

    def click_withdrawal_application(self):
        self.driver.find_element_by_xpath(Locators.click_withdrawal_application_xpath).click()

    def takeScreenshot(self, driver):
        """
        Takes screenshot of the current open web page
        :param driver
        :return:
        """
        fileName = str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "/Users/echalo/PycharmProjects/ICP Framwork/screenshots"
        destinationFile = screenshotDirectory + fileName

        try:
            driver.save_screenshot(destinationFile)
            print("Screenshot saved to directory --> :: " + destinationFile)
        except NotADirectoryError:
            print("Not a directory issue")
