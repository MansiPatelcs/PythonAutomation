
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
# Click on link

# driver.find_element(By.LINK_TEXT,"Digital downloads").click()

# find number of links in a page

# links=driver.find_elements(By.TAG_NAME,'a')
links=driver.find_elements(By.XPATH,'//a')
print("Total number of links are:", len(links))

# print all the link names

for i in links:
    print(i.text)

