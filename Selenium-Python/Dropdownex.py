import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select

class DDEx:
    def dropdown_test(self):
        ser=Service(ChromeDriverManager().install())
        driver=webdriver.Chrome(service=ser)
        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select")
        driver.maximize_window()
        time.sleep(3)
        driver.switch_to.frame("iframeResult")
        time.sleep(3)
        select=Select(driver.find_element(by="name",value="cars"))
        select.select_by_index(3)
        time.sleep(1)
        select.select_by_value("saab")
        time.sleep(1)
        select.select_by_visible_text("Volvo")
        time.sleep(1)
        print(select.first_selected_option.text)
        print(list(select.all_selected_options))
        print(select.is_multiple)
        print(list(select.options))
        driver.quit()

ddObj=DDEx()
ddObj.dropdown_test()


