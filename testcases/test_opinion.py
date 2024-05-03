#Imports needed for the code to work
import pytest
from pages.opinion_page import LaunchPage

#Code to create the applicable page for externalizing in other test cases. Super code externalizes the Base Driver so the operator can use the methods from that particular file
@pytest.mark.usefixtures("setup")
class TestOpinionAndVerify():
    def test_opinion(self):
        
        #Accesses the conftest file to call the webdriver code
        op = LaunchPage(self.driver)
        
        #**FIRST CODE ACTION BELOW MAY NEED TO BE COMMENTED OUT BECAUSE THIS ELEMENT TENDS TO APPEAR RANDOMLY. ELEMENT APPEARS AS OF 4/30/2024
        
        #Code to close the prompt that appears when accessing usatoday.com
        op.enterClosePromptButtonLocation()
        
        #Code to enter the Opinion page
        op.enterOpinionPageLocation()
        
        #Code to click on the Meet The Opinion Team page
        op.enterMeetTheOpinionTeamButtonLocation()
        
        #Code to scroll down to and click on Rex Huppke
        op.enterScrollDownToAndClickOnRexHuppkeButtonLocation()