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
    TRAVEL_PAGE = "(//nav[@class='gnt_n_mn']//a[@class='gnt_n_mn_l gnt_n_mn_ce'])[7]"
    TEN_BEST_BUTTON = "//div[@class='gnt_sn_a_w']//button"
    TRAVEL_GUIDES_BUTTON = "(//a[@class='gnt_sn_dd_a'])[2]"
    FIRST_OPTION_BUTTON = "(//section[@class='show-for-medium-up']//div[@class='small-12 medium-12 large-6 columns add-margin-bottom'])[1]"
    STAY_BUTTON = "//div[@class='row']//dd[@class='w-20 panel-button-2']"
    EAT_BUTTON = "//div[@class='row']//dd[@class='w-20 panel-button-3']"
    PARTY_BUTTON = "//div[@class='row']//dd[@class='w-20 panel-button-4']"
    SHOP_BUTTON = "//div[@class='row']//dd[@class='w-20 panel-button-5']"
    FACEBOOK_BUTTON = "//ul[@class='social-menu menu-top']//a[@id='facebook-menu']"  
  
    #**FIRST METHOD BELOW MAY NEED TO BE COMMENTED OUT BECAUSE THIS ELEMENT TENDS TO APPEAR RANDOMLY. ELEMENT APPEARS AS OF 4/30/2024
    
    #CLOSE PROMPT BUTTON METHOD - Code for a method that called the location of the close prompt button from the above locators variables
    def getClosePromptButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.CLOSE_PROMPT_BUTTON)

    #Code for a method to call the SUBSCRIBE PAGE METHOD and then clicks on the link
    def enterClosePromptButtonLocation(self):
        self.getClosePromptButtonLocation().click()

    #TRAVEL PAGE METHOD - Code for a method that called the location of the travel page from the above locators variables
    def getTravelPageLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.TRAVEL_PAGE)

    #Code for a method to call the TRAVEL PAGE METHOD and then clicks on the link
    def enterTravelPageLocation(self):
        self.getTravelPageLocation().click()

    #10BEST BUTTON METHOD - Code for a method that called the location of the 10best button from the above locators variables
    def get10BestButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.TEN_BEST_BUTTON)

    #Code for a method to call the 10BEST BUTTON METHOD and then clicks on the link
    def enter10BestButtonLocation(self):
        self.get10BestButtonLocation().click()
        
    #TRAVEL GUIDES BUTTON METHOD - Code for a method that called the location of the travel guides button from the above locators variables
    def getTravelGuidesButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.TRAVEL_GUIDES_BUTTON)

    #Code for a method to call the TRAVEL GUIDES BUTTON METHOD and then clicks on the link
    def enterTravelGuidesButtonLocation(self):
        self.getTravelGuidesButtonLocation().click()

    #FIRST OPTION BUTTON METHOD - Code for a method that called the location of the first option button from the above locators variables
    def getFirstOptionButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.FIRST_OPTION_BUTTON)

    #Code for a method to call the FIRST OPTION BUTTON METHOD and then clicks on the link
    def enterFirstOptionsButtonLocation(self):
        sleep(2)
        self.getFirstOptionButtonLocation().click()
        
    #STAY BUTTON METHOD - Code for a method that called the location of the stay button from the above locators variables
    def getStayButtonLocation(self):
        return self.scroll_to_element_and_click(By.XPATH, self.STAY_BUTTON)
        
    #EAT BUTTON METHOD - Code for a method that called the location of the eat button from the above locators variables
    def getEatButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.EAT_BUTTON)

    #Code for a method to call the EAT BUTTON METHOD and then clicks on the link
    def enterEatButtonLocation(self):
        sleep(2)
        self.getEatButtonLocation().click()
        
    #PARTY BUTTON METHOD - Code for a method that called the location of the party button from the above locators variables
    def getPartyButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.PARTY_BUTTON)

    #Code for a method to call the PARTY BUTTON METHOD and then clicks on the link
    def enterPartyButtonLocation(self):
        sleep(2)
        self.getPartyButtonLocation().click()
        
    #SHOP BUTTON METHOD - Code for a method that called the location of the shop button from the above locators variables
    def getShopButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.SHOP_BUTTON)

    #Code for a method to call the SHOP BUTTON METHOD and then clicks on the link
    def enterShopButtonLocation(self):
        sleep(2)
        self.getShopButtonLocation().click()
        
    #FACEBOOK BUTTON METHOD - Code for a method that called the location of the facebook button from the above locators variables
    def getFacebookButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.FACEBOOK_BUTTON)

    #Code for a method to call the FACEBOOK BUTTON METHOD and then clicks on the link
    def enterFacebookButtonLocation(self):
        self.getFacebookButtonLocation().click()