import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

class MultiDDEx:
    def multi_dropdown_test(self):
        ser=Service(ChromeDriverManager().install())
        driver=webdriver.Chrome(service=ser)
        driver.get("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html")
        driver.maximize_window()
        time.sleep(3)
        select_element=driver.find_element(by="id",value="multi-select")
        multi_select=Select(select_element)
        multi_select.select_by_value("Texas")
        multi_select.select_by_index(0)
        multi_select.select_by_visible_text("Florida")
        time.sleep(3)
        list=multi_select.all_selected_options
        for item in list:
            print(item.text)
        driver.quit()

multiObj=MultiDDEx()
multiObj.multi_dropdown_test()