import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver




@pytest.fixture()
def setup():
   driver = webdriver.Chrome()
   return driver
