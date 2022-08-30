from http.server import executable
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#finds the path to the webdriver, open the webpage, and maximize the window
driver = webdriver.Chrome(executable_path = r'C:\\Users\\oniki_000.000\\Desktop\\AutomationTestingMasterclass\\Drivers\\Chromedriver\\chromedriver_win32\\chromedriver.exe')
driver.get('https://www.youtube.com')
wait = WebDriverWait(driver, 10)
driver.maximize_window()

#go to the sign in button and click it
Explore = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='endpoint']/tp-yt-paper-item")))
sleep(4)
Explore.click()
