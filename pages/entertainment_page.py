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
    ENTERTAINMENT_PAGE = "(//nav[@class='gnt_n_mn']//a[@class='gnt_n_mn_l gnt_n_mn_ce'])[3]"
    BOOKS_DROPDOWN = "(//div[@class='gnt_sn_a_w'])[1]//button"
    BEST_SELLING_BOOKLIST_BUTTON = "//a[@class='gnt_sn_dd_a']"
    BOOKSTORE_MAP_BUTTON = "(//div[@class='class-bFztx1B class-rFSo80e']//li[@class='class-jnpxnK0'])[1]"
    ABOUT_THE_LIST_BUTTON = "(//div[@class='class-bFztx1B class-rFSo80e']//li[@class='class-jnpxnK0'])[2]"
    BOOKLIST_FAQS_BUTTON = "(//div[@class='class-bFztx1B class-rFSo80e']//li[@class='class-jnpxnK0'])[3]"
    SUBSCRIPTION_BOXES_BUTTON = "(//div[@class='class-bFztx1B class-rFSo80e']//li[@class='class-jnpxnK0'])[4]"
    MYSTERY_BOXES_BUTTON = "(//div[@class='class-bFztx1B class-rFSo80e']//li[@class='class-jnpxnK0'])[5]"
    BOOKLIST_RETURN_BUTTON = "(//div[@class='class-bFztx1B class-rFSo80e']//li[@class='class-jnpxnK0'])[1]"
    DOWNLOAD_LIST_BUTTON = "//div[@class='class-bFztx1B class-N8RYAzA']//button[@class='class-Rpdypjl']"  
  
    #**FIRST METHOD BELOW MAY NEED TO BE COMMENTED OUT BECAUSE THIS ELEMENT TENDS TO APPEAR RANDOMLY. ELEMENT APPEARS AS OF 4/30/2024
    
    #CLOSE PROMPT BUTTON METHOD - Code for a method that called the location of the close prompt button from the above locators variables
    def getClosePromptButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.CLOSE_PROMPT_BUTTON)

    #Code for a method to call the SUBSCRIBE PAGE METHOD and then clicks on the link
    def enterClosePromptButtonLocation(self):
        self.getClosePromptButtonLocation().click()

    #ENTERTAINMENT PAGE METHOD - Code for a method that called the location of the entertainment page from the above locators variables
    def getEntertainmentPageLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.ENTERTAINMENT_PAGE)

    #Code for a method to call the ENTERTAINMENT PAGE METHOD and then clicks on the link
    def enterEntertainmentPageLocation(self):
        self.getEntertainmentPageLocation().click()
        
    #BOOKS DROP DOWN METHOD - Code for a method that called the location of the books drop down from the above locators variables
    def getBooksDropdownLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.BOOKS_DROPDOWN)
    
    #Code for a method to call the BOOKS DROP DOWN METHOD and then clicks on the link
    def enterBooksDropdownLocation(self):
        self.getBooksDropdownLocation().click()
        
    #BEST-SELLING BOOKLIST BUTTON METHOD - Code for a method that called the location of the best-selling booklist button from the above locators variables
    def getBestsellingBooklistButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.BEST_SELLING_BOOKLIST_BUTTON)
    
    #Code for a method to call the BEST-SELLING BOOKLIST DROPDOWN METHOD and then clicks on the link
    def enterBestsellingBooklistButtonLocation(self):
        self.getBestsellingBooklistButtonLocation().click()
        
    #BOOKSTORE MAP BUTTON METHOD - Code for a method that called the location of the bookstore map button from the above locators variables
    def getBookstoreMapButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.BOOKSTORE_MAP_BUTTON)
    
    #Code for a method to call the BOOKSTORE MAP BUTTON METHOD and then clicks on the link
    def enterBookstoreMapButtonLocation(self):
        sleep(2)
        self.getBookstoreMapButtonLocation().click()
        
    #ABOUT THE LIST BUTTON METHOD - Code for a method that called the location of the about the list button from the above locators variables
    def getAboutTheListButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.ABOUT_THE_LIST_BUTTON)
    
    #Code for a method to call the ABOUT THE LIST BUTTON METHOD and then clicks on the link
    def enterAboutTheListButtonLocation(self):
        sleep(2)
        self.getAboutTheListButtonLocation().click()
        
    #BOOKLIST FAQS BUTTON METHOD - Code for a method that called the location of the booklist faqs button from the above locators variables
    def getBooklistFaqsButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.BOOKLIST_FAQS_BUTTON)
    
    #Code for a method to call the BOOKLIST FAQS BUTTON METHOD and then clicks on the link
    def enterBooklistFaqsButtonLocation(self):
        sleep(2)
        self.getBooklistFaqsButtonLocation().click()
        
    #SUBSCRIPTION BOXES BUTTON METHOD - Code for a method that called the location of the subscription boxes button from the above locators variables
    def getSubscriptionBoxesButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.SUBSCRIPTION_BOXES_BUTTON)
    
    #Code for a method to call the SUBSCRIPTION BOXES BUTTON METHOD and then clicks on the link
    def enterSubscriptionBoxesButtonLocation(self):
        sleep(2)
        self.getSubscriptionBoxesButtonLocation().click()
        
    #MYSTERY BOXES BUTTON METHOD - Code for a method that called the location of the mystery boxes button from the above locators variables
    def getMysteryBoxesButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.MYSTERY_BOXES_BUTTON)
    
    #Code for a method to call the MYSTERY BOXES BUTTON METHOD and then clicks on the link
    def enterMysteryBoxesButtonLocation(self):
        sleep(2)
        self.getMysteryBoxesButtonLocation().click()
        
    #BOOKLIST RETURN DROPDOWN METHOD - Code for a method that called the location of the booklist return button from the above locators variables
    def getBooklistReturnButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.BOOKLIST_RETURN_BUTTON)
    
    #Code for a method to call the BOOKLIST RETURN BUTTON METHOD and then clicks on the link
    def enterBooklistReturnButtonLocation(self):
        sleep(2)
        self.getBooklistReturnButtonLocation().click()
        
    #DOWNLOAD LIST BUTTON METHOD - Code for a method that called the location of the download list button from the above locators variables
    def getDownloadListButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.DOWNLOAD_LIST_BUTTON)
    
    #Code for a method to call the DOWNLOAD LIST BUTTON METHOD and then clicks on the link
    def enterDownloadListButtonLocation(self):
        sleep(2)
        self.getDownloadListButtonLocation().click()