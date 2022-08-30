from http.server import executable
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#finds the path to the webdriver, open the webpage, and maximize the window
driver = webdriver.Chrome(executable_path = r'C:\\Users\\oniki_000.000\\Desktop\\TF\\Webdriver\\chromedriver_win32\\chromedriver.exe')
driver.get('https://www.spotify.com/us/premium/')
wait = WebDriverWait(driver, 10)
driver.maximize_window()

#click on View Plans
Plans = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='spoti-root']/div/main/section[1]/article/header/div[1]/div[3]/div[2]/a/div[1]")))
Plans.click()

#scroll down the home webpage
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

#close out the cookies prompt
sleep(2)
Close = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='onetrust-close-btn-container']/button")))
Close.click()

#click on Individual Plan
sleep(2)
Individual = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='plans']/article/div[2]/div[2]/div/a/div[1]")))
Individual.click()