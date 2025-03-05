From selenium.webdriver.common.by.import By


class login_page:
   enter_email = (By.XPATH, "//input[@name = 'email']")
   enter_password = (By.XPATH, "//input[@name = 'password']")
   click_login_button = (By.XPATH, "//button[@type = 'submit']//span[@class='MuiButton-label']l")
   error_message = (By.XPATH, "//div[@class = ‘MuiAlert-message’]")
   homepage_login = (By.XPATH, "//div[@class = ‘title’]")
   Test_cost_calculator = (By.XPATH, "//div[@class = ‘MuiBox-root jss82 title’]")
   Test_patient_dropdown = (By.XPATH, "//button[@class = 'MuiButtonBase-root MuiIconButton-root MuiAutocomplete-popupIndicator']//span[@class = 'MuiIconButton-label']")
   Select_test = (By.XPATH, "//div[@class = 'MuiBox-root jss484']")
   discount_dropdown = (By.XPATH, "//div[@class = 'MuiInputBase-root MuiOutlinedInput-root MuiInputBase-formControl']")
   select_discount = (By.XPATH, "//li[@data-value = '20']")
   Subtotal = (By.XPATH, "//div[@class = 'MuiBox-root jss93']")
   Total = (By.XPATH, "//div[@class = 'MuiBox-root jss96']")


   def __init__(self, driver):
       self.driver = driver


   def login_email(self, email):
       self.driver.find_element(*self.enter_email).send_keys(email)


   def login_password(self, Password):
       self.driver.find_element(*self.enter_password).send_keys(Password)


   def login_click_login_button(self):
       self.driver.find_element(*self.click_login_button).click()


   def login_error_message(self):
       return self.driver.find_element(*self.error_message).text


   def login_homepage(self):
       return self.driver.find_element(*self.homepage_login).text

   def login_Test_patient_dropdown(self):
       return self.driver.find_element(*self.Test_patient_dropdown).click()

   def login_Select_test(self):
       return self.driver.find_element(*self.Select_test).click()

   def login_discount_dropdown(self):
       return self.driver.find_element(*self.discount_dropdown).click()

   def login_select_discount(self):
       return self.driver.find_element(*self.select_discount).click()

   def login_Subtotal(self):
       return self.driver.find_element(*self.Subtotal).text

   def login_Total(self):
       return self.driver.find_element(*self.Total).text
