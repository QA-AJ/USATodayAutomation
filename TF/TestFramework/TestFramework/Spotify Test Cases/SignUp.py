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

#click on the Sign Up option
Select = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#main > div > div.Root__top-container > div.Root__top-bar > header > div.LKFFk88SIRC9QKKUWR5u > button.Button-sc-1dqy6lx-0.gZafTI.sibxBMlr_oxWTfBrEz2G")))
Select.click()

#click on the email option and enter the information
Email = wait.until(EC.element_to_be_clickable((By.ID, "email")))
Email.click()
Email.send_keys("testaccountbaby@gmail.com")

#click on the confirm email option and reenter the same email
Email = wait.until(EC.element_to_be_clickable((By.ID, "confirm")))
Email.click()
Email.send_keys("testaccountbaby@gmail.com")

#click on the password option and enter the information
Password = wait.until(EC.element_to_be_clickable((By.ID, "password")))
Password.click()
Password.send_keys("Th3B!gge$tGuy-")

#click on the username option and enter the information
Username = wait.until(EC.element_to_be_clickable((By.ID, "displayname")))
Username.click()
Username.send_keys("TheRealInternationalWonder15")

#click on the month option and pick a year
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
sleep(2)
Month = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='month']")))
Month.click()
Month.send_keys("F")

#click on the Day option and enter the information
Day = wait.until(EC.element_to_be_clickable((By.ID, "day")))
Day.click()
Day.send_keys("17")

#click on the Year option and enter the information
Year = wait.until(EC.element_to_be_clickable((By.ID, "year")))
Year.click()
Year.send_keys("1970")

#click on the male gender option
Select = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/main/div/div/form/fieldset/div/div[1]")))
Select.click()

#click on the sign up option for the first time
SignUp = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#__next > main > div > div > form > div.EmailForm__Center-jwtojv-0.itqiSk > div > button")))
SignUp.click()

#click on the "I'm not a robot" option
Captcha = wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[starts-with(@name, 'a-') and starts-with(@src, 'https://www.google.com/recaptcha')]")))
Robot = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='recaptcha-anchor']/div[1]")))
Robot.click()

#click on the sign up option for the second time
TrueSignUp = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#__next > main > div > div > form > div.EmailForm__Center-jwtojv-0.itqiSk > div > button")))
TrueSignUp.click()
