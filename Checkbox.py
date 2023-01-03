import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj= Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

""" select specific checkbox"""

# driver.find_element(By.XPATH, "//input[@id='monday']").click()

"""select all the checkboxes"""

# checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
# print(len(checkboxes))

# approach 1

# for i in range(len(checkboxes)):
#     checkboxes[i].click()

# approach 2

# for i in checkboxes:
#     i.click()

""" select multiple checkboxes by choice """

# for i in checkboxes:
#     weekname=i.get_attribute('id')
#     if weekname=='monday' or weekname=='sunday':
#         i.click()

""" select last 2 checkboxes """

# for i in range(len(checkboxes)-2,len(checkboxes)):
#     checkboxes[i].click()

""" select first 2 checkboxes """

# for i in range(len(checkboxes)):
#     if i<2:
#         checkboxes[i].click()

""" clearing all the checkboxes """

# time.sleep(5)
#
# for i in checkboxes:
#     if i.is_selected():
#         i.click()

time.sleep(5)
