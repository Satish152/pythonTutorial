import logging
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service

ser=Service(EdgeChromiumDriverManager(log_level=logging.INFO).install())
driver=webdriver.Edge(service=ser)
driver.get("https://google.com")
driver.maximize_window()
driver.close()