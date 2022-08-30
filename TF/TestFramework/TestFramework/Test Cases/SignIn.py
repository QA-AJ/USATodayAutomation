#import things
from http.server import executable
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


#finds the path to the webdriver, open the webpage, and maximize the window
driver = webdriver.Chrome(executable_path = r'C:\\Users\\oniki_000.000\\Desktop\\AutomationTestingMasterclass\\Drivers\\Chromedriver\\chromedriver_win32\\chromedriver.exe')
driver.get('https://www.youtube.com')
wait = WebDriverWait(driver, 10)
driver.maximize_window()

#go to the sign in button and click it
Select = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/div[1]/tp-yt-app-drawer/div[2]/div/div[2]/div[2]/ytd-guide-renderer/div[1]/ytd-guide-signin-promo-renderer/ytd-button-renderer/a/tp-yt-paper-button")))
Select.click()

#click on create account and go through the process
SignIn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#yDmH0d > c-wiz > div > div.eKnrVb > div > div.Z6Ep7d > div > div.XOrBDc > div > div > div:nth-child(1) > div > button > span")))
SignIn.click()
sleep(2)
Account = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#yDmH0d > c-wiz > div > div.eKnrVb > div > div.Z6Ep7d > div > div.XOrBDc > div > div > div:nth-child(2) > div > ul > li:nth-child(2) > span.VfPpkd-StrnGf-rymPhb-b9t22c")))
Account.click()

#enter in account information
FirstName = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='firstName']")))
FirstName.send_keys("Jimmy")
LastName = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='lastName']" )))
LastName.send_keys("Jim")
Username = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='username']")))
Username.send_keys("biggestsupertest123@gmail.com")
Password = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='passwd']/div[1]/div/div[1]/input")))
Password.send_keys("bigbrain1")
ConfirmPassword = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='confirm-passwd']/div[1]/div/div[1]/input")))
ConfirmPassword.send_keys("bigbrain1")

#click the next button
Next = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#accountDetailsNext > div > button > span")))
Next.click()

