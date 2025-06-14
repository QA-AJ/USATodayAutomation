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
    SPORTS_PAGE = "(//nav[@class='gnt_n_mn']//a[@class='gnt_n_mn_l gnt_n_mn_ce'])[2]"
    NFL_DRAFT_HUB_BUTTON = "(//a[@class='gnt_sn_a gnt_sn_a_w'])[1]"
    DRAFT_TRACKER_BUTTON = "(//div[@class='class-b-Q7YQ2 class-kYojzCo']//li[@class='class-VS1QjVh'])[1]" #//*[@id='__next']/div/div[5]/div/div[2]/div/div[1]/div/div/ul/li[2]"
    MOCK_DRAFTS_BUTTON = "(//div[@class='class-b-Q7YQ2 class-kYojzCo']//li[@class='class-VS1QjVh'])[2]"
    AT_THE_DRAFT_BUTTON = "(//div[@class='class-b-Q7YQ2 class-kYojzCo']//li[@class='class-VS1QjVh'])[5]" 
  
    #**FIRST METHOD BELOW MAY NEED TO BE COMMENTED OUT BECAUSE THIS ELEMENT TENDS TO APPEAR RANDOMLY. ELEMENT APPEARS AS OF 4/30/2024
    
    #CLOSE PROMPT BUTTON METHOD - Code for a method that called the location of the close prompt button from the above locators variables
    def getClosePromptButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.CLOSE_PROMPT_BUTTON)

    #Code for a method to call the SUBSCRIBE PAGE METHOD and then clicks on the link
    def enterClosePromptButtonLocation(self):
        self.getClosePromptButtonLocation().click()

    #SPORTS PAGE METHOD - Code for a method that called the location of the sports page from the above locators variables
    def getSportsPageLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.SPORTS_PAGE)

    #Code for a method to call the ENTERTAINMENT PAGE METHOD and then clicks on the link
    def enterSportsPageLocation(self):
        self.getSportsPageLocation().click()
        
    #NFL DRAFT HUB BUTTON METHOD - Code for a method that called the location of the nfl draft hub button from the above locators variables
    def getNFLDraftHubButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.NFL_DRAFT_HUB_BUTTON)
    
    #Code for a method to call the BOOKS DROP DOWN METHOD and then clicks on the link
    def enterNFLDraftHubButtonLocation(self):
        self.getNFLDraftHubButtonLocation().click()
        
    #DRAFT TRACKER BUTTON METHOD - Code for a method that called the location of the draft tracker button from the above locators variables
    def getDraftTrackerButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.DRAFT_TRACKER_BUTTON)
    
    #Code for a method to call the DRAFT TRACKER BUTTON METHOD and then clicks on the link
    def enterDraftTrackerButtonLocation(self):
        sleep(2)
        self.getDraftTrackerButtonLocation().click()
        
    #MOCK DRAFTS BUTTON METHOD - Code for a method that called the location of the mock drafts button from the above locators variables
    def getMockDraftsButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.MOCK_DRAFTS_BUTTON)
    
    #Code for a method to call the MOCK DRAFTS BUTTON METHOD and then clicks on the link
    def enterMockDraftsButtonLocation(self):
        sleep(2)
        self.getMockDraftsButtonLocation().click()
        
    #AT THE DRAFT BUTTON METHOD - Code for a method that called the location of the at the draft button from the above locators variables
    def getAtTheDraftButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.AT_THE_DRAFT_BUTTON)
    
    #Code for a method to call the AT THE DRAFT BUTTON METHOD and then clicks on the link
    def enterAtTheDraftButtonLocation(self):
        sleep(2)
        self.getAtTheDraftButtonLocation().click()