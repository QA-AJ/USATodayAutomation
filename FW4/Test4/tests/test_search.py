import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.search_page import SearchPage

#@pytest.mark.skip(reason="test case confirmed working")
@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilter():
    def test_search(self):
        sb = SearchPage(self.driver, self.wait)
        
        #click on the Search Bar option from the home screen
        sb.searching()

        #search for "God-Blo"
        sb.name("God-Blo")
        
        #click on the The Blog for the Gods podcast
        sb.blog()
        
        #click on Level 11 episode
        sb.episode()
        
        #click on play
        sb.play()