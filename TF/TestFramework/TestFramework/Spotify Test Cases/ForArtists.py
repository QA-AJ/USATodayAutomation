from http.server import executable
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#finds the path to the webdriver, open the webpage, and maximize the window
driver = webdriver.Chrome(executable_path = r'C:\\Users\\oniki_000.000\\Desktop\\TF\\Webdriver\\chromedriver_win32\\chromedriver.exe')
driver.get('https://spotify.com/us')
wait = WebDriverWait(driver, 10)
driver.maximize_window()

#scroll down the home webpage
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

#close out the cookies prompt
sleep(2)
Close = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='onetrust-close-btn-container']/button")))
Close.click()

#click on for artists under the communities category
Artist = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#main > div > div.Root__top-container > div.Root__main-view > div.main-view-container > div.os-host.os-host-foreign.os-theme-spotify.os-host-resize-disabled.os-host-scrollbar-horizontal-hidden.main-view-container__scroll-node.os-host-transition.os-host-overflow.os-host-overflow-y > div.os-padding > div > div > div.main-view-container__mh-footer-container > nav > div.Footer__TopSection-sc-xwm5vq-1.gFNFTZ > div.Footer__StyledTopLinks-sc-xwm5vq-2.tENXN > div:nth-child(2) > ul > a:nth-child(2) > span")))
Artist.click()

#Scroll down the webpage and click on See All FAQs
sleep(4)
All = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='menu-links']/li[2]/span/a")))
All.click

#click on the Artisit profile option
Profile = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#menu-links > li:nth-child(2) > span")))
Profile.click()

#search for Managing your artist profile option
Manage = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/div/div/main/div/div/div[1]/div/div/div/input")))
Manage.click()
Manage.send_keys("Managing your artist profile")
sleep(2)
Art = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/div/div/main/div/div/div[1]/div/div/ul/li[2]/a")))
Art.click()

#click on the get access to spotify for artists option
Access = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#__next > div > div > div > main > div > div > div > div.sc-b7999c5f-2.hobtqb > div.sc-2c995646-1.sc-d0915642-0.jZzhGm.hmIDbW > div.sc-d0915642-2.gAbHAf > div > p:nth-child(4) > a > span")))
Access.click()