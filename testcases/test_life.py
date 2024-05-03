#Imports needed for the code to work
import pytest
from pages.life_page import LaunchPage

#Code to create the applicable page for externalizing in other test cases. Super code externalizes the Base Driver so the operator can use the methods from that particular file
@pytest.mark.usefixtures("setup")
class TestLifeAndVerify():
    def test_life(self):
        
        #Accesses the conftest file to call the webdriver code
        lfp = LaunchPage(self.driver)
        
        #**FIRST CODE ACTION BELOW MAY NEED TO BE COMMENTED OUT BECAUSE THIS ELEMENT TENDS TO APPEAR RANDOMLY. ELEMENT APPEARS AS OF 4/30/2024
        
        #Code to close the prompt that appears when accessing usatoday.com
        lfp.enterClosePromptButtonLocation()
        
        #Code to enter the Life page
        lfp.enterLifePageLocation()
        
        #Code to click on the Horoscopes page
        lfp.enterHoroscopesButtonLocation()
        
        #Code to enter the Daily page
        lfp.enterDailyButtonLocation()
        
        #Code to enter the Aries Daily Page
        lfp.enterAriesDailyButtonLocation()
        
        #Code to enter the Taurus Daily Page
        lfp.enterTaurusDailyButtonLocation()
        
        #Code to enter the Gemini Daily Page
        lfp.enterGeminiDailyButtonLocation()
        
        #Code to enter the Cancer Daily Page
        lfp.enterCancerDailyButtonLocation()
        
        #Code to enter the Leo Daily Page
        lfp.enterLeoDailyButtonLocation()
        
        #Code to enter the Virgo Daily Page
        lfp.enterVirgoDailyButtonLocation()
        
        #Code to enter the Libra Daily Page
        lfp.enterLibraDailyButtonLocation()
        
        #Code to enter the Scorpio Daily Page
        lfp.enterScorpioDailyButtonLocation()
        
        #Code to enter the Sagittarius Daily Page
        lfp.enterSagittariusDailyButtonLocation()
        
        #Code to enter the Capricorn Daily Page
        lfp.enterCapricornDailyButtonLocation()
        
        #Code to enter the Aquarius Daily Page
        lfp.enterAquariusDailyButtonLocation()
        
        #Code to enter the Pisces Daily Page
        lfp.enterPiscesDailyButtonLocation()
        
        #Code to enter the Aries Monthly Page
        lfp.enterAriesMonthlyButtonLocation()
        
        #Code to enter the Taurus Monthly Page
        lfp.enterTaurusMonthlyButtonLocation()
        
        #Code to enter the Gemini Monthly Page
        lfp.enterGeminiMonthlyButtonLocation()
        
        #Code to enter the Cancer Monthly Page
        lfp.enterCancerMonthlyButtonLocation()
        
        #Code to enter the Leo Monthly Page
        lfp.enterLeoMonthlyButtonLocation()
        
        #Code to enter the Virgo Monthly Page
        lfp.enterVirgoMonthlyButtonLocation()
        
        #Code to enter the Libra Monthly Page
        lfp.enterLibraMonthlyButtonLocation()
        
        #Code to enter the Scorpio Monthly Page
        lfp.enterScorpioMonthlyButtonLocation()
        
        #Code to enter the Sagittarius Monthly Page
        lfp.enterSagittariusMonthlyButtonLocation()
        
        #Code to enter the Capricorn Monthly Page
        lfp.enterCapricornMonthlyButtonLocation()
        
        #Code to enter the Aquarius Monthly Page
        lfp.enterAquariusMonthlyButtonLocation()
        
        #Code to enter the Psychic Page
        lfp.enterPsychicButtonLocation()