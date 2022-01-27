import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep

class CheckboxEx:
    def checkbox_test(self):
        ser=Service(ChromeDriverManager().install())
        driver=webdriver.Chrome(service=ser)
        driver.get("https://www.html.am/html-codes/forms/html-checkbox-code.cfm")
        driver.maximize_window()
        checksList=driver.find_elements(by="xpath",value="//h2[text()='Disabling a Checkbox']/following-sibling::table//td[@class='exampleDisplay']/input")
        print(len(checksList))
        time.sleep(4)
        for check in checksList:
            print(check.is_enabled())
            if check.is_enabled()==True:
                if check.is_selected()==False:
                    time.sleep(4)
                    check.click()
                    time.sleep(4)
            else:
                print(check.get_attribute("value")+" text")
        driver.quit()

obj=CheckboxEx()
obj.checkbox_test()