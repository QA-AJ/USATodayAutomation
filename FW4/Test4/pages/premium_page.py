from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class PremiumPage():
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def prem(self):
        #click on the premium option at the top of the screen
        Prem = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#main > div > div.Root__top-container > div.Root__top-bar > header > button:nth-child(5)")))
        Prem.click()

    #def views(self):
    #    #click on View Plans
    #    sleep(2)
    #    Plans = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "Button-qlcn5g-0 eJSmcN")))
    #    Plans.click()

    #def cookies(self):
    #    #close out the cookies prompt
    #    sleep(4)
    #    Close = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='onetrust-close-btn-container']/button")))
    #    Close.click()

    #def scroll(self):
    #    #scroll down the home webpage
    #    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    #def individual(self):
    #    #click on Individual Plan
    #    sleep(2)
    #    Individual = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='plans']/article/div[2]/div[2]/div/a/div[1]")))
    #    Individual.click()
