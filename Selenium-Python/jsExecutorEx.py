
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from  webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class JavascriptExecEx:
    def sampleTest(self):
        service=Service(ChromeDriverManager().install())
        driver=webdriver.Chrome(service=service)
        driver.maximize_window()
        driver.get("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html")
        sleep(6)
        demoOnlienOpt=driver.find_element(By.XPATH,"//a[text()='Demo Home']")
        select_element = driver.execute_script("return document.getElementById('multi-select')")
        driver.execute_script("arguments[0].scrollIntoView(true);",select_element)
        sleep(3)
        driver.execute_script("scroll(0,0);")
        sleep(3)

jsObj=JavascriptExecEx()
jsObj.sampleTest()