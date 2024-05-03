#Imports needed for the code to work
from time import sleep
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver

#Code to create the applicable page for externalizing in other test cases. Super code externalizes the Base Driver so the operator can use the methods from that particular file
class LaunchPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        
    #**FIRST LOCATOR VARIABLE BELOW MAY NEED TO BE COMMENTED OUT BECAUSE THIS ELEMENT TENDS TO APPEAR RANDOMLY. ELEMENT APPEARS AS OF 4/30/2024
    
    #Locator variables. Change these to affect the test case
    CLOSE_PROMPT_BUTTON = "//div[@class='gnt_mol']//button[@class='gnt_mol_xb']"
    SIGNIN_DROPDOWN = "//nav[@class='gnt_n_mn']//a[@class='gnt_n_us_a gnt_n_mn_ce']"
    CREATE_ACCOUNT_BUTTON = "//div[@class='gnt_n_us_dd']//a[@class='gnt_n_us_dd_ba gnt_n_us_dd_a__li']"
    FIRST_NAME_FIELD = "//div[@class='form-fields-container']//input[@name='firstName']"
    LAST_NAME_FIELD = "//div[@class='form-fields-container']//input[@name='lastName']"
    EMAIL_ADDRESS_FIELD = "//div[@class='form-fields-container']//input[@name='email']"
    CREATE_PASSWORD_FIELD = "//div[@class='form-fields-container']//input[@name='password']"
    RETYPE_PASSWORD_FIELD = "//div[@class='form-fields-container']//input[@name='password-confirm']"
    SUBMIT_BUTTON = "//div[@class='form-fields-container']//button[@class='input button primary']"
    
    #**FIRST METHOD BELOW MAY NEED TO BE COMMENTED OUT BECAUSE THIS ELEMENT TENDS TO APPEAR RANDOMLY. ELEMENT APPEARS AS OF 4/30/2024
    
    #CLOSE PROMPT BUTTON METHOD - Code for a method that called the location of the close prompt button from the above locators variables - COMMENTED OUT BECAUSE THIS ELEMENT IS NO LONGER APPEARING AS OF 4/30/2024. THIS ELEMENT TENDS TO APPEAR RANDOMLY
    def getClosePromptButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.CLOSE_PROMPT_BUTTON)

    #Code for a method to call the CLOSE PROMPT BUTTON METHOD and then clicks on the link
    def enterClosePromptButtonLocation(self):
        self.getClosePromptButtonLocation().click()

    #SIGN IN DROP DOWN METHOD - Code for a method that called the location of the sign in drop down from the above locators variables
    def getSigninDropdownLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.SIGNIN_DROPDOWN)

    #Code for a method to call the SIGN IN DROP DOWN METHOD and then clicks on the link
    def enterSigninDropdownLocation(self):
        self.getSigninDropdownLocation().click()
        
    #CREATE ACCOUNT BUTTON METHOD - Code for a method that called the location of the create account button from the above locators variables
    def getCreateAccountButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.CREATE_ACCOUNT_BUTTON)

    #Code for a method to call the CLOSE PROMPT BUTTON METHOD and then clicks on the link
    def enterCreatAccountButtonLocation(self):
        self.getCreateAccountButtonLocation().click()

    #FIRST NAME FIELD METHOD - Code for a method that called the location of the first name field from the above locators variables
    def getFirstNameFieldLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.FIRST_NAME_FIELD)

    #Code for a method to call the FIRST NAME FIELD METHOD and then clicks on the link
    def enterFirstNameFieldLocation(self, firstName):
        sleep(2)
        self.getFirstNameFieldLocation().send_keys(firstName)
        
    #LAST NAME FIELD METHOD - Code for a method that called the location of the last name field from the above locators variables
    def getLastNameFieldLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.LAST_NAME_FIELD)

    #Code for a method to call the LAST NAME FIELD METHOD and then clicks on the link
    def enterLastNameFieldLocation(self, lastName):
        self.getLastNameFieldLocation().send_keys(lastName)
        
    #EMAIL ADDRESS FIELD METHOD - Code for a method that called the location of the email address field from the above locators variables
    def getEmailAddressFieldLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.EMAIL_ADDRESS_FIELD)

    #Code for a method to call the EMAIL ADDRESS FIELD METHOD and then clicks on the link
    def enterEmailAddressFieldLocation(self, emailAddress):
        self.getEmailAddressFieldLocation().send_keys(emailAddress)
        
    #CREATE PASSWORD FIELD METHOD - Code for a method that called the location of the create password field from the above locators variables
    def getCreatePasswordFieldLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.CREATE_PASSWORD_FIELD)

    #Code for a method to call the CREATE PASSWORD FIELD METHOD and then clicks on the link
    def enterCreatePasswordFieldLocation(self, createPassword):
        self.getCreatePasswordFieldLocation().send_keys(createPassword)
        
    #RETYPE PASSWORD FIELD METHOD - Code for a method that called the location of the retype password field from the above locators variables
    def getRetypePasswordFieldLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.RETYPE_PASSWORD_FIELD)
    
    #Code for a method to call the RETYPE PASSWORD FIELD METHOD and then clicks on the link
    def enterRetypePasswordFieldLocation(self, retypePassword):
        self.getRetypePasswordFieldLocation().send_keys(retypePassword)

    #Code to select all of the text fields. Calls the FIRST NAME, LAST NAME, EMAIL ADDRESS, CREATE PASSWORD, and RETYPE PASSWORD FIELDS for this to work
    def textFields(self, firstName, lastName, emailAddress, createPassword, retypePassword):
        self.enterFirstNameFieldLocation(firstName)
        self.enterLastNameFieldLocation(lastName)
        self.enterEmailAddressFieldLocation(emailAddress)
        self.enterCreatePasswordFieldLocation(createPassword)
        self.enterRetypePasswordFieldLocation(retypePassword)

    #SUBMIT BUTTON METHOD - Code for a method that called the location of the submit button from the above locators variables
    def getSubmitButtonLocation(self):
        return self.wait_unitl_element_is_clickable(By.XPATH, self.SUBMIT_BUTTON)
    
    #Code for a method to call the RETYPE PASSWORD FIELD METHOD and then clicks on the link
    def enterSubmitButtonLocation(self):
        self.getSubmitButtonLocation().click()