from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class ForArtist():
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def cookies(self):
        #close out the cookies prompt
        sleep(2)
        Close = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='onetrust-close-btn-container']/button")))
        Close.click()

    def art(self):
        #click on the for the artists option under the company category
        Artist = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#main > div > div.Root__top-container > div.Root__main-view > div.main-view-container > div.os-host.os-host-foreign.os-theme-spotify.os-host-resize-disabled.os-host-scrollbar-horizontal-hidden.main-view-container__scroll-node.os-host-transition.os-host-overflow.os-host-overflow-y > div.os-padding > div > div > div.main-view-container__mh-footer-container > nav > div.Footer__TopSection-sc-xwm5vq-1.gFNFTZ > div.Footer__StyledTopLinks-sc-xwm5vq-2.tENXN > div:nth-child(2) > ul > a:nth-child(2) > span")))
        Artist.click()

    def scroll(self):
        #Scroll to the bottom of the webpage
        self.driver.execute_script("var scrollingElement = (document.scrollingElement || document.body);scrollingElement.scrollTop = scrollingElement.scrollHeight;")
        sleep(4)

    def faq(self):
        #click on See All FAQs
        Profile = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#menu-links > li:nth-child(2) > span")))
        Profile.click()

    def manage(self, profileInfo):
        #search for Managing your artist profile option
        Manage = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/div/div/main/div/div/div[1]/div/div/div/input")))
        Manage.click()
        Manage.send_keys(profileInfo)
        sleep(2)
        Art = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='__next']/div/div/div/main/div/div/div[1]/div/div/ul/li[2]/a")))
        Art.click()
    
    def access(self):
        #click on the get access to spotify for artists option
        Access = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#__next > div > div > div > main > div > div > div > div.sc-b7999c5f-2.cqfCFI > div.sc-2c995646-1.sc-1212796e-0.ciTQmt.bzlckN > div.sc-1212796e-2.htHGrs > div > p:nth-child(4) > a > span")))
        Access.click()