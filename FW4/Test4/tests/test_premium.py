import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.premium_page import PremiumPage

@pytest.mark.skip(reason="test case confirmed not working")
@pytest.mark.usefixtures("setup")
class TestPremiumAndVerifyFilter():
    def test_premium(self):
        pp = PremiumPage(self.driver, self.wait)

        #click on the premium option at the top of the screen
        pp.prem()

        #pp.cookies()

        
        #pp.views()  


        #pp.scroll()


        #pp.individual()
