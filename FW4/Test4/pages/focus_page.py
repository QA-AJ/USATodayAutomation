from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class ProfilePage():
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def cookies(self):
        #close out the cookies prompt
        sleep(2)
        Close = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='onetrust-close-btn-container']/button")))
        Close.click()

    def screen(self):
        #click on the see all option for the focus category
        Focus = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#main > div > div.Root__top-container > div.Root__main-view > div.main-view-container > div.os-host.os-host-foreign.os-theme-spotify.os-host-resize-disabled.os-host-scrollbar-horizontal-hidden.main-view-container__scroll-node.os-host-transition.os-host-overflow.os-host-overflow-y > div.os-padding > div > div > div.main-view-container__scroll-node-child > main > section > div > div > section:nth-child(4) > div.q8AZzDc_1BumBHZg0tZb > div > a > span")))
        Focus.click()

    def option(self):
        #click on first option
        sleep(2)
        Option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main']/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div/div/section/div[2]/div[1]/div/div[3]")))
        Option.click()

    def first(self):
        #click on first song option
        first = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main']/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/div/section/div[2]/div[3]/div/div[2]/div[2]/div[1]/div/div[2]/div/a/div")))
        first.click()

    def play(self):
        #click on play
        Play = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[3]/div[4]/div/div/div/div/div/button/span")))
        Play.click()
        sleep(4)