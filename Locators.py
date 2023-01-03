
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()       # maximize browser window

"""id and name locators """

# driver.find_element(By.ID,"small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
# driver.find_element(By.NAME,"q").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
# time.sleep(5)

""" Linktext & Partial linktext """

# driver.find_element(By.LINK_TEXT,"Register").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"Reg").click()
# time.sleep(5)

# driver.close()
# driver.quit()

""" To find more than one elements use class name  and tag name"""

# sliders=driver.find_elements(By.CLASS_NAME,"")
# print(len(sliders))

# links=driver.find_elements(By.TAG_NAME,"a")
# print(len(links))
