from http.server import executable
from selenium import webdriver


#finds the path to the webdriver
driver = webdriver.Chrome(executable_path = r'C:\\Users\\oniki_000.000\\Desktop\\AutomationTestingMasterclass\\Drivers\\Chromedriver\\chromedriver_win32\\chromedriver.exe')
driver.get('https://www.youtube.com') #opens up the webpage
driver.maximize_window() #maximizes the window used by the driver
driver.implicitly_wait(5) #forces the webdriver to wait for 5 seconds before doing the task
driver.find_element_by_xpath("/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input").send_keys("Python") #types the text into the search bar
driver.find_element_by_id("search-icon-legacy").click() #click on the "search" button
driver.find_element_by_xpath("/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[2]/ytd-channel-name/div/div/yt-formatted-string/a").click() #click on the "freeCodeCamp.org" profile
driver.find_element_by_xpath("/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse[2]/div[3]/ytd-c4-tabbed-header-renderer/tp-yt-app-header-layout/div/tp-yt-app-header/div[2]/div[2]/div/div[1]/div/div[2]/div[4]/ytd-button-renderer/a/tp-yt-paper-button").click() #click on the "subscribe" button