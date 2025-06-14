#Imports needed for the code to work
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
    OPINION_PAGE = "(//nav[@class='gnt_n_mn']//a[@class='gnt_n_mn_l gnt_n_mn_ce'])[8]"
    MEET_THE_OPINION_TEAM_BUTTON = "(//a[@class='gnt_sn_a gnt_sn_a_w'])[6]"  
    REX_HUPPKE_BUTTON = "(//div[@class='gnt_ar_b']//a[@target='_blank'])[12]" 
  
    #**FIRST METHOD BELOW MAY NEED TO BE COMMENTED OUT BECAUSE THIS ELEMENT TENDS TO APPEAR RANDOMLY. ELEMENT APPEARS AS OF 4/30/2024
    
    #CLOSE PROMPT BUTTON METHOD - Code for a method that called the location of the close prompt button from the above locators variables
    def getClosePromptButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.CLOSE_PROMPT_BUTTON)

    #Code for a method to call the SUBSCRIBE PAGE METHOD and then clicks on the link
    def enterClosePromptButtonLocation(self):
        self.getClosePromptButtonLocation().click()

    #OPINION PAGE METHOD - Code for a method that called the location of the opinion page from the above locators variables
    def getOpinionPageLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.OPINION_PAGE)

    #Code for a method to call the OPINION PAGE METHOD and then clicks on the link
    def enterOpinionPageLocation(self):
        self.getOpinionPageLocation().click()
    
    #MEET THE OPINION TEAM BUTTON METHOD - Code for a method that called the location of the meet the opinion team button from the above locators variables
    def getMeetTheOpinionTeamButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.MEET_THE_OPINION_TEAM_BUTTON)

    #Code for a method to call the MEET THE OPINION TEAM BUTTON METHOD and then clicks on the link
    def enterMeetTheOpinionTeamButtonLocation(self):
        self.getMeetTheOpinionTeamButtonLocation().click()
        
    #SCROLL DOWN TO AND CLICK ON REX HUPPKE BUTTON METHOD - Code for a method that called the location of the meet the opinion team button from the above locators variables
    def enterScrollDownToAndClickOnRexHuppkeButtonLocation(self):
        return self.scroll_to_element_and_click(By.XPATH, self.REX_HUPPKE_BUTTON)