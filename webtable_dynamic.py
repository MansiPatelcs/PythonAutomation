from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()

# Admin--->user management--->users

driver.find_element(By.XPATH,"//aside[@class='oxd-sidepanel']//li[1]").click()

driver.find_element(By.XPATH,"//span[normalize-space()='User Management']").click()
driver.find_element(By.XPATH,"//ul[@role='menu']//li").click()

# total rows in a table

rows=len(driver.find_elements(By.XPATH,"//div[@role='rowgroup']/div"))
print(rows)

count=0
for r in range(1,rows+1):
    status=driver.find_element(By.XPATH,"//div[@role='rowgroup']/div").text
    print(status)
    if status=="Enabled":
        count+=1

print("Total number of users:",rows)
print("Number of enabled users:",count)
print("Number of disabled users:",rows-count)


