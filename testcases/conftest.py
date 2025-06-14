#Module with code to handle the webdriver that can be used in test cases

#Imports needed for the code to work
import pytest
from selenium import webdriver

#Code to add command line options for use in the command line/terminal and/or in Jenkins
def pytest_addoption(parser):
    parser.addoption("--driver", "--url")

#Makes this a class fixture so it can be used that way when externalized in other test cases
@pytest.fixture(scope='class')
def setup(request):
    #Code to access the webdriver of the operator's chosing. 
    driver = webdriver.Chrome()
    
    #Code to maximize the browser window
    driver.maximize_window()
    
    #Code to get the webpage
    driver.get("https://usatoday.com/")
    
    #Code to make a class request for the driver
    request.cls.driver = driver
    yield
    
    #Code to close the driver
    driver.close()