import unittest
from selenium import webdriver
import time
from POM.LoginPage import LoginPage
from POM.ProjectsPage import ClickProjectsPage
from POM.BasicDetailsPage import BasicDetailsPage
from utils import utils as utils


class TestDPWA(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/Users/echalo/PycharmProjects/ICP Framwork/Drivers/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        login = LoginPage(driver)
        login.go()
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login_button()
        login.takeScreenshot(driver)
        time.sleep(15)
        login.click_verify_token()
        time.sleep(5)

        homepage = ClickProjectsPage(driver)
        homepage.click_financial_dropdown_tabs()
        time.sleep(3)
        homepage.click_wa()
        time.sleep(5)
        homepage.click_big_actions_button()
        time.sleep(2)
        homepage.click_withdrawal_application()
        time.sleep(5)

        basicdetails = BasicDetailsPage(driver)
        basicdetails.selectDirectPaymentAPPType()
        time.sleep(2)
        basicdetails.enterWANumber()
        time.sleep(3)
        basicdetails.enterAppCurrency()
        time.sleep(3)
        basicdetails.selectFinance()
        basicdetails.enterAmount(utils.AMOUNT)
        basicdetails.confirmAndProceed()
        time.sleep(5)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

        print("Test Completed")


if __name__ == '__main__':
    unittest.main()
