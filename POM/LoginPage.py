from Locators.Locators import Locators
import time


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://uat.icp.ifad.org/"
        self.username_textbox_css = Locators.username_textbox_css
        self.password_textbox_css = Locators.password_textbox_css
        self.login_button_xpath = Locators.login_button_xpath

    def go(self):
        self.driver.get(self.url)

    def enter_username(self, username):
        self.driver.find_element_by_css_selector(Locators.username_textbox_css).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_css_selector(Locators.password_textbox_css).send_keys(password)

    def click_login_button(self):
        self.driver.find_element_by_xpath(Locators.login_button_xpath).click()

    def click_verify_token(self):
        self.driver.find_element_by_xpath(Locators.verify_button_xpath).click()

    def takeScreenshot(self, driver):
        """
        Takes screenshot of the current open web page
        :param driver
        :return:
        """
        fileName = str(round(time.time() * 1000)) + ".png"
        screenshotDirectory = "/Users/echalo/PycharmProjects/ICP Framwork/venv/screenshot"
        destinationFile = screenshotDirectory + fileName

        try:
            driver.save_screenshot(destinationFile)
            print("Screenshot saved to directory --> :: " + destinationFile)
        except NotADirectoryError:
            print("Not a directory issue")

