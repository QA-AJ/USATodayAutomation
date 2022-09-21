import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.focus_page import ProfilePage

#@pytest.mark.skip(reason="test case confirmed working")
@pytest.mark.usefixtures("setup")
class TestFocusAndVerifyFilter():
    def test_focus(self):
        fp = ProfilePage(self.driver, self.wait)
        
        #close out the cookies prompt
        fp.cookies()
        
        #click on the see all option for the focus category
        fp.screen()
        
        #click on first option
        fp.option()
        
        #click on first song option
        fp.first()

        #click on play
        fp.play()