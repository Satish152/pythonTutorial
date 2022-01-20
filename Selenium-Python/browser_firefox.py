from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

ser=Service(GeckoDriverManager().install())
driver= webdriver.Firefox(service=ser)
driver.get("https://google.com")
driver.maximize_window()
driver.close()