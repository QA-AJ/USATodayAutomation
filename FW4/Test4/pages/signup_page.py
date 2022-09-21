from logging import captureWarnings
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class SignUpPage():
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def signup(self):
        #click on the Sign Up option
        sleep(2)
        Select = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#main > div > div.Root__top-container > div.Root__top-bar > header > div.LKFFk88SIRC9QKKUWR5u > button.Button-sc-1dqy6lx-0.daAltg.sibxBMlr_oxWTfBrEz2G")))
        Select.click()

    def cookies(self):
        #close out the cookies prompt
        sleep(2)
        close = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='onetrust-close-btn-container']/button")))
        close.click()

    def address(self, email):
        #click on the email option and enter the information
        sleep(2)
        Email = self.wait.until(EC.element_to_be_clickable((By.ID, "email")))
        Email.click()
        Email.send_keys(email)

    def confirmaddress(self, conmail):
        #click on the confirm email option and reenter the same email
        sleep(2)
        Email = self.wait.until(EC.element_to_be_clickable((By.ID, "confirm")))
        Email.click()
        Email.send_keys(conmail)

    def password(self, PW):
        #click on the password option and enter the information
        sleep(2)
        Password = self.wait.until(EC.element_to_be_clickable((By.ID, "password")))
        Password.click()
        Password.send_keys(PW)

    def username(self, UN):
        #click on the username option and enter the information
        sleep(2)
        Username = self.wait.until(EC.element_to_be_clickable((By.ID, "displayname")))
        Username.click()
        Username.send_keys(UN)

    def month(self, Mon):
        #click on the month option and pick a year
        sleep(2)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        sleep(4)
        Month = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='month']")))
        Month.click()
        Month.send_keys(Mon)

    def day(self, DY):
        #click on the Day option and enter the information
        sleep(4)
        Day = self.wait.until(EC.element_to_be_clickable((By.ID, "day")))
        Day.click()
        Day.send_keys(DY)

    def year(self, YR):
        #click on the Year option and enter the information
        sleep(4)
        Year = self.wait.until(EC.element_to_be_clickable((By.ID, "year")))
        Year.click()
        Year.send_keys(YR)

    def gender(self):
        #click on the male gender option
        sleep(4)
        Select = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/main/div/div/form/fieldset/div/div[1]")))
        Select.click()

    def captcha(self):
        #click on the captcha and confirm the "I'm not a robot" option
        sleep(4)
        self.wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[starts-with(@name, 'a-') and starts-with(@src, 'https://www.google.com/recaptcha')]")))
        Robot = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='recaptcha-anchor']/div[1]")))
        Robot.click()

    def truesignup(self):
        #click on the sign up option
        sleep(4)
        SignUp = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#__next > main > div > div > form > div.EmailForm__Center-jwtojv-0.itqiSk > div > button > div.ButtonInner-sc-14ud5tc-0.kjYGDx.encore-bright-accent-set.SignupButton___StyledButtonPrimary-cjcq5h-1.frbGK")))
        SignUp.click()