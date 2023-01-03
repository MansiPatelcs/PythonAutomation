from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

#  1) Scroll down page by pixel

# driver.execute_script("window.scrollBy(0,3000)","")
# value=driver.execute_script("return window.pageYOffset;")
# print("Number of pixels moved:",value)

# 2) Scroll down page till the element is visible

# flag=driver.find_element(By.XPATH,"//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img")
# driver.execute_script("arguments[0].scrollIntoView();",flag)
# time.sleep(5)
#
# value=driver.execute_script("return window.pageYOffset;")
# print("Number of pixels moved:",value)

# 3) Scroll down page till end

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(5)

value=driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:",value)

# Scroll up to starting position

driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
time.sleep(5)

value=driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:",value)
