from http.server import executable
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#finds the path to the webdriver, open the webpage, and maximize the window
driver = webdriver.Chrome(executable_path = r'C:\\Users\\oniki_000.000\\Desktop\\AutomationTestingMasterclass\\Drivers\\Chromedriver\\chromedriver_win32\\chromedriver.exe')
driver.get('https://www.twitch.tv')
wait = WebDriverWait(driver, 10)
driver.maximize_window()

#use the search bar to look for Maximillian_Dood's profile
Search = wait.until(EC.element_to_be_clickable((By.XPATH,"(//input[@type='search'])[1]")))
Search.click()
sleep(4)
Search.send_keys("Call of Duty: Modern Warfare")
Search.send_keys(Keys.ENTER)

#select Call of Duty: Modern Warfare
COD = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div[2]/div/main/div[1]/div[3]/div/div/div/div/div[1]/div/div[2]/div[1]/div[3]/div/div/div[2]/div/div[1]/div/strong")))
COD.click()

#select the clips tab
sleep(2)
Clips = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='directory-game-main-content']/div[3]/div/ul/li[3]/a/div/div[1]/p")))
Clips.click()

#select the most recent crossbow clip
sleep(4)
Recent = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='directory-game-main-content']/div[4]/div[1]/div/div/div/div[2]/article/div[1]/div/div[1]/div[1]/div/a/h3")))
Recent.click()