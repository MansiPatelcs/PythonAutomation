from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

# driver.get("https://demo.nopcommerce.com/")
# driver.maximize_window()
# reglink=Keys.CONTROL+Keys.RETURN
# driver.find_element(By.XPATH,"//a[@class='ico-register']").send_keys(reglink)

#  New Tab - Selenium4 : Opens a new tab and switches to new tab

# driver.get("https://www.opencart.com/")
# driver.switch_to.new_window("tab")
# driver.get("https://www.orangehrm.com/")

#  New window - Selenium4 : Opens a new browser window and switches to new window

driver.get("https://www.opencart.com/")
driver.switch_to.new_window("window")
driver.get("https://www.orangehrm.com/")

time.sleep(10)
