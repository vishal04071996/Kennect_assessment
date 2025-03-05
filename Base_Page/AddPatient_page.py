from selenium.webdriver.common.by import By


class Patient_form:
    # Locators
    Add_patient_button = (By.XPATH, "//a[@href='/patients/add']")
    Add_Patient_name = (By.XPATH, "//input[@name = 'name']")
    Add_Patients_email = (By.XPATH, "//input[@name = 'email']")
    Add_Patients_phone = (By.XPATH, "///input[@name = 'phone']")
    General_detail_button = (By.XPATH, "//span[@class = 'MuiButton-label jss836']")

    Input_height = (By.XPATH, "//input[@name = 'height']")
    Input_weight = (By.XPATH, "//input[@name='weight']")
    Input_gender = (By.XPATH, "//li[@data-value='male']")
    Input_age = (By.XPATH, "//input[@name='age']")
    input_systolic = (By.XPATH, "//input[@name='systolic']")

    input_diastolic = (By.XPATH, "//input[@name='diastolic']")
    add_test_button = (By.XPATH, "//span[@class = 'MuiButton-label jss836']")
    blood_test_add = (By.XPATH, "//input[@id = 'patient-test']")
    vitamins_test_add_test = (By.XPATH, "//span[@class='MuiChip-label']")
    Discount_test_add = (By.XPATH, "//li[@data-value = '15']")
    Lab_recomamdation = (By.XPATH, "Lab_recomamdation")
    Add_equipment = (By.XPATH, "//span[@class='material-icons MuiIcon-root']")
    Select_test = (By.XPATH, "//li[@data-value='JNvltFGjqTTtJKse2AEN']")
    Save_button = (By.XPATH, "//button[@title='Save']")
    Add_patients_button = (By.XPATH, "//span[@class='MuiButton-label jss836']")
    List_of_active_test = (By.XPATH, "//ul[@class='MuiList-root MuiList-padding']//li")

    URL2 = "https://gor-pathology.web.app/tests"

    exist_email1 = "User testdemo@mailinator.com already exist!"

    def __init__(self, driver):
        self.driver = driver

    # Methods
    def click_Add_patient_button(self):
        self.driver.find_element(*self.Add_patient_button).click()

    def ADD_patients_name(self, Patients_name):
        self.driver.find_element(*self.Add_patients_name).send_keys(Patients_name)

    def ADD_Patients_email(self, Patients_email):
        self.driver.find_element(*self.Add_Patients_email).send_keys(Patients_email)

    def ADD_Patients_phone(self, Patients_phone):
        self.driver.find_element(*self.Add_Patients_phone).send_keys(Patients_phone)

    def Sumit_General_detail_button(self):
        self.driver.find_element(*self.General_detail_button).click()

    def ADD_Input_height(self, Input_height):
        return self.driver.find_element(*self.Input_height).send_keys(Input_height)

    def ADD_Input_weight(self, Input_weight):
        return self.driver.find_element(*self.Input_weight).send_keys(Input_weight)

    def ADD_Input_gender(self, Input_gender):
        return self.driver.find_element(*self.Input_gender).send_keys(Input_gender)

    def ADD_Input_age(self, Input_age):
        return self.driver.find_element(*self.Input_age).send_keys(Input_age)

    def ADD_input_systolic(self, input_systolic):
        return self.driver.find_element(*self.input_systolic).send_keys(input_systolic)

    def ADD_input_diastolic(self, input_diastolic):
        return self.driver.find_element(*self.input_diastolic).send_keys(input_diastolic)

    def ADD_test_button(self):
        return self.driver.find_element(*self.add_test_button).click()

    def ADD_blood_test_add(self):
        self.driver.find_element(*self.blood_test_add).click()

    def ADD_vitamins_test_add_test(self):
        self.driver.find_element(*self.vitamins_test_add_test).click()

    def ADD_Discount_test_add(self):
        self.driver.find_element(*self.Discount_test_add).click()

    def ADD_Lab_recomamdation(self):
        self.driver.find_element(*self.Lab_recomamdation).click()

    def ADD_equipment(self):
        self.driver.find_element(*self.Add_equipment).click()

    def ADD_Select_test(self):
        self.driver.find_element(*self.Select_test).click()

    def ADD_Save_button(self):
        self.driver.find_element(*self.Save_button).click()

    def ADD_Add_patients_button(self):
        self.driver.find_element(*self.Add_patients_button).click()

    def ADD_List_of_active_test(self):
        return self.driver.find_element(*self.List_of_active_test).text
