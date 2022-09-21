import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.invest_page import Investing

#@pytest.mark.skip(reason="test case confirmed working")
@pytest.mark.usefixtures("setup")
class TestInvestingAndVerifyFilter():
    def test_invest(self):
        iv = Investing(self.driver, self.wait)

        #close out the cookies prompt
        iv.cookies()

        #click on investors under the communities category
        iv.vesting()

        #click on the view all option
        iv.all()

        #click on the first option
        iv.quarter()
