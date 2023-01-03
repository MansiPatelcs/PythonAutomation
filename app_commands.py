from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/")

print(driver.title)
print(driver.current_url)    # return current url of the web page

# driver.quit()   # to close the browser

print(driver.page_source)
