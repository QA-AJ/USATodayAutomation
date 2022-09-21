from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Investing():
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
    
    def cookies(self):
        #close out the cookies prompt
        sleep(2)
        Close = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='onetrust-close-btn-container']/button")))
        Close.click()

    def vesting(self):
        #click on investors under the communities category
        Invest = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#main > div > div.Root__top-container > div.Root__main-view > div.main-view-container > div.os-host.os-host-foreign.os-theme-spotify.os-host-overflow.os-host-overflow-y.os-host-resize-disabled.os-host-scrollbar-horizontal-hidden.main-view-container__scroll-node.os-host-transition > div.os-padding > div > div > div.main-view-container__mh-footer-container > nav > div.Footer__TopSection-sc-xwm5vq-1.gFNFTZ > div.Footer__StyledTopLinks-sc-xwm5vq-2.tENXN > div:nth-child(2) > ul > a:nth-child(5) > span")))
        Invest.click()
    
    def all(self):
        #click on the view all option
        Vall = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/form/div[2]/div/div[2]/div[3]/div/span/span[1]/div/div/div/div[2]/div/div[1]/div/a")))
        Vall.click()

    def quarter(self):
        #click on the first option
        first = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/form/div[2]/div/div[2]/div[3]/div/span/span[1]/div/div[1]/div/div[2]/div/div/div[1]/div[2]/div/ul/li[2]/a")))
        first.click()
        sleep(6)