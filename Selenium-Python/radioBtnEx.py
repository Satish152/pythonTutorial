import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


class RadiobtnEx:
    def radiobtn_test(self):
        ser=Service(ChromeDriverManager().install())
        driver=webdriver.Chrome(service=ser)
        driver.get("https://www.html.am/html-codes/forms/html-checkbox-code.cfm")
        driver.maximize_window()
        radioList=driver.find_elements(by="xpath",value="//input[@type='radio']")
        print(len(radioList))
        time.sleep(4)
        for radio in radioList:
            print(radio.is_enabled())
            if radio.is_enabled()==True:
                if radio.is_selected()==False:
                    time.sleep(4)
                    radio.click()
                    time.sleep(4)
            else:
                print(radio.get_attribute("value")+" text")
        driver.quit()

obj=RadiobtnEx()
obj.radiobtn_test()