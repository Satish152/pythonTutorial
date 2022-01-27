from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

ser=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=ser)
driver.get("https://google.com")
driver.maximize_window()
driver.close()