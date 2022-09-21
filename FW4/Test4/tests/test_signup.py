import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.signup_page import SignUpPage

@pytest.mark.skip(reason="test case confirmed not working")
@pytest.mark.usefixtures("setup")
class TestSignUpAndVerifyFilter():
    def test_signup(self):
        su = SignUpPage(self.driver, self.wait)

        #click on the Sign Up option
        su.signup()

        #close the cookies prompt
        su.cookies()

        #click on the email option and enter the information
        su.address("testaccountbaby1@gmail.com")

        #click on the confirm email option and reenter the same email
        su.confirmaddress("testaccountbaby1@gmail.com")
        
        #click on the password option and enter the information
        su.password("Th3B!gge$tGuy-!")
        
        #click on the username option and enter the information
        su.username("TheRealInternationalWonder15")
        
        #click on the month option and pick a year
        su.month("F")

        #click on the Day option and enter the information
        su.day("17")

        #click on the Year option and enter the information
        su.year("1970")

        #click on the male gender option
        su.gender()

        #click on the captcha and confirm the "I'm not a robot" option
        su.captcha()

        #click on the sign up option for the second time
        su.truesignup()