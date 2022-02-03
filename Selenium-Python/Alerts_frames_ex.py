from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from  webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class alert_frames_ex:
    def alert_frames_fun(self):
        ser = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=ser)
        driver.get("https://demoqa.com/frames")
        driver.maximize_window()
        #frame1
        sleep(3)
        driver.switch_to.frame("frame1")
        print(driver.find_element(By.ID,"sampleHeading").text)
        driver.switch_to.default_content()
        driver.switch_to.frame(1)
        print(driver.find_element(By.ID,"sampleHeading").text)
        driver.switch_to.default_content()
        alertsMenu="//span[text()='Alerts']/.."
        alert_element=driver.find_element(By.XPATH,alertsMenu)
        sleep(2)
        driver.execute_script("arguments[0].scrollIntoView(true);",alert_element)
        alert_element.click()
        sleep(3)
        driver.find_element(By.ID,"alertButton").click()
        sleep(2)
        driver.switch_to.alert.accept()
        driver.quit()

alertObj=alert_frames_ex()
alertObj.alert_frames_fun()


