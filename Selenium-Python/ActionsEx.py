from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from  webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class ActionsEx:
    def actions_fun(self):
        ser = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=ser)
        driver.get("https://www.cricbuzz.com/")
        driver.maximize_window()
        actions=ActionChains(driver)
        seriesDD=driver.find_element(By.ID, "seriesDropDown")
        actions.move_to_element(seriesDD).perform();
        sleep(3)
        actions.click(driver.find_element(By.XPATH,"//a[text()='West Indies tour of India, 2022']")).perform()
        sleep(2)
        driver.quit()

actObj=ActionsEx()
actObj.actions_fun()
