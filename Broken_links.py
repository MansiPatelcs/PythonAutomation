# we need to install request package through file---> Settings--->ProjectInterpreter
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

alllinks=driver.find_elements(By.TAG_NAME,"a")

count=0
for i in alllinks:
    url=i.get_attribute("href")
    try:
        res=requests.head(url)
    except:
        None

    if res.status_code>=400:
        print(url,"is broken link")
        count+=1
    else:
        print(url,"is valid link")

print("Total number of broken links:",count)
