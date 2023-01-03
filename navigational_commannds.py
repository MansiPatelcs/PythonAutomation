from selenium import webdriver
from selenium.webdriver.chrome.service import Service
serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
import time

driver.get("https://www.amazon.in/")

driver.get("https://www.nykaa.com/")

driver.back()  # amazon
time.sleep(5)
# driver.forward()# nykaa
# driver.refresh()


