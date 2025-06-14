#Imports needed for the code to work
from time import sleep
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver

#Code to create the applicable page for externalizing in other test cases. Super code externalizes the Base Driver so the operator can use the methods from that particular file
class LaunchPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    #**FIRST LOCATOR VARIABLE BELOW MAY NEED TO BE COMMENTED OUT BECAUSE THIS ELEMENT TENDS TO APPEAR RANDOMLY. ELEMENT APPEARS AS OF 4/30/2024

    #Locator variables. Change these to affect the test case
    CLOSE_PROMPT_BUTTON = "//div[@class='gnt_mol']//button[@class='gnt_mol_xb']"
    ELECTIONS_PAGE = "(//nav[@class='gnt_n_mn']//a[@class='gnt_n_mn_l gnt_n_mn_ce'])[1]"
    RESULTS_BUTTON = "//nav[@class='gnt_sn']//a[@class='gnt_sn_a gnt_sn_a_w']"
    VIEW_FULL_REPUBLICAN_RACE_DETAILS_BUTTON = "(//div[@class='_4-d4C-__4-d4C-']//a[@class='XYQycm__XYQycm'])[1]"
    VIEW_FULL_DEMOCRATIC_RACE_DETAILS_BUTTON = "(//div[@class='_4-d4C-__4-d4C-']//a[@class='XYQycm__XYQycm'])[2]"
    NEVADA_BUTTON = "//*[@id='base_32']"
    REPUBLICAN_NEVADA_ELECTION_RESULTS_BUTTON = "(//div[@class='_7mKtF8__7mKtF8']//span[@class='WUamXQ__WUamXQ icon-arrow-right-lg-1'])[4]"
    DEMOCRATIC_NEVADA_ELECTION_RESULTS_BUTTON = "(//div[@class='_7mKtF8__7mKtF8']//span[@class='WUamXQ__WUamXQ icon-arrow-right-lg-1'])[3]"
    CLARK_COUNTY_BUTTON = "//*[@id='county_3']"
    DELEGATES_BUTTON = "(//div[@class='iw9Kcp__iw9Kcp']//li[@class='_5BuDDG__5BuDDG'])[2]"
    
    #**FIRST METHOD BELOW MAY NEED TO BE COMMENTED OUT BECAUSE THIS ELEMENT TENDS TO APPEAR RANDOMLY. ELEMENT APPEARS AS OF 4/30/2024
    
    #CLOSE PROMPT BUTTON METHOD - Code for a method that called the location of the close prompt button from the above locators variables
    def getClosePromptButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.CLOSE_PROMPT_BUTTON)

    #Code for a method to call the CLOSE PROMPT BUTTON METHOD and then clicks on the link
    def enterClosePromptButtonLocation(self):
        self.getClosePromptButtonLocation().click()

    #ELECTIONS PAGE METHOD - Code for a method that called the location of the u.s. page from the above locators variables
    def getElectionsPageLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.ELECTIONS_PAGE)

    #Code for a method to call the ELECTIONS  PAGE METHOD and then clicks on the link
    def enterElectionsPageLocation(self):
        self.getElectionsPageLocation().click()
    
    #RESULTS BUTTON METHOD - Code for a method that called the location of the results button from the above locators variables
    def getResultsButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.RESULTS_BUTTON)

    #Code for a method to call the RESULTS BUTTON METHOD and then clicks on the link
    def enterResultsButtonLocation(self):
        self.getResultsButtonLocation().click()
        sleep(2)

    #VIEW FULL REPUBLICAN RACE DETAILS BUTTON METHOD - Code for a method that called the location of the view full republican race details button from the above locators variables
    def getViewFullRepublicanRaceDetailsButtonLocation(self):
        return self.scroll_to_element_and_click(By.XPATH, self.VIEW_FULL_REPUBLICAN_RACE_DETAILS_BUTTON)
        
    #NEVADA BUTTON METHOD - Code for a method that called the location of the nevada button from the above locators variables
    def getNevadaButtonLocation(self):
        return self.scroll_to_element_and_click(By.XPATH, self.NEVADA_BUTTON)

    #REPUBLICAN NEVADA ELECTION RESULTS BUTTON METHOD - Code for a method that called the location of the republican nevada election results button from the above locators variables
    def getRepublicanNevadaElectionResultsButtonLocation(self):
          return self.scroll_to_element_and_click(By.XPATH, self.REPUBLICAN_NEVADA_ELECTION_RESULTS_BUTTON)
    
    #CLARK COUNTY BUTTON METHOD - Code for a method that called the location of the clark county button from the above locators variables
    def getClarkCountyButtonLocation(self):
        return self.scroll_to_element_and_click(By.XPATH, self.CLARK_COUNTY_BUTTON)

    #DELEGATE BUTTON METHOD - Code for a method that called the location of the delegate button from the above locators variables
    def getDelegateButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.DELEGATES_BUTTON)

    #Code for a method to call the DELEGATE BUTTON METHOD and then clicks on the link
    def enterDelegateButtonLocation(self):
        sleep(2)
        self.getDelegateButtonLocation().click()
        
    #VIEW FULL DEMOCRATICIC RACE DETAILS BUTTON METHOD - Code for a method that called the location of the view full democratic race details button from the above locators variables
    def getViewFullDemocraticRaceDetailsButtonLocation(self):
        return self.scroll_to_element_and_click(By.XPATH, self.VIEW_FULL_DEMOCRATIC_RACE_DETAILS_BUTTON)
        
    #NEVADA BUTTON METHOD - Code for a method that called the location of the nevada button from the above locators variables
    def getNevadaButtonLocation(self):
        return self.scroll_to_element_and_click(By.XPATH, self.NEVADA_BUTTON)

    #DEMOCRATIC NEVADA ELECTION RESULTS BUTTON METHOD - Code for a method that called the location of the democratic nevada election results button from the above locators variables
    def getDemocraticNevadaElectionResultsButtonLocation(self):
        return self.scroll_to_element_and_click(By.XPATH, self.DEMOCRATIC_NEVADA_ELECTION_RESULTS_BUTTON)
    
    #CLARK COUNTY BUTTON METHOD - Code for a method that called the location of the clark county button from the above locators variables
    def getClarkCountyButtonLocation(self):
        return self.scroll_to_element_and_click(By.XPATH, self.CLARK_COUNTY_BUTTON)