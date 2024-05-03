#Imports needed for the code to work
from time import sleep
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver

#Code to create the applicable page for externalizing in other test cases. Super code externalizes the Base Driver so the operator can use the methods from that particular file
class LaunchPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    #**FIRST LOCATOR VARIABLE BELOW MAY NEED TO BE COMMENTED OUT BECAUSE THIS ELEMENT TENDS TO APPEAR RANDOMLY. ELEMENT APPEARS AS OF 4/30/202
        
    #Locator variables. Change these to affect the test case
    CLOSE_PROMPT_BUTTON = "//div[@class='gnt_mol']//button[@class='gnt_mol_xb']"
    TECH_PAGE = "(//nav[@class='gnt_n_mn']//a[@class='gnt_n_mn_l gnt_n_mn_ce'])[6]"
    PROBLEMS_SOLVED_BUTTON = "(//a[@class='gnt_sn_a gnt_sn_a_w'])[4]"
    SHADOW_ROOT = 'return document.querySelector("#mainContentSection > special-franchise-hero").shadowRoot.querySelector("div > div > div.hero-slot > a > div.text-wrap")'
    FIRST_OPTION_BUTTON = "//dive[@class='franchise-wrapper video']//a[@class='top-container']"   
  
    #**FIRST METHOD BELOW MAY NEED TO BE COMMENTED OUT BECAUSE THIS ELEMENT TENDS TO APPEAR RANDOMLY. ELEMENT APPEARS AS OF 4/30/2024
    
    #CLOSE PROMPT BUTTON METHOD - Code for a method that called the location of the close prompt button from the above locators variables
    def getClosePromptButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.CLOSE_PROMPT_BUTTON)

    #Code for a method to call the SUBSCRIBE PAGE METHOD and then clicks on the link
    def enterClosePromptButtonLocation(self):
        self.getClosePromptButtonLocation().click()

    #TECH PAGE METHOD - Code for a method that called the location of the tecg page from the above locators variables
    def getTechPageLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.TECH_PAGE)

    #Code for a method to call the TECH PAGE METHOD and then clicks on the link
    def enterTechPageLocation(self):
        self.getTechPageLocation().click()

    #PROBLEMS SOLVED BUTTON METHOD - Code for a method that called the location of the problems solved button from the above locators variables
    def getProblemsSolvedButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.PROBLEMS_SOLVED_BUTTON)

    #Code for a method to call the PROBLEMS SOLVED BUTTON METHOD and then clicks on the link
    def enterProblemsSolvedButtonLocation(self):
        self.getProblemsSolvedButtonLocation().click()
        
    #SHADOW ROOT METHOD - Code for a method that called the location of the shadow root button from the above locators variables
    def getShadowRootLocation(self):
        return self.wait_until_access_to_shadow_root(self.SHADOW_ROOT)
    
    def enterShadowRootLocation(self):
        sleep(10)
        self.getShadowRootLocation().click()
        sleep(10)