from http.server import executable
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#finds the path to the webdriver, open the webpage, and maximize the window
driver = webdriver.Chrome(executable_path = r'C:\\Users\\oniki_000.000\\Desktop\\TF\\Webdriver\\chromedriver_win32\\chromedriver.exe')
driver.get('https://open.spotify.com/')
wait = WebDriverWait(driver, 10)
driver.maximize_window()

#scroll down the home webpage
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

#close out the cookies prompt
sleep(2)
Close = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='onetrust-close-btn-container']/button")))
Close.click()

#click on the see all option for the focus category
Focus = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#main > div > div.Root__top-container > div.Root__main-view > div.main-view-container > div.os-host.os-host-foreign.os-theme-spotify.os-host-resize-disabled.os-host-scrollbar-horizontal-hidden.main-view-container__scroll-node.os-host-transition.os-host-overflow.os-host-overflow-y > div.os-padding > div > div > div.main-view-container__scroll-node-child > main > section > div > div > section:nth-child(4) > div.q8AZzDc_1BumBHZg0tZb > div > a > span")))
Focus.click()

#click on peaceful piano
sleep(2)
Piano = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main']/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div/div/section/div[2]/div[1]/div/div[3]")))
Piano.click()

#click on La Vie
La_Vie = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main']/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div/div[2]/div[2]/div[1]/div/div[2]/div/a/div")))
La_Vie.click()

#click on play
Play = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#main > div > div.Root__top-container > div.Root__main-view > div.main-view-container > div.os-host.os-host-foreign.os-theme-spotify.os-host-resize-disabled.os-host-scrollbar-horizontal-hidden.main-view-container__scroll-node.os-host-transition.os-host-overflow.os-host-overflow-y > div.os-padding > div > div > div.main-view-container__scroll-node-child > main > section > div.os-host.os-host-foreign.os-theme-spotify.os-host-resize-disabled.os-host-scrollbar-horizontal-hidden.os-host-scrollbar-vertical-hidden.os-host-transition > div.os-padding > div > div > div > div > div > button > span > span")))
Play.click()

