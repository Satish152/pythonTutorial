# for fluent wait we can use the same class WebDriverWait by passing few wxtra arguments like
# polling time and ignore exceptions which converts the explicit wait class to fluent wait

from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By

class Fluent_wait_Ex:
    def fluentWait_ex(self):
        service=Service(ChromeDriverManager().install())
        driver=webdriver.Chrome(service=service)
        driver.maximize_window()
        wait=WebDriverWait(driver,20,3,ignored_exceptions=[ElementClickInterceptedException,NoSuchElementException])
        driver.get("https://www.apsrtconline.in/oprs-web/")
        wait.until(EC.visibility_of_element_located((By.ID,"q")))

testObj=Fluent_wait_Ex()
testObj.fluentWait_ex()