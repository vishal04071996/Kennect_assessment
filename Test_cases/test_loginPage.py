import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

from base_page.LOGIN_PAGE1 import login_page
from utilities.read_properties import Read_Config


class Test_01:
    email = Read_Config.get_email()
    Password = Read_Config.get_Password()
    wrong_email = Read_Config.get_wrong_email()
    wrong_password = Read_Config.get_wrong_password()
    URL = Read_Config.get_URL()
    actual_text = Read_Config.get_actual_text()

    def test_login_Valid(self, setup):

        self.driver = setup
        self.driver.get(self.URL)

        self.LP = login_page(self.driver)
        self.LP.login_email(self.email)
        self.LP.login_password(self.Password)
        self.LP.login_click_login_button()

        if self.LP.login_homepage() == self.actual_text:
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

    def test_login_invalid(self, setup):

#login to Page
        self.driver = setup
        self.driver.get(self.URL)

        self.LP = login_page(self.driver)
        self.LP.login_username(self.wrong_username)
        self.LP.login_password(self.wrong_password)
        self.LP.login_click_login_button()
        self.driver.save_screenshot(".//screenshots//test_invigilation.png")
        print("comments:", self.LP.login_error_message())

    def test_Test_Cost_Calculator(self, setup):

        self.driver = setup
        self.driver.get(self.URL)

        self.LP = login_page(self.driver)
        self.LP.login_email(self.email)
        self.LP.login_password(self.Password)
        self.LP.login_click_login_button()

#scroll down to Page
        self.LP.execute_script("window.scrollBy(0,document.body.scrollHeight);")

        if self.LP.Test_cost_calculator.text == "Test Cost Calculator":
            print("Test Cost Calculator is Found")
        else:
            print("Not Found")

        self.LP.login_Test_patient_dropdown()
        self.LP.login_Select_test()
        self.LP.login_discount_dropdown()
        self.LP.login_select_discount()

#check test is add
        if self.LP.login_Subtotal() > 0:
            print("the subtotal amount is:", self.LP.login_Subtotal)
        else:
            print("blood test is not selected")

#check that test and discount is added
        if self.LP.login_Subtotal() == 900:
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

        if self.LP.login_Total() == 720:
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False


