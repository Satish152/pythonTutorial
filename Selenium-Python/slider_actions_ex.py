import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from  webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class SlideFiledEx:
    def slide_fun(self):
        ser = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=ser)
        driver.get("https://www.w3schools.com/howto/howto_js_rangeslider.asp")
        driver.maximize_window()
        actions=ActionChains(driver)
        element=driver.find_element(By.CLASS_NAME,"slider-square")
        value=driver.find_element(By.ID,"f").text
        print(value," before slide")
        actions.click_and_hold(element).pause(1).drag_and_drop_by_offset(element, 60, 0).perform()
        time.sleep(3)
        value1 = driver.find_element(By.ID, "f").text
        print(value1, " after slide")
        if value!=value1:
            print("value updated")

slider_obj=SlideFiledEx()
slider_obj.slide_fun()

