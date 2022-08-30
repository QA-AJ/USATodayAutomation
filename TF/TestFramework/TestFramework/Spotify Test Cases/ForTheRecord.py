from http.server import executable
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#finds the path to the webdriver, open the webpage, and maximize the window
driver = webdriver.Chrome(executable_path = r'C:\\Users\\oniki_000.000\\Desktop\\TF\\Webdriver\\chromedriver_win32\\chromedriver.exe')
driver.get('https://www.spotify.com/us/')
wait = WebDriverWait(driver, 10)
driver.maximize_window()

#scroll down the home webpage
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

#close out the cookies prompt
sleep(2)
Close = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='onetrust-close-btn-container']/button")))
Close.click()

#click on the for the record option under the company category
Record = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main']/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[3]/nav/div[1]/div[1]/div[1]/ul/a[3]")))
Record.click()

#click on the first available option
sleep(2)
Kojima = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div/div/main/div/div[1]/div[3]/div[1]/div")))
Kojima.click()

#click on the share option and share it to LinkedIn
sleep(2)
driver.execute_script("window.scrollTo(0, 500)")
Share = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='post-18173']/header/div[2]/div/div/div/div[2]/div/div")))
Share.click()
sleep(2)
LinkedIn = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='share-dropdown']/ul/li[4]/a")))
LinkedIn.click()