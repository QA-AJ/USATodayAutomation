#Imports needed for the code to work
import pytest
from pages.elections_page import LaunchPage

#Code to create the applicable page for externalizing in other test cases. Super code externalizes the Base Driver so the operator can use the methods from that particular file
@pytest.mark.usefixtures("setup")
class TestElectionsAndVerify():
    def test_elections(self):
        
        #Accesses the conftest file to call the webdriver code
        ele = LaunchPage(self.driver)
        
        #**FIRST CODE ACTION BELOW MAY NEED TO BE COMMENTED OUT BECAUSE THIS ELEMENT TENDS TO APPEAR RANDOMLY. ELEMENT APPEARS AS OF 4/30/2024
        
        #Code to close the prompt that appears when accessing usatoday.com
        ele.enterClosePromptButtonLocation()
        
        #Code to enter the US page
        ele.enterElectionsPageLocation()
        
        #Code to click on the Results page
        ele.enterResultsButtonLocation()
        
        #Code to enter the View Full Republican Race details page
        ele.getViewFullRepublicanRaceDetailsButtonLocation()
        
        #Code to click on Nevada
        ele.getNevadaButtonLocation()
        
        #Code to click on Nevada Election Results
        ele.getRepublicanNevadaElectionResultsButtonLocation()
        
        #Code to click on the navigation drop down
        ele.getClarkCountyButtonLocation()
        
        #Code to click on one of the candidates
        ele.enterDelegateButtonLocation()
        
        #Code to enter the View Full Democratic Race details page
        ele.getViewFullDemocraticRaceDetailsButtonLocation()
        
        #Code to click on Nevada
        ele.getNevadaButtonLocation()
        
        #Code to click on Democratic Nevada Election Results
        ele.getDemocraticNevadaElectionResultsButtonLocation()
        
        #Code to click on the navigation drop down
        ele.getClarkCountyButtonLocation()