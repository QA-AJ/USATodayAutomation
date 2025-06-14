#Imports needed for the code to work
import pytest
from pages.travel_page import LaunchPage

#Code to create the applicable page for externalizing in other test cases. Super code externalizes the Base Driver so the operator can use the methods from that particular file
@pytest.mark.usefixtures("setup")
class TestsTravelAndVerify():
    def test_travel(self):
        
        #Accesses the conftest file to call the webdriver code
        tp = LaunchPage(self.driver)
        
        #**FIRST CODE ACTION BELOW MAY NEED TO BE COMMENTED OUT BECAUSE THIS ELEMENT TENDS TO APPEAR RANDOMLY. ELEMENT APPEARS AS OF 4/30/2024
        
        #Code to click on the X to close the prompt
        tp.enterClosePromptButtonLocation()
        
        #Code to click on the travel link
        tp.enterTravelPageLocation()
        
        #Code to click on the 10Best link
        tp.enter10BestButtonLocation()
        
        #Code to click on the travel Guides link
        tp.enterTravelGuidesButtonLocation()

        #Code to click on the first option on the left for places
        tp.enterFirstOptionsButtonLocation()
        
        #Code to click on the stay button
        tp.getStayButtonLocation()
        
        #Code to click on the eat button
        tp.enterEatButtonLocation()
        
        #Code to click on the party button
        tp.enterPartyButtonLocation()
        
        #Code to click on the shop button
        tp.enterShopButtonLocation()
        
        #Code to click on the Facebook link
        tp.enterFacebookButtonLocation()