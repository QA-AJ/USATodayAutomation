#Imports needed for the code to work
import pytest
from pages.createaccount_page import LaunchPage

#Code to create the applicable page for externalizing in other test cases. Super code externalizes the Base Driver so the operator can use the methods from that particular file
@pytest.mark.usefixtures("setup")
class TestCreateAccountAndVerify():
    def test_createaccount(self):
        
        #Accesses the conftest file to call the webdriver code
        sip = LaunchPage(self.driver)
        
        #**FIRST CODE ACTION BELOW MAY NEED TO BE COMMENTED OUT BECAUSE THIS ELEMENT TENDS TO APPEAR RANDOMLY. ELEMENT APPEARS AS OF 4/30/2024
        
        #Code to close the prompt that appears when accessing usatoday.com
        sip.enterClosePromptButtonLocation()
        
        #Code to enter the sign in drop down
        sip.enterSigninDropdownLocation()
        
        #Code to enter the create account page
        sip.enterCreatAccountButtonLocation()
        
        #Code to enter text into the text fields
        sip.textFields("Terry", "Ter", "TerryT@GGG.org", "1234abcd!@#$", "1234abcd!@#$")
        
        #code to click on the create account button to complete the process.
        sip.enterSubmitButtonLocation()