import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.support_page import SupportPage

@pytest.mark.skip(reason="test case confirmed not working")
@pytest.mark.usefixtures("setup")
class TestSupportAndVerifyFilter():
    def test_support(self):
        sup = SupportPage(self.driver, self.wait)

        #click on the support option at the top of the screen
        sup.support()
        
        
        sup.search("Music")

        
        #sup.music()

        
        #sup.helpful()


        #sup.hacked()


        #sup.no()