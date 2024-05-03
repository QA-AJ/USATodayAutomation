#Imports needed for the code to work
import pytest
from pages.money_page import LaunchPage

#Code to create the applicable page for externalizing in other test cases. Super code externalizes the Base Driver so the operator can use the methods from that particular file
@pytest.mark.usefixtures("setup")
class TestMoneyAndVerify():
    def test_money(self):
        
        #Accesses the conftest file to call the webdriver code
        mp = LaunchPage(self.driver)
        
        #**FIRST CODE ACTION BELOW MAY NEED TO BE COMMENTED OUT BECAUSE THIS ELEMENT TENDS TO APPEAR RANDOMLY. ELEMENT APPEARS AS OF 4/30/2024        
        
        #Code to close the prompt that appears when accessing usatoday.com
        mp.enterClosePromptButtonLocation()
        
        #Code to enter the Money page
        mp.enterMoneyPageLocation()
        
        #Code to enter the Lottery page
        mp.enterLotteryButtonLocation()
        
        #Code to enter the Powerball page
        mp.enterPowerballButtonLocation()
        
        #Code to enter the Mega Millions page
        mp.enterMegaMillionsButtonLocation()
        
        #Code to enter the State Lottery Results page
        mp.enterStateLotteryResultsButtonLocation()

        #Code to enter the Arizona page
        mp.enterArizonaButtonLocation()