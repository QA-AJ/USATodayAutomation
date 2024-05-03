#Imports needed for the code to work
import pytest
from pages.us_page import LaunchPage

#Code to create the applicable page for externalizing in other test cases. Super code externalizes the Base Driver so the operator can use the methods from that particular file
@pytest.mark.usefixtures("setup")
class TestUsAndVerify():
    def test_us(self):
        
        #Accesses the conftest file to call the webdriver code
        usp = LaunchPage(self.driver)
        
        #**FIRST CODE ACTION BELOW MAY NEED TO BE COMMENTED OUT BECAUSE THIS ELEMENT TENDS TO APPEAR RANDOMLY. ELEMENT APPEARS AS OF 4/30/2024
        
        #Code to close the prompt that appears when accessing usatoday.com
        usp.enterClosePromptButtonLocation()
        
        #Code to enter the US page
        usp.enterUSPageLocation()
        
        #Code to click on the politics drop down
        usp.enterPoliticsButtonLocation()
        
        #Code to enter the Elections page
        usp.enterElectionsButtonLocation()
        
        #Code to click on the Follow The Candidates drop down
        usp.enterFollowTheCandidatesButtonLocation()
        
        #Code to click on one of the candidates
        usp.enterJoeBidenButtonLocation()
        
        #Code to click on the navigation drop down
        usp.enterNavigationButtonLocation()
        
        #Code to click on one of the candidates
        usp.enterRobertFKennedyJRButtonLocation()
        
        #Code to click on the navigation drop down
        usp.enterNavigationButtonLocation()
        
        #Code to click on one of the candidates
        usp.enterJillSteinButtonLocation()
        
        #Code to click on the navigation drop down
        usp.enterNavigationButtonLocation()
        
        #Code to click on one of the candidates
        usp.enterDonaldTrumpButtonLocation()
        
        #Code to click on the navigation drop down
        usp.enterNavigationButtonLocation()
        
        #Code to click on one of the candidates
        usp.enterCornelWestButtonLocation()
        
        #Code to click on the navigation drop down
        usp.enterNavigationButtonLocation()
        
        #Code to click on one of the candidates
        usp.enterMarianneWilliamsonButtonLocation()

        #Code to click on the navigation drop down
        usp.enterNavigationButtonLocation()
        
        #Code to click on the first option
        usp.enterFirstOptionButtonLocation()