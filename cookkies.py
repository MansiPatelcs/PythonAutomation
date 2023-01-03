from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
import time


serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# Capture cookies from the browser
cookies=driver.get_cookies()
print(len(cookies))

# print details of all cookies

# for i in cookies:
#     print(i.get("name"),":",i.get("value"))
#     # print(i)

#  Add new cookie to the browser

driver.add_cookie({"name":"MyCookie","value":"123456"})
cookies=driver.get_cookies()
print("Cookies after adding...",len(cookies))

# Delete specific cookie from the browser

driver.delete_cookie("MyCookie")
cookies=driver.get_cookies()
print("after deleting...",len(cookies))

#  Delete all the cookies

driver.delete_all_cookies()
cookies=driver.get_cookies()
print("size of cookies after deleted one:",len(cookies))


