from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By

class Explicit_wait_Ex:
    def explicitWait_ex(self):
        service=Service(ChromeDriverManager().install())
        driver=webdriver.Chrome(service=service)
        driver.maximize_window()
        wait=WebDriverWait(driver,20)
        driver.get("https://www.apsrtconline.in/oprs-web/")
        exist=wait.until(EC.visibility_of_element_located((By.XPATH,"//img[contains(@src,'bot-3')]")))
        if exist:
            print("Explicit wait working fine")
        else:
            print("Explicit wait not working fine")
        if wait.until(EC.element_to_be_clickable((By.ID,"fromPlaceName"))):
            print("From place field is enabled")
        else:
            print("From place field is not enabled")



testObj=Explicit_wait_Ex()
testObj.explicitWait_ex()
