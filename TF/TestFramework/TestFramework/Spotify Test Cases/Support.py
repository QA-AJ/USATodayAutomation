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

#click on the support option
Support = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#spoti-root > div > div:nth-child(1) > header > div > nav > ul > li:nth-child(2) > a")))
Support.click()

#Search for missing music or podcasts
sleep(2)
Music = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div[2]/div[1]/div[2]/div[1]/input")))
Music.click()
Music.send_keys("Music")
MissingMusic = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#__next > div.mainContainer > div:nth-child(1) > div.Search__Container-sc-1bio9hz-0.ksUJub > div.SearchResults__Container-sc-1k7y5gq-0.jybEPW > ul > li:nth-child(1) > a > span")))
MissingMusic.click()

#Scroll down and click on Yes for helpful article
sleep(2)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
Helpful = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#__next > div.mainContainer > div > div.Article__BottomContainer-sc-1gl2ake-2.hSavHO > div > button:nth-child(2)")))
Helpful.click()

#Scroll back up and click on account hacked link
sleep(2)
driver.execute_script("scrollBy(0,-document.body.scrollTop)")
Hacked = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#__next > div.mainContainer > div > div:nth-child(2) > div > p:nth-child(7) > a")))
Hacked.click()

#scroll down and click on No for helpgul article
sleep(2)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
NotHelpful = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#__next > div.mainContainer > div > div.Article__BottomContainer-sc-1gl2ake-2.hSavHO > div > button:nth-child(2)")))
NotHelpful.click()

