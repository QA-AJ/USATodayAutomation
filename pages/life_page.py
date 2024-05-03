#Imports needed for the code to work
from time import sleep
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver

#Code to create the applicable page for externalizing in other test cases. Super code externalizes the Base Driver so the operator can use the methods from that particular file
class LaunchPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    #**FIRST LOCATOR VARIABLE BELOW MAY NEED TO BE COMMENTED OUT BECAUSE THIS ELEMENT TENDS TO APPEAR RANDOMLY. ELEMENT APPEARS AS OF 4/30/202
        
    #Locator variables. Change these to affect the test case
    CLOSE_PROMPT_BUTTON = "//div[@class='gnt_mol']//button[@class='gnt_mol_xb']"
    LIFE_PAGE = "(//nav[@class='gnt_n_mn']//a[@class='gnt_n_mn_l gnt_n_mn_ce'])[4]"
    HOROSCOPES_BUTTON = "(//a[@class='gnt_sn_a gnt_sn_a_w'])[4]"
    DAILY_BUTTON = "(//div[@id='background']//li)[3]"
    ARIES_DAILY_BUTTON = "(//div[@id='horoscopes']//section)[1]"
    TAURUS_DAILY_BUTTON = "(//div[@id='horoscopes']//li)[1]"
    GEMINI_DAILY_BUTTON = "(//div[@id='horoscopes']//li)[3]"
    CANCER_DAILY_BUTTON = "(//div[@id='horoscopes']//li)[5]"
    LEO_DAILY_BUTTON = "(//div[@id='horoscopes']//li)[7]"
    VIRGO_DAILY_BUTTON = "(//div[@id='horoscopes']//li)[9]"
    LIBRA_DAILY_BUTTON = "(//div[@id='horoscopes']//li)[11]"
    SCORPIO_DAILY_BUTTON = "(//div[@id='horoscopes']//li)[13]"
    SAGITTARIUS_DAILY_BUTTON = "(//div[@id='horoscopes']//li)[15]"
    CAPRICORN_DAILY_BUTTON = "(//div[@id='horoscopes']//li)[17]"
    AQUARIUS_DAILY_BUTTON = "(//div[@id='horoscopes']//li)[19]"
    PISCES_DAILY_BUTTON = "(//div[@id='horoscopes']//li)[21]"
    ARIES_MONTHLY_BUTTON = "(//div[@id='horoscopes']//li)[2]"
    TAURUS_MONTHLY_BUTTON = "(//div[@id='horoscopes']//li)[4]"
    GEMINI_MONTHLY_BUTTON = "(//div[@id='horoscopes']//li)[6]"
    CANCER_MONTHLY_BUTTON = "(//div[@id='horoscopes']//li)[8]"
    LEO_MONTHLY_BUTTON = "(//div[@id='horoscopes']//li)[10]"
    VIRGO_MONTHLY_BUTTON = "(//div[@id='horoscopes']//li)[12]"
    LIBRA_MONTHLY_BUTTON = "(//div[@id='horoscopes']//li)[14]"
    SCORPIO_MONTHLY_BUTTON = "(//div[@id='horoscopes']//li)[16]"
    SAGITTARIUS_MONTHLY_BUTTON = "(//div[@id='horoscopes']//li)[18]"
    CAPRICORN_MONTHLY_BUTTON = "(//div[@id='horoscopes']//li)[20]"
    AQUARIUS_MONTHLY_BUTTON = "(//div[@id='horoscopes']//li)[22]"
    PSYCHIC_BUTTON = "//div[@class='cardcontainer']//a[@class='card']"
  
    #**FIRST METHOD BELOW MAY NEED TO BE COMMENTED OUT BECAUSE THIS ELEMENT TENDS TO APPEAR RANDOMLY. ELEMENT APPEARS AS OF 4/30/2024
    
    #CLOSE PROMPT BUTTON METHOD - Code for a method that called the location of the close prompt button from the above locators variables
    def getClosePromptButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.CLOSE_PROMPT_BUTTON)

    #Code for a method to call the SUBSCRIBE PAGE METHOD and then clicks on the link
    def enterClosePromptButtonLocation(self):
        self.getClosePromptButtonLocation().click()

    #LIFE PAGE METHOD - Code for a method that called the location of the life page from the above locators variables
    def getLifePageLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.LIFE_PAGE)

    #Code for a method to call the LIFE PAGE METHOD and then clicks on the link
    def enterLifePageLocation(self):
        self.getLifePageLocation().click()

    #HOROSCOPES BUTTON METHOD - Code for a method that called the location of the horoscopes button from the above locators variables
    def getHoroscopesButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.HOROSCOPES_BUTTON)

    #Code for a method to call the HOROSCOPES BUTTON METHOD and then clicks on the link
    def enterHoroscopesButtonLocation(self):
        self.getHoroscopesButtonLocation().click()
        
    #DAILY BUTTON METHOD - Code for a method that called the location of the daily guides button from the above locators variables
    def getDailyButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.DAILY_BUTTON)

    #Code for a method to call the DAILY BUTTON METHOD and then clicks on the link
    def enterDailyButtonLocation(self):
        self.getDailyButtonLocation().click()

    #ARIES DAILY BUTTON METHOD - Code for a method that called the location of the aries daily button from the above locators variables
    def getAriesDailyButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.ARIES_DAILY_BUTTON)

    #Code for a method to call the ARIES DAILY BUTTON METHOD and then clicks on the link
    def enterAriesDailyButtonLocation(self):
        self.getAriesDailyButtonLocation().click()

    #TAURUS DAILY BUTTON METHOD - Code for a method that called the location of the taurus daily button from the above locators variables
    def getTaurusDailyButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.TAURUS_DAILY_BUTTON)

    #Code for a method to call the TAURUS DAILY BUTTON METHOD and then clicks on the link
    def enterTaurusDailyButtonLocation(self):
        self.getTaurusDailyButtonLocation().click()

    #GEMINI DAILY BUTTON METHOD - Code for a method that called the location of the gemini daily button from the above locators variables
    def getGeminiDailyButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.GEMINI_DAILY_BUTTON)

    #Code for a method to call the GEMINI DAILY BUTTON METHOD and then clicks on the link
    def enterGeminiDailyButtonLocation(self):
        self.getGeminiDailyButtonLocation().click()

    #CANCER DAILY BUTTON METHOD - Code for a method that called the location of the cancer daily button from the above locators variables
    def getCancerDailyButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.CANCER_DAILY_BUTTON)

    #Code for a method to call the CANCER DAILY BUTTON METHOD and then clicks on the link
    def enterCancerDailyButtonLocation(self):
        self.getCancerDailyButtonLocation().click()

    #LEO DAILY BUTTON METHOD - Code for a method that called the location of the leo daily button from the above locators variables
    def getLeoDailyButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.LEO_DAILY_BUTTON)

    #Code for a method to call the LEO DAILY BUTTON METHOD and then clicks on the link
    def enterLeoDailyButtonLocation(self):
        self.getLeoDailyButtonLocation().click()

    #VIRGO DAILY BUTTON METHOD - Code for a method that called the location of the virgo daily button from the above locators variables
    def getVirgoDailyButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.VIRGO_DAILY_BUTTON)

    #Code for a method to call the VIRGO DAILY BUTTON METHOD and then clicks on the link
    def enterVirgoDailyButtonLocation(self):
        self.getVirgoDailyButtonLocation().click()

    #LIBRA DAILY BUTTON METHOD - Code for a method that called the location of the libra daily button from the above locators variables
    def getLibraDailyButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.LIBRA_DAILY_BUTTON)

    #Code for a method to call the LIBRA DAILY BUTTON METHOD and then clicks on the link
    def enterLibraDailyButtonLocation(self):
        self.getLibraDailyButtonLocation().click()

    #SCORPIO DAILY BUTTON METHOD - Code for a method that called the location of the scorpio daily button from the above locators variables
    def getScorpioDailyButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.SCORPIO_DAILY_BUTTON)

    #Code for a method to call the SCORPIO DAILY BUTTON METHOD and then clicks on the link
    def enterScorpioDailyButtonLocation(self):
        self.getScorpioDailyButtonLocation().click()

    #SAGITTARIUS DAILY BUTTON METHOD - Code for a method that called the location of the sagittarius daily button from the above locators variables
    def getSagittariusDailyButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.SAGITTARIUS_DAILY_BUTTON)

    #Code for a method to call the SAGITTARIUS DAILY BUTTON METHOD and then clicks on the link
    def enterSagittariusDailyButtonLocation(self):
        self.getSagittariusDailyButtonLocation().click()

    #CAPRICORN DAILY BUTTON METHOD - Code for a method that called the location of the capricorn daily button from the above locators variables
    def getCapricornDailyButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.CAPRICORN_DAILY_BUTTON)

    #Code for a method to call the CAPRICORN DAILY BUTTON METHOD and then clicks on the link
    def enterCapricornDailyButtonLocation(self):
        self.getCapricornDailyButtonLocation().click()

    #AQUARIUS DAILY BUTTON METHOD - Code for a method that called the location of the aquarius daily button from the above locators variables
    def getAquariusDailyButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.AQUARIUS_DAILY_BUTTON)

    #Code for a method to call the AQUARIUS DAILY BUTTON METHOD and then clicks on the link
    def enterAquariusDailyButtonLocation(self):
        self.getAquariusDailyButtonLocation().click()

    #PISCES DAILY BUTTON METHOD - Code for a method that called the location of the pisces daily button from the above locators variables
    def getPiscesDailyButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.PISCES_DAILY_BUTTON)

    #Code for a method to call the PISCES DAILY BUTTON METHOD and then clicks on the link
    def enterPiscesDailyButtonLocation(self):
        self.getPiscesDailyButtonLocation().click()

    #ARIES MONTHLY BUTTON METHOD - Code for a method that called the location of the aries monthly button from the above locators variables
    def getAriesMonthlyButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.ARIES_MONTHLY_BUTTON)

    #Code for a method to call the ARIES MONTHLY BUTTON METHOD and then clicks on the link
    def enterAriesMonthlyButtonLocation(self):
        self.getAriesMonthlyButtonLocation().click()

    #TAURUS MONTHLY BUTTON METHOD - Code for a method that called the location of the taurus monthly button from the above locators variables
    def getTaurusMonthlyButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.TAURUS_MONTHLY_BUTTON)

    #Code for a method to call the TAURUS MONTHLY BUTTON METHOD and then clicks on the link
    def enterTaurusMonthlyButtonLocation(self):
        self.getTaurusMonthlyButtonLocation().click()

    #GEMINI MONTHLY BUTTON METHOD - Code for a method that called the location of the gemini monthly button from the above locators variables
    def getGeminiMonthlyButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.GEMINI_MONTHLY_BUTTON)

    #Code for a method to call the GEMINI MONTHLY BUTTON METHOD and then clicks on the link
    def enterGeminiMonthlyButtonLocation(self):
        self.getGeminiMonthlyButtonLocation().click()

    #CANCER MONTHLY BUTTON METHOD - Code for a method that called the location of the cancer monthly button from the above locators variables
    def getCancerMonthlyButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.CANCER_MONTHLY_BUTTON)

    #Code for a method to call the CANCER MONTHLY BUTTON METHOD and then clicks on the link
    def enterCancerMonthlyButtonLocation(self):
        self.getCancerMonthlyButtonLocation().click()

    #LEO MONTHLY BUTTON METHOD - Code for a method that called the location of the leo monthly button from the above locators variables
    def getLeoMonthlyButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.LEO_MONTHLY_BUTTON)

    #Code for a method to call the LEO MONTHLY BUTTON METHOD and then clicks on the link
    def enterLeoMonthlyButtonLocation(self):
        self.getLeoMonthlyButtonLocation().click()

    #VIRGO MONTHLY BUTTON METHOD - Code for a method that called the location of the virgo monthly button from the above locators variables
    def getVirgoMonthlyButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.VIRGO_MONTHLY_BUTTON)

    #Code for a method to call the VIRGO MONTHLY BUTTON METHOD and then clicks on the link
    def enterVirgoMonthlyButtonLocation(self):
        self.getVirgoMonthlyButtonLocation().click()

    #LIBRA MONTHLY BUTTON METHOD - Code for a method that called the location of the libra monthly button from the above locators variables
    def getLibraMonthlyButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.LIBRA_MONTHLY_BUTTON)

    #Code for a method to call the LIBRA MONTHLY BUTTON METHOD and then clicks on the link
    def enterLibraMonthlyButtonLocation(self):
        self.getLibraMonthlyButtonLocation().click()

    #SCORPIO MONTHLY BUTTON METHOD - Code for a method that called the location of the scorpio monthly button from the above locators variables
    def getScorpioMonthlyButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.SCORPIO_MONTHLY_BUTTON)

    #Code for a method to call the SCORPIO MONTHLY BUTTON METHOD and then clicks on the link
    def enterScorpioMonthlyButtonLocation(self):
        self.getScorpioMonthlyButtonLocation().click()

    #SAGITTARIUS MONTHLY BUTTON METHOD - Code for a method that called the location of the sagittarius monthly button from the above locators variables
    def getSagittariusMonthlyButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.SAGITTARIUS_MONTHLY_BUTTON)

    #Code for a method to call the SAGITTARIUS MONTHLY BUTTON METHOD and then clicks on the link
    def enterSagittariusMonthlyButtonLocation(self):
        self.getSagittariusMonthlyButtonLocation().click()

    #CAPRICORN MONTHLY BUTTON METHOD - Code for a method that called the location of the capricorn monthly button from the above locators variables
    def getCapricornMonthlyButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.CAPRICORN_MONTHLY_BUTTON)

    #Code for a method to call the CAPRICORN MONTHLY BUTTON METHOD and then clicks on the link
    def enterCapricornMonthlyButtonLocation(self):
        self.getCapricornMonthlyButtonLocation().click()

    #AQUARIUS MONTHLY BUTTON METHOD - Code for a method that called the location of the aquarius monthly button from the above locators variables
    def getAquariusMonthlyButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.AQUARIUS_MONTHLY_BUTTON)

    #Code for a method to call the AQUARIUS MONTHLY BUTTON METHOD and then clicks on the link
    def enterAquariusMonthlyButtonLocation(self):
        self.getAquariusMonthlyButtonLocation().click()

    #PSYCHIC BUTTON METHOD - Code for a method that called the location of the psychic button from the above locators variables
    def getPsychicButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.PSYCHIC_BUTTON)

    #Code for a method to call the PSYCHIC BUTTON METHOD and then clicks on the link
    def enterPsychicButtonLocation(self):
        sleep(5)
        self.getPsychicButtonLocation().click()