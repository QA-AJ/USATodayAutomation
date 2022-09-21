import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.records_page import ForRecord

#@pytest.mark.skip(reason="test case confirmed working")
@pytest.mark.usefixtures("setup")
class TestRecordsAndVerifyFilter():
    def test_record(self):
        rp = ForRecord(self.driver, self.wait)

        #scroll down the home webpage
        rp.scroll()

        #close out the cookies prompt
        rp.cookies()

        #click on the for the record option under the company category
        rp.record()

        #click on the first available option in the upper right corner
        rp.first()

        #click on the share option
        rp.share()

        #share it to LinkedIn
        rp.link()
