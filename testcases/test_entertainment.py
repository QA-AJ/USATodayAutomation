#Imports needed for the code to work
import pytest
from pages.entertainment_page import LaunchPage

#Code to create the applicable page for externalizing in other test cases. Super code externalizes the Base Driver so the operator can use the methods from that particular file
@pytest.mark.usefixtures("setup")
class TestEntertainmentAndVerify():
    def test_entertainment(self):
        
        #Accesses the conftest file to call the webdriver code
        ep = LaunchPage(self.driver)
        
        #**FIRST CODE ACTION BELOW MAY NEED TO BE COMMENTED OUT BECAUSE THIS ELEMENT TENDS TO APPEAR RANDOMLY. ELEMENT APPEARS AS OF 4/30/2024
        
        #Code to click on the X to close the prompt
        ep.enterClosePromptButtonLocation()
        
        #Code to click on the Entertainment link
        ep.enterEntertainmentPageLocation()

        #Code to click on the Books Drop Down link
        ep.enterBooksDropdownLocation()

        #Code to click on the Best-selling Booklist link
        ep.enterBestsellingBooklistButtonLocation()

        #Code to click on the Bookstore Map link
        ep.enterBookstoreMapButtonLocation()

        #Code to click on the About The List link
        ep.enterAboutTheListButtonLocation()

        #Code to click on the Booklist FAQs link
        ep.enterBooklistFaqsButtonLocation()

        #Code to click on the Subscription Boxes link
        ep.enterSubscriptionBoxesButtonLocation()

        #Code to click on the Mystery Boxes link
        ep.enterMysteryBoxesButtonLocation()

        #Code to click on the Booklist link
        ep.enterBooklistReturnButtonLocation()

        #Code to click on the Download List link
        ep.enterDownloadListButtonLocation()