#Imports needed for the code to work
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
    US_PAGE = "//nav[@class='gnt_n_mn']//a[@class='gnt_n_mn_l gnt_n_mn_l__fi gnt_n_mn_ce']"
    POLITICS_BUTTON = "(//div[@class='gnt_sn_a_w'])[2]//button"
    ELECTIONS_BUTTON = "//a[@class='gnt_sn_dd_a']"
    FOLLOW_THE_CANDIDATES_BUTTON = "(//div[@class='gnt_sn_a_w'])[1]//button"
    JOE_BIDEN_BUTTON = "(//a[@class='gnt_sn_dd_a'])[1]"
    ROBERT_F_KENNEDY_JR_BUTTON = "(//a[@class='gnt_sn_dd_a'])[1]"
    JILL_STEIN_BUTTON = "(//a[@class='gnt_sn_dd_a'])[2]"
    DONALD_TRUMP_BUTTON = "(//a[@class='gnt_sn_dd_a'])[3]"
    CORNEL_WEST_BUTTON = "(//a[@class='gnt_sn_dd_a'])[4]"
    MARIANNE_WILLIAMSON_BUTTON = "(//a[@class='gnt_sn_dd_a'])[5]"
    DROP_DOWN_BUTTON = "//nav[@class='gnt_sn']//button"
    FIRST_OPTION_BUTTON = "//div[@class='gnt_pr']//a[@class='gnt_m_he']"   
  
    #**FIRST METHOD BELOW MAY NEED TO BE COMMENTED OUT BECAUSE THIS ELEMENT TENDS TO APPEAR RANDOMLY. ELEMENT APPEARS AS OF 4/30/2024
 
    #CLOSE PROMPT BUTTON METHOD - Code for a method that called the location of the close prompt button from the above locators variables
    def getClosePromptButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.CLOSE_PROMPT_BUTTON)

    #Code for a method to call the CLOSE PROMPT BUTTON METHOD and then clicks on the link
    def enterClosePromptButtonLocation(self):
        self.getClosePromptButtonLocation().click()

    #U.S. PAGE METHOD - Code for a method that called the location of the u.s. page from the above locators variables
    def getUSPageLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.US_PAGE)

    #Code for a method to call the U.S. PAGE METHOD and then clicks on the link
    def enterUSPageLocation(self):
        self.getUSPageLocation().click()

    #POLITICS BUTTON METHOD - Code for a method that called the location of the politics button from the above locators variables
    def getPoliticsButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.POLITICS_BUTTON)

    #Code for a method to call the POLITICS BUTTON METHOD and then clicks on the link
    def enterPoliticsButtonLocation(self):
        self.getPoliticsButtonLocation().click()
        
    #ELECTIONS BUTTON METHOD - Code for a method that called the location of the elections button from the above locators variables
    def getElectionsButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.ELECTIONS_BUTTON)

    #Code for a method to call the ELECTIONS BUTTON METHOD and then clicks on the link
    def enterElectionsButtonLocation(self):
        self.getElectionsButtonLocation().click()
        
    #FOLLOW THE CANDIDATES BUTTON METHOD - Code for a method that called the location of the follow the candidates button from the above locators variables
    def getFollowTheCandidatesButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.FOLLOW_THE_CANDIDATES_BUTTON)

    #Code for a method to call the FOLLOW THE CANDIDATES BUTTON METHOD and then clicks on the link
    def enterFollowTheCandidatesButtonLocation(self):
        self.getFollowTheCandidatesButtonLocation().click()        
    
    #JOE BIDEN BUTTON METHOD - Code for a method that called the location of the joe biden button from the above locators variables
    def getJoeBidenButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.JOE_BIDEN_BUTTON)
    
    #NAVIGATION BUTTON METHOD - Code for a method that called the location of the navigation button from the above locators variables
    def getNavigationButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.DROP_DOWN_BUTTON)

    #Code for a method to call the NAVIGATION BUTTON METHOD and then clicks on the link
    def enterNavigationButtonLocation(self):
        self.getNavigationButtonLocation().click()

    #Code for a method to call the JOE BIDEN BUTTON METHOD and then clicks on the link
    def enterJoeBidenButtonLocation(self):
        self.getJoeBidenButtonLocation().click()
        
    #ROBERT F. KENNEDY JR. BUTTON METHOD - Code for a method that called the location of the robert f. kennedy jr. button from the above locators variables
    def getRobertFKennedyJRButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.ROBERT_F_KENNEDY_JR_BUTTON)

    #Code for a method to call the ROBERT F. KENNEDY JR. BUTTON METHOD and then clicks on the link
    def enterRobertFKennedyJRButtonLocation(self):
        self.getRobertFKennedyJRButtonLocation().click()
        
    #JILL STEIN BUTTON METHOD - Code for a method that called the location of the jill stein button from the above locators variables
    def getJillSteinButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.JILL_STEIN_BUTTON)

    #Code for a method to call the JILL STEIN BUTTON METHOD and then clicks on the link
    def enterJillSteinButtonLocation(self):
        self.getJillSteinButtonLocation().click()
        
    #DONALD TRUMP BUTTON METHOD - Code for a method that called the location of the donald trump button from the above locators variables
    def getDonaldTrumpButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.DONALD_TRUMP_BUTTON)

    #Code for a method to call the DONALD TRUMP BUTTON METHOD and then clicks on the link
    def enterDonaldTrumpButtonLocation(self):
        self.getDonaldTrumpButtonLocation().click()
        
    #CORNEL WEST BUTTON METHOD - Code for a method that called the location of the cornel west button from the above locators variables
    def getCornelWestButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.CORNEL_WEST_BUTTON)

    #Code for a method to call the CORNEL WEST BUTTON METHOD and then clicks on the link
    def enterCornelWestButtonLocation(self):
        self.getCornelWestButtonLocation().click()
        
    #MARIANNE WILLIAMSON BUTTON METHOD - Code for a method that called the location of the marianne williamson button from the above locators variables
    def getMarianneWilliamsonButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.MARIANNE_WILLIAMSON_BUTTON)

    #Code for a method to call the MARIANNE WILLIAMSON BUTTON METHOD and then clicks on the link
    def enterMarianneWilliamsonButtonLocation(self):
        self.getMarianneWilliamsonButtonLocation().click()
    
    #FIRST OPTION BUTTON METHOD - Code for a method that called the location of the first option button from the above locators variables
    def getFirstOptionButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.FIRST_OPTION_BUTTON)

    #Code for a method to call the FIRST OPTION BUTTON METHOD and then clicks on the link
    def enterFirstOptionButtonLocation(self):
        self.getFirstOptionButtonLocation().click()