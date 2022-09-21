from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class ForRecord():
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def scroll(self):
        #scroll down the home webpage
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def cookies(self):
        #close out the cookies prompt
        sleep(2)
        Close = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='onetrust-close-btn-container']/button")))
        Close.click()

    def record(self):
        #click on the for the record option under the company category
        Record = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main']/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[3]/nav/div[1]/div[1]/div[1]/ul/a[3]")))
        Record.click()

    def first(self):
        #click on the first available option in the upper right corner
        sleep(2)
        Page = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div/div/main/div/div[1]/div[3]/div[1]/div")))
        Page.click()

    def share(self):
        #click on the share option
        sleep(2)
        self.driver.execute_script("window.scrollTo(0, 500)")
        Share = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[3]/div/div[1]/main/article/header/div[2]/div/div/div/div[2]/div/div/button/span")))
        Share.click()
        
    def link(self):
        #share it to LinkedIn
        sleep(2)
        LinkedIn = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='share-dropdown']/ul/li[4]/a")))
        LinkedIn.click()