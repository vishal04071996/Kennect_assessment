import configparser


config = configparser.RawConfigParser()
config.read(".//configurations/config.ini")




class Read_Config:
   @staticmethod
   def get_email():
       email = config.get('admin login info', 'email')
       return email


   @staticmethod
   def get_Password():
       Password = config.get('admin login info', 'Password')
       return Password


   @staticmethod
   def get_wrong_email():
       wrong_email = config.get('admin login info', 'wrong_email')
       return wrong_email


   @staticmethod
   def get_wrong_password():
       wrong_password = config.get('admin login info', 'wrong_password')
       return wrong_password


   @staticmethod
   def get_URL():
       URL = config.get('admin login info', 'URL')
       return URL


   @staticmethod
   def get_actual_text():
       actual_text = config.get('admin login info', 'actual_text')
       return actual_text

   @staticmethod
   def get_Patients_name():
       Patients_name = config.get('admin login info', 'Patients_name')
       return Patients_name


   @staticmethod
   def get_Patients_email():
       Patients_email = config.get('admin login info', 'Patients_email')
       return Patients_email

   @staticmethod
   def get_Patients_phone():
       Patients_phone = config.get('admin login info', 'Patients_phone')
       return Patients_phone

   @staticmethod
   def get_Height():
       Height = config.get('admin login info', 'Height')
       return Height

   @staticmethod
   def get_weight():
       weight = config.get('admin login info', 'weight')
       return weight

   @staticmethod
   def get_gender():
       gender = config.get('admin login info', 'gender')
       return gender

   @staticmethod
   def get_age():
       age = config.get('admin login info', 'age')
       return age

   @staticmethod
   def get_systolic():
       systolic = config.get('admin login info', 'systolic')
       return systolic

   @staticmethod
   def get_diastolic():
       diastolic = config.get('admin login info', 'diastolic')
       return diastolic

   @staticmethod
   def get_URL2():
       URL2 = config.get('admin login info', 'URL2')
       return URL2
