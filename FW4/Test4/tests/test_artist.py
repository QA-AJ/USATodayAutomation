import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.artists_page import ForArtist

#@pytest.mark.skip(reason="test case confirmed working")
@pytest.mark.usefixtures("setup")
class TestArtistAndVerifyFilter():
    def test_artist(self):
        ap = ForArtist(self.driver, self.wait)
        
        #close out the cookies prompt
        ap.cookies()

        #click on the for the artists option under the company category
        ap.art()
        
        #Scroll to the bottom of the webpage
        ap.scroll()

        #click on See All FAQs
        ap.faq()

        #search for Managing your artist profile option
        ap.manage("Managing your artist profile")

        #click on the get access to spotify for artists option
        ap.access()

        


