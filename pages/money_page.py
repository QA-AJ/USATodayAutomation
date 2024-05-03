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
    MONEY_PAGE = "(//nav[@class='gnt_n_mn']//a[@class='gnt_n_mn_l gnt_n_mn_ce'])[5]"
    LOTTERY_BUTTON = "(//a[@class='gnt_sn_a gnt_sn_a_w'])[5]"
    POWERBALL_BUTTON = "//div[@class='B-eRu5__B-eRu5']//a[@class='R63xpd__R63xpd A0dst3__A0dst3']"
    MEGA_MILLIONS_BUTTON = "//div[@class='B-eRu5__B-eRu5']//a[@class='R63xpd__R63xpd v8J-al__v8J-al']"
    STATE_LOTTERY_RESULTS_BUTTON = "//div[@class='B-eRu5__B-eRu5']//button[@class='R63xpd__R63xpd Zj6hTG__Zj6hTG']"
    ARIZON_BUTTON = "//div[@class='zxLFBH__zxLFBH DmO-fA__DmO-fA']//li[@class='NjzggM__NjzggM']"
  
    #**FIRST METHOD BELOW MAY NEED TO BE COMMENTED OUT BECAUSE THIS ELEMENT TENDS TO APPEAR RANDOMLY. ELEMENT APPEARS AS OF 4/30/2024
    
    #CLOSE PROMPT BUTTON METHOD - Code for a method that called the location of the close prompt button from the above locators variables
    def getClosePromptButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.CLOSE_PROMPT_BUTTON)

    #Code for a method to call the SUBSCRIBE PAGE METHOD and then clicks on the link
    def enterClosePromptButtonLocation(self):
        self.getClosePromptButtonLocation().click()

    #MONEY PAGE METHOD - Code for a method that called the location of the money page from the above locators variables
    def getMoneyPageLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.MONEY_PAGE)

    #Code for a method to call the MONEY PAGE METHOD and then clicks on the link
    def enterMoneyPageLocation(self):
        self.getMoneyPageLocation().click()

    #LOTTERY BUTTON METHOD - Code for a method that called the location of the lottery button from the above locators variables
    def getLotteryButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.LOTTERY_BUTTON)

    #Code for a method to call the LOTTERY BUTTON METHOD and then clicks on the link
    def enterLotteryButtonLocation(self):
        sleep(2)
        self.getLotteryButtonLocation().click()
 
    #POWERBALL BUTTON METHOD - Code for a method that called the location of the powerball button from the above locators variables
    def getPowerballButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.POWERBALL_BUTTON)

    #Code for a method to call the POWERBALL BUTTON METHOD and then clicks on the link
    def enterPowerballButtonLocation(self):
        sleep(2)
        self.getPowerballButtonLocation().click()

    #MEGA MILLIONS BUTTON METHOD - Code for a method that called the location of the mega millions button from the above locators variables
    def getMegaMillionsButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.MEGA_MILLIONS_BUTTON)

    #Code for a method to call the MEGA MILLIONS METHOD and then clicks on the link
    def enterMegaMillionsButtonLocation(self):
        sleep(2)
        self.getMegaMillionsButtonLocation().click()    
  
    #STATE LOTTERY RESULTS BUTTON METHOD - Code for a method that called the location of the state lottery results button from the above locators variables
    def getStateLotteryResultsButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.STATE_LOTTERY_RESULTS_BUTTON)

    #Code for a method to call the STATE LOTTERY RESULTS BUTTON METHOD and then clicks on the link
    def enterStateLotteryResultsButtonLocation(self):
        sleep(2)
        self.getStateLotteryResultsButtonLocation().click()
  
    #ARIZONA BUTTON METHOD - Code for a method that called the location of the arizona button from the above locators variables
    def getArizonaButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.ARIZON_BUTTON)

    #Code for a method to call the ARIZONA BUTTON METHOD and then clicks on the link
    def enterArizonaButtonLocation(self):
        sleep(2)
        self.getArizonaButtonLocation().click()