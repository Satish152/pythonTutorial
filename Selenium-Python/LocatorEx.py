from selenium import webdriver
from  webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class LocatorEx:

    def LocatorEx(self,browserName):
        print("Selected browser name is "+browserName)

    def __init__(self,browserName):
        self.driver = None
        try:
            if browserName=="chrome":
                service=Service(ChromeDriverManager().install())
                self.driver=webdriver.Chrome(service=service)
            elif browserName=="firefox":
                service=Service(GeckoDriverManager().install())
                self.driver=webdriver.firefox(service=service)
            elif browserName=="ie":
                service = Service(IEDriverManager().install())
                self.driver = webdriver.Ie(service=service)
            else:
                service = Service(ChromeDriverManager().install())
                self.driver = webdriver.Chrome(service=service)
            self.driver.maximize_window()
        except Exception as e:
            if self.driver==None:
                print("Driver Initialization failed")
                SystemExit(0)

    def open_url(self,url):
        self.driver.get(url)
        print(self.driver.current_url)

    def enter_value(self):
        self.driver.find_element(by="name",value="q").send_keys("search")

    def close_browser(self):
        self.driver.quit()

obj=LocatorEx("chrome")
obj.open_url("https://google.com")
obj.enter_value()
obj.close_browser()