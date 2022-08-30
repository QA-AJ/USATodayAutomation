from http.server import executable
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


#finds the path to the webdriver
driver = webdriver.Chrome(executable_path = r'C:\\Users\\oniki_000.000\\Desktop\\AutomationTestingMasterclass\\Drivers\\Chromedriver\\chromedriver_win32\\chromedriver.exe')
wait = WebDriverWait(driver, 10)
driver.get('https://www.youtube.com') #opens up the webpage
driver.maximize_window() #maximizes the window used by the driver

#searching = wait.unitl(EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input"))
#searching.click()
#searching.send_keys("Python")
#searching.send_keys(Keys.ENTER)
driver.find_element_by_xpath("/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input").send_keys("Python") #types the text into the search bar
driver.find_element_by_id("search-icon-legacy").click() #click on the "search" button
sleep(4)
#driver.find_element_by_css_selector("#video-title > yt-formatted-string").click() #click on the "Python Tutorial - Python Full Course for Beginners" video
driver.find_element_by_xpath("//*[@id='video-title']/yt-formatted-string").click() #click on the "Learn Python - Full Course for Beginners [Tutorial]" video
sleep(2)
#driver.find_element_by_css_selector("#video-title").click()
driver.find_elements_by_xpath("//*[@id='text']/a").click()
#driver.find_element_by_id("guide-button").click()
#driver.find_element_by_xpath("/html/body/ytd-app/div[1]/tp-yt-app-drawer/div[2]/div/div[2]/div[2]/ytd-guide-renderer/div[1]/ytd-guide-section-renderer[2]/div/ytd-guide-entry-renderer[2]/a/tp-yt-paper-item/yt-formatted-string").click()