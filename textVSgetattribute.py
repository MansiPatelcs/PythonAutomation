from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

import time

driver.get("https://admin-demo.nopcommerce.com/login")

# email_box=driver.find_element(By.XPATH,"//input[@id='Email']")
#
# email_box.clear()
# email_box.send_keys("abc@gmail.com")
#
# print("result of text:",email_box.text)
# print("result of get_attribute():",email_box.get_attribute("value"))

# a=driver.find_element(By.XPATH,"//button[normalize-space()='Log in']")
# print("results of text:",a.text)
# print("results of get_attribute():",a.get_attribute("value"))
# print("results of get_attribute():",a.get_attribute("type"))
