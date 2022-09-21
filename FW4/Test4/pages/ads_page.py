from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class ForAds():
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

    def advert(self):
        #click on advertising under the communities category
        Adverts = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#main > div > div.Root__top-container > div.Root__main-view > div.main-view-container > div.os-host.os-host-foreign.os-theme-spotify.os-host-resize-disabled.os-host-scrollbar-horizontal-hidden.main-view-container__scroll-node.os-host-overflow.os-host-overflow-y.os-host-transition > div.os-padding > div > div > div.main-view-container__mh-footer-container > nav > div.Footer__TopSection-sc-xwm5vq-1.gFNFTZ > div.Footer__StyledTopLinks-sc-xwm5vq-2.tENXN > div:nth-child(2) > ul > a:nth-child(4) > span")))
        Adverts.click()
        sleep(6)

    def close(self):
        #close the popup
        Close = self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[5]/div[2]/button")))
        Close.click()

    def bottom(self):
        #scroll to the bottom of the page
        self.driver.execute_script("window.scrollTo(0, 4500)")
        sleep(6)

    def first(self, Select):
        #select an option from the first dropdown
        Select = Select(self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/section/div/div/form/fieldset/div[1]/label[1]/div/select"))))
        Select.select_by_visible_text('an agency')
    
    def second(self):
        #select an option from the second dropdown
        sleep(2)
        Select = Select(self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/section/div/div/form/fieldset/div[1]/label[2]/div/select"))))
        Select.select_by_visible_text('drive traffic')
    
    def fname(self, firstName):
        #fill in first name
        Fname = self.wait.until(EC.element_to_be_clickable((By.NAME, "firstName")))
        Fname.click()
        Fname.send_keys(firstName)
    
    def lname(self, lastName):
        #fill in last name
        Lname = self.wait.until(EC.element_to_be_clickable((By.NAME, "lastName")))
        Lname.click()
        Lname.send_keys(lastName)
    
    def email(self, emailAdd):
        #fill in email address
        Email = self.wait.until(EC.element_to_be_clickable((By.NAME, "email")))
        Email.click()
        Email.send_keys(emailAdd)
    
    def company(self, companyName):
        #fill in company
        Cname = self.wait.until(EC.element_to_be_clickable((By.NAME, "company")))
        Cname.click()
        Cname.send_keys(companyName)
    
    
    #def
    
    
    #def