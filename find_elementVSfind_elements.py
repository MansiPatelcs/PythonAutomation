from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

import time

driver.get("https://demo.nopcommerce.com/")

"""find_element() --- returns single webelement"""

""" 1) Locator matching with single webelement"""

# element=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
# element.send_keys("Lenovo Thinkpad X1 Carbon Laptop")
# time.sleep(5)

""" 2) Locator matching with multiple webelements"""

# element=driver.find_element(By.XPATH,"//div[@class='footer']//a")
# print(element.text)

""" 3) Element not available then throw NoSuchElementException"""

# login_element=driver.find_element(By.LINK_TEXT,"Log")
# login_element.click()

"""find_elements"""

""" 1) Locator matching with single webelement """

# elements=driver.find_elements(By.XPATH,"//input[@id='small-searchterms']")
# print(len(elements))

# elements[0].send_keys("Lenovo Thinkpad X1 Carbon Laptop")

""" 2) Locator matching with multiple webelements """

# elements=driver.find_elements(By.XPATH,"//div[@class='footer']//a")
# print(len(elements))
# # print(elements[0].text)
# for i in elements:
#     print(i.text)

# 3) Element not available then not throw NoSuchElementException

login_element=driver.find_elements(By.LINK_TEXT,"Log")
print(len(login_element))
