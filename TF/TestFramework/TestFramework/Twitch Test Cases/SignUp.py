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
SignUp = wait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='root']/div/div[2]/nav/div/div[3]/div[3]/div/div[1]/div[2]/button")))
SignUp.click()
sleep(4)

#enter in account information
Username = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='signup-username']")))
Username.send_keys("TerryBossMade")
Password = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='password-input']")))
Password.send_keys("Sp3ct@cle$0fL!feBaby")
ConfirmPassword = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='password-input-confirmation']")))
ConfirmPassword.send_keys("Sp3ct@cle$0fL!feBaby")
Month = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[3]/div/div[2]/div[1]/select")))
Month.send_keys("Jan")
Month.send_keys(Keys.ENTER)
Day = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[3]/div/div[2]/div[2]/div/input")))
Day.send_keys("15")
Day.send_keys(Keys.ENTER)
Year = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[3]/div/div[2]/div[3]/div/input")))
Year.send_keys("1980")
Year.send_keys(Keys.ENTER)

#Select email instead option
sleep(2)
Instead = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[4]/div/div[2]/button/div/div[2]")))
Instead.click()

#enter email
sleep(2)
Email = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='email-input']")))
Email.send_keys("TopG4Lyfe@gmail.com")

#Click on sign up button
Finish = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/div/div/div/div/div/div[1]/div/div/div[3]/form/div/div[5]/button")))
Finish.click()