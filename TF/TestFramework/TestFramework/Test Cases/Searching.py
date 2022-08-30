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

#Click on the search button and look up Automation
SearchBar = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input")))
SearchBar.send_keys("Automation")
SearchIcon = wait.until(EC.element_to_be_clickable((By.ID, "search-icon-legacy")))
SearchIcon.click()

#Click on the required Automation Video
ClickOn = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='video-title']/yt-formatted-string")))
sleep(4)
ClickOn.click()