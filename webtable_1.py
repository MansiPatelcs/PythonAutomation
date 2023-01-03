# 1) count number of rows & columns
# 2) read specific rows & columns
# 3) read all the rows & columns
# 4) read data based on conditions(List books name those author is Mukesh)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# 1) count number of rows & columns

noOfrows=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))

noOfcols=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))
print(noOfrows)
print(noOfcols)

# 2) read specific rows & columns

# a=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[5]/td[1]").text
# print(a)

# 3) read all the rows & columns

# print("printing all the rows and column data...........")
#
# for r in range(2,noOfrows+1):
#     for c in range(1,noOfcols+1):
#         a=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
#         print(a,end="         ")
#     print()

# 4) read data based on conditions(List books name those author is Mukesh)

for r in range(2,noOfrows+1):
    authorname=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]").text
    if authorname=="Mukesh":
        bookname=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]").text
        price=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[4]").text
        print(bookname,"    ",authorname,"    ",price)
