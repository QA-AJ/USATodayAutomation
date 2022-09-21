from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class SearchPage():
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def searching(self):
        #click on the Search Bar option from the home screen
        HomeMenu = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#main > div > div.Root__top-container > nav > div.tUwyjggD2n5KvEtP5z1B > ul > li:nth-child(2) > a")))
        HomeMenu.click()
      
    def name(self, searchBar):
        #click on the search bar and type in "God-blo"
        sleep(4)
        SearchSpot = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main']/div/div[2]/div[1]/header/div[3]/div/div/form/input")))
        SearchSpot.click()
        SearchSpot.send_keys(searchBar)
        Podcasts = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#main > div > div.Root__top-container > div.Root__main-view > div.main-view-container > div.os-host.os-host-foreign.os-theme-spotify.os-host-resize-disabled.os-host-scrollbar-horizontal-hidden.main-view-container__scroll-node.os-host-transition.os-host-overflow.os-host-overflow-y > div.os-padding > div > div > div.main-view-container__scroll-node-child > main > div.fVB_YDdnaDlztX7CcWTA > div > div > div > div.KjPUGV8uMbl_0bvk9ePv > a:nth-child(6) > button > span")))
        Podcasts.click()

    def blog(self):
        #click on the The Blog for the Gods podcast
        sleep(4)
        Extra = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='searchPage']/div/div/div[1]/section/div[2]/div[4]/div/div[2]/a/div")))
        Extra.click()

    def episode(self):
        #click on Level 11 episode
        Episode = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='main']/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[4]/div[2]/div[2]/div[1]/div")))
        Episode.click()

    def play(self):
        #click on play
        sleep(2)
        All= self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='play-button']")))
        All.click()
        sleep(15)