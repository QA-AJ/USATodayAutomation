import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


#finds the path to the webdriver, open the webpage, and maximize the window
@pytest.fixture(scope='class')
def setup(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://spotify.com/us')
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.wait = wait
    yield
    driver.quit()
