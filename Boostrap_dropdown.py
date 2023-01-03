from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element(By.XPATH,"//span[@id='select2-reasondummy-container']").click()

options=driver.find_elements(By.XPATH,"//ul[@id='select2-reasondummy-results']/li")
print(len(options))

for i in options:
    if i.text=="Prefer not to say":
        i.click()
        break
time.sleep(10)

