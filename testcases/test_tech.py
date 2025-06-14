#Imports needed for the code to work
import pytest
from pages.tech_page import LaunchPage

#Code to create the applicable page for externalizing in other test cases. Super code externalizes the Base Driver so the operator can use the methods from that particular file
@pytest.mark.usefixtures("setup")
class TestTechAndVerify():
    def test_tech(self):
        
        #Accesses the conftest file to call the webdriver code
        utp = LaunchPage(self.driver)
        
        #**FIRST CODE ACTION BELOW MAY NEED TO BE COMMENTED OUT BECAUSE THIS ELEMENT TENDS TO APPEAR RANDOMLY. ELEMENT APPEARS AS OF 4/30/2024
        
        #Code to click on the X to close the prompt
        utp.enterClosePromptButtonLocation()
        
        #Code to click on the tech link
        utp.enterTechPageLocation()
        
        #Code to click on the problems solved link
        utp.enterProblemsSolvedButtonLocation()
        
        #Code to click on the first option which is nested inside of a shadow root
        utp.enterShadowRootLocation()