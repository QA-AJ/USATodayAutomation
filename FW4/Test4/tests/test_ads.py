import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.ads_page import ForAds

@pytest.mark.skip(reason="test case confirmed not working")
@pytest.mark.usefixtures("setup")
class TestAdvertsAndVerifyFilter():
    def test_ad(self):
        adp = ForAds(self.driver, self.wait)
        
        #scroll down the home webpage
        adp.scroll()

        #close out the cookies prompt
        adp.cookies()

        #click on advertising under the communities category
        adp.advert()


        adp.close()

        #scroll to the bottom of the page
        adp.bottom()


        adp.first()



        adp.second()



        adp.fname("Johnny")



        adp.lname("Smith")



        adp.email("myemail2000@gmail.com")



        adp.company("advertistments 4 all")