from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()

"""is_displayed() """  """ is_enabled() """

searchbox=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")

a=searchbox.is_displayed()
print("Displayed:",a)

b=searchbox.is_enabled()
print("Enabled:",b)

"""is_selected"""

rd_male=driver.find_element(By.XPATH,"//input[@id='gender-male']")
rd_female=driver.find_element(By.XPATH,"//input[@id='gender-female']")

print(rd_male.is_selected())
print(rd_female.is_selected())

rd_male.click()
print("After selecting male radio button...... ")
print(rd_male.is_selected())
print(rd_female.is_selected())
