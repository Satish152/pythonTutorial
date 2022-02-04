from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class Implicit_wait_Ex:
    def implicitWait_ex(self):
        service=Service(ChromeDriverManager().install())
        driver=webdriver.Chrome(service=service)
        driver.maximize_window()
        #this implicit wait applied globally to the complete session of execution under this driver obj
        # if at all any element not found or some error happend in selenum wait for 10sec
        driver.implicitly_wait(10)
        driver.get("https://google.com")
        #here it have valid locator found in dom, so once element available it continue the execution
        driver.find_element(By.NAME,"q").send_keys("google")
        # here invalid locator passed, stlll it wait for 10 seconds and fails the execution
        driver.find_element(By.NAME,"qa").send_keys("text")

imp_obj=Implicit_wait_Ex()
imp_obj.implicitWait_ex()