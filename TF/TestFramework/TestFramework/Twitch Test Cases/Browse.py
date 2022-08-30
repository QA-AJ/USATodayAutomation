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

##navigate to the following page on tiktok
Browse = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div[2]/nav/div/div[1]/div[2]/div/div/div[1]/a")))
Browse.click()

#click on Game option
sleep(4)
Game = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='browse-root-main-content']/div[2]/div/div[1]/div/a/div")))
Game.click()

#click on League of Legends
sleep(4)
LOL = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div[2]/div/main/div[1]/div[3]/div/div/div/div/div[1]/div[3]/div[2]/div/div[4]/div/div[1]/div/div/div/div/span/a/h2")))
LOL.click()

#click on LCS profile
Profile = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='directory-game-main-content']/div[4]/div/div[1]/div[1]/div[2]/div/div/div/article/div[1]/div/div[1]/div[1]/a/h3")))
Profile.click()

#expand the player to full view
Video = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div[2]/div/main/div[1]/div[3]/div/div/div[1]/div[1]/div[1]/div[2]/div/div/div[1]/div/div")))
Video.click()
