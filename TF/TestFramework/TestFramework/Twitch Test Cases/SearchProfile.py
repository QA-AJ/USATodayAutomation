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
Search.send_keys("Maximillian_Dood")
Search.send_keys(Keys.ENTER)

#click on the profile
Profile = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div[2]/div/main/div[1]/div[3]/div/div/div/div/div[1]/div/div[1]/div[1]/div[2]/div/div/div[2]/div[1]/div/div/strong/a")))
Profile.click()

##Pause the video playing
#MainVideo = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='channel-player']/div/div[1]/div[1]/button/div/div/div/svg/g/path")))
#MainVideo.click()

#click on the videos tab
sleep(2)
Videos = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='offline-channel-main-content']/div[2]/div[2]/div/div/ul/li[4]/a/div/div[1]/p")))
Videos.click()

#click on the most recent video
sleep(2)
Recent = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='offline-channel-main-content']/div[3]/div/div/div/div/div/div/div[2]/div[2]/div[1]/div/div/article[1]/div[1]/div/div[1]/div[1]/div/a/h3")))
Recent.click()
