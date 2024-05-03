#Imports needed for the code to work
import pytest
from pages.sports_page import LaunchPage

#Code to create the applicable page for externalizing in other test cases. Super code externalizes the Base Driver so the operator can use the methods from that particular file
@pytest.mark.usefixtures("setup")
class TestSportsAndVerify():
    def test_sports(self):
        
        #Accesses the conftest file to call the webdriver code
        spt = LaunchPage(self.driver)
        
        #**FIRST CODE ACTION BELOW MAY NEED TO BE COMMENTED OUT BECAUSE THIS ELEMENT TENDS TO APPEAR RANDOMLY. ELEMENT APPEARS AS OF 4/30/2024
        
        #Code to close the prompt that appears when accessing usatoday.com
        spt.enterClosePromptButtonLocation()
        
        #Code to enter the Sports page
        spt.enterSportsPageLocation()
        
        #Code to click on the NFL Draft Hub page
        spt.enterNFLDraftHubButtonLocation()
        
        #Code to enter the Draft Tracker page
        spt.enterDraftTrackerButtonLocation()
        
        #Code to enter the Mock Drafts page
        spt.enterMockDraftsButtonLocation()
        
        #Code to enter the At the Draft page
        spt.enterAtTheDraftButtonLocation()