from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from  webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class Multi_window_handle:
    def multi_win_handle(self):
        ser = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=ser)
        driver.get("https://demoqa.com/browser-windows")
        driver.maximize_window()
        parent=driver.current_window_handle
        newtabBtn=driver.find_element(By.ID,"tabButton")
        newtabBtn.click()
        sleep(3)
        wins=driver.window_handles
        for window in wins:
            if window!=parent:
                driver.switch_to.window(window)
                print(driver.title)
                driver.close()
                break
            print(driver.title)
        print(driver.switch_to.window(parent))
        driver.quit()

multi_win_obj=Multi_window_handle()
multi_win_obj.multi_win_handle()