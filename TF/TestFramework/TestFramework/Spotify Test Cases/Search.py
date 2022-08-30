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

#click on the Search option
Select = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#main > div > div.Root__top-container > nav > div.tUwyjggD2n5KvEtP5z1B > ul > li:nth-child(2) > a > span")))
Select.click()

#click on the Search Bar option
sleep(2)
SearchBar = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main']/div/div[2]/div[1]/header/div[3]/div/div/form/input")))
SearchBar.click()
SearchBar.send_keys("God-Blo")
Podcasts = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#main > div > div.Root__top-container > div.Root__main-view > div.main-view-container > div.os-host.os-host-foreign.os-theme-spotify.os-host-resize-disabled.os-host-scrollbar-horizontal-hidden.main-view-container__scroll-node.os-host-transition.os-host-overflow.os-host-overflow-y > div.os-padding > div > div > div.main-view-container__scroll-node-child > main > div.fVB_YDdnaDlztX7CcWTA > div > div > div > div.KjPUGV8uMbl_0bvk9ePv > a:nth-child(6) > button > span")))
Podcasts.click()

#click on the The Blog for the Gods podcast
sleep(4)
Extra = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='searchPage']/div/div/div[1]/section/div[2]/div[4]/div/div[2]/a/div")))
Extra.click()

#click on Level 11 episode
Episode = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main']/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[4]/div[2]/div[2]/div[1]/div/div[2]/div/a/h4")))
Episode.click()

#click on play
sleep(2)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
All= wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main']/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[4]/a")))
All.click()
