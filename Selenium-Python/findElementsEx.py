from selenium import webdriver
from  webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class ListofElementsEx:


    def __init__(self):
        self.driver = None
        try:
            service=Service(ChromeDriverManager().install())
            self.driver=webdriver.Chrome(service=service)
            self.driver.maximize_window()
        except Exception as e:
            print("driver initialization error")

    def test(self):
        self.driver.get("https://google.com")
        list=self.driver.find_elements(by=By.TAG_NAME,value="a")
        print(len(list))
        for link in list:
            print(link.text)
            if link.text=="Gmail":
                print(link.get_attribute("href"))
                link.click()
                break

    def tear_down(self):
        self.driver.close()

obj=ListofElementsEx()
obj.test()
obj.tear_down()

