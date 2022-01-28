# In python we have different methods available to take screenshots
# get_screenshot_as_file() which accepts file path as a parameter to store the file
# screenshot() method is used to take the screenshpt of particular webelement
# save_screenshot() is used to save the screenshot in given location
# same like we have get_screenshot_as_png() and get_screenshot_as_base64()

# By default it accepts only .PNG format

import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

class ScreenshotEx:
    def screenshot_test(self):
        ser=Service(ChromeDriverManager().install())
        driver=webdriver.Chrome(service=ser)
        driver.get("https://demo.seleniumeasy.com/basic-select-dropdown-demo.html")
        driver.maximize_window()
        time.sleep(3)
        select_element=driver.find_element(by="id",value="multi-select")
        select_element.screenshot("../screenshot/elementSS.png")
        multi_select = Select(select_element)
        multi_select.select_by_value("Texas")
        driver.get_screenshot_as_file("../screenshot/fileSS.png")
        driver.save_screenshot("../screenshot/saveSS.png")
        driver.quit()

ssObj=ScreenshotEx()
ssObj.screenshot_test()