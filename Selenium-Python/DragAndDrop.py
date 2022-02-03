import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from  webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class DragAndDropEx:
    def drag_and_drop_fun(self):
        ser = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=ser)
        driver.get("https://jqueryui.com/draggable/")
        driver.maximize_window()
        frame_element=driver.find_element(By.CLASS_NAME,"demo-frame")
        driver.switch_to.frame(frame_element)
        drag_element=driver.find_element(By.ID,"draggable")
        actions=ActionChains(driver)
        actions.drag_and_drop_by_offset(drag_element,50,0).perform()
        print("drag performed")
        time.sleep(2)
        actions.drag_and_drop_by_offset(drag_element, 0, 50).perform()
        print("drag performed")
        time.sleep(3)

dragAndDropObj=DragAndDropEx()
dragAndDropObj.drag_and_drop_fun()
