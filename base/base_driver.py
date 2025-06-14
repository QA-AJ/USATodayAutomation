#Module with code to handle WebDriverWait and clickable/selectable actions that would normally be hardcoded in

#Imports needed for the code to work
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

#Class to allow callings/access to the webdriver
class BaseDriver:
    def __init__(self, driver):
        self.driver = driver
        
    #Code for scrolling to an element and either make it visible or click on it via streamlining the code so it can be used across all applicable test cases.
    
    #Should be used for methods that require hovering over options/menus
    def scroll_to_element(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        ActionChains(self.driver).move_to_element(wait.until(EC.visibility_of_element_located((locator_type, locator)))).perform()
    
    #Should be used for regular methods that need the driver to scroll to an element and then click on it
    def scroll_to_element_and_click(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)   
        ActionChains(self.driver).move_to_element(wait.until(EC.visibility_of_element_located((locator_type, locator)))).click().perform()
 
    #Code to make clickable elements on pages selectable via streamlining the code so it can be used across all applicable test cases
    def wait_unitl_element_is_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        clickable_elements = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return clickable_elements
     
    #Code to make drop down elements on pages selectable via streamlining the code so it can be used across all applicable test cases
    def wait_until_element_is_selectable(self, locator_type, locator):
        selectable_elements = Select(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((locator_type, locator))))
        return selectable_elements


    #Code to make shadow roots on pages selectable via streamlining the code so it can be used across all applicable test cases
    def wait_until_access_to_shadow_root(self, script):
        shadow_root = self.driver.execute_script(script)
        return shadow_root

        
    #Code to switch to iframes in order to find elements via streamlining the code so it can be used across all applicable test cases
    def wait_until_frame_is_switchable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        frame = wait.until(EC.frame_to_be_available_and_switch_to_it((locator_type, locator)))
        return frame
    
    #Code to switch back to main view after switching to an iframe to find elements via streamlining the code so it can be used across all applicable test cases
    def switchingtomainview(self):
        self.driver.switch_to.default_content()