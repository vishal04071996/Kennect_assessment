import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from Base_Page.AddPatient_page import Patient_form
from Base_Page.Login_page import login_page
from utilities.read_properties import Read_Config

Actual_todo_list = []


class Test_02:
    email = Read_Config.get_email()
    Password = Read_Config.get_Password()
    URL = Read_Config.get_URL()
    Patients_name = Read_Config.get_Patients_name()
    Patients_email = Read_Config.get_Patients_email()
    Patients_phone = Read_Config.get_Patients_phone()
    Height = Read_Config.get_Height()
    weight = Read_Config.get_weight()
    gender = Read_Config.get_gender()
    age = Read_Config.get_age()
    systolic = Read_Config.get_systolic()
    diastolic = Read_Config.get_diastolic()

    URL2 = Read_Config.get_URL2()
    actual_text = Read_Config.get_actual_text()

    def test_AddPatients(self, setup):

        self.driver = setup
        self.driver.get(self.URL)

#login to Page
        self.LP = login_page(self.driver)
        self.LP.login_email(self.email)
        self.LP.login_password(self.Password)
        self.LP.login_click_login_button()

#Add Patient details
        self.driver.get(self.URL2)
        self.PA = Patient_form(self.driver)
        self.PA.click_Add_patient_button()
        self.PA.ADD_patients_name(self.Patients_name)
        self.PA.ADD_Patients_email(self.Patients_email)
        self.PA.Add_Patients_phone(self.Patients_phone)
        self.PA.Sumit_General_detail_button()

#Add Patient Secondary details
        self.PA.ADD_Input_height(self.Height)
        self.PA.ADD_Input_weight(self.weight)
        self.PA.ADD_Input_gender(self.gender)
        self.PA.ADD_Input_age(self.age)
        self.PA.ADD_input_systolic(self.systolic)
        self.PA.ADD_input_diastolic(self.diastolic)
        self.PA.ADD_test_button()
#
        self.PA.ADD_blood_test_add()
        self.PA.ADD_vitamins_test_add_test()
        self.PA.ADD_Discount_test_add()
        self.PA.ADD_Lab_recomamdation()
        self.PA.ADD_equipment()
        self.PA.ADD_Select_test()
        self.PA.ADD_Save_button()
        self.PA.ADD_Add_patients_button()

#After adding a test, it will be reflected in the list of todos
        todo_lists = self.PA.ADD_List_of_active_test()
        for todo_list in todo_lists:
            Actual_todo_list.append(todo_list)

        if "self.Patients_name" in Actual_todo_list:
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False
