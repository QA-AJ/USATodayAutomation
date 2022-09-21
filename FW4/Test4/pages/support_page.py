from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class SupportPage():
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def support(self):
        #click on the support option at the top of the screen
        Support = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#main > div > div.Root__top-container > div.Root__top-bar > header > button:nth-child(6)")))
        Support.click()

    def search(self, missingMusic):
        #Search for missing music or podcasts
        sleep(4)
        Music = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div[2]/div[1]/div[2]/div/input")))
        Music.click()
        Music.send_keys(missingMusic)

    def music(self):
        #click on the missing music or podcasts option
        MissingMusic = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#__next > div.mainContainer > div:nth-child(1) > div.Search__Container-sc-1bio9hz-0.ksUJub > div.SearchResults__Container-sc-1k7y5gq-0.jybEPW > ul > li:nth-child(1) > a > span")))
        MissingMusic.click()

    def helpful(self):
        #Scroll down and click on Yes for helpful article
        sleep(2)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        Helpful = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#__next > div.mainContainer > div > div.Article__BottomContainer-sc-1gl2ake-2.hSavHO > div > button:nth-child(2)")))
        Helpful.click()

    def hacked(self):
        #Scroll back up and click on account hacked link
        sleep(2)
        self.driver.execute_script("scrollBy(0,-document.body.scrollTop)")
        Hacked = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#__next > div.mainContainer > div > div:nth-child(2) > div > p:nth-child(7) > a")))
        Hacked.click()

    def no(self):
        #scroll down and click on No for helpgul article
        sleep(2)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        NotHelpful = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#__next > div.mainContainer > div > div.Article__BottomContainer-sc-1gl2ake-2.hSavHO > div > button:nth-child(2)")))
        NotHelpful.click()