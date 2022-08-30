from webbrowser import get
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

class setup():
     #Launch the browser and open defined website
     driver = webdriver.Chrome(executable_path = r'C:\\Users\\oniki_000.000\\Desktop\\AutomationTestingMasterclass\\Drivers\\Chromedriver\\chromedriver_win32\\chromedriver.exe')
     wait = WebDriverWait(driver, 10)
     driver.get('https://www.youtube.com/')
     driver.maximize_window()
