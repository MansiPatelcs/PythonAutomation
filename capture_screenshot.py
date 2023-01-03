from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# driver.save_screenshot("C:\\Users\\Mansi Patel\\PycharmProjects\\pythonProject\\selenium_python\\day1\\homepage.png")
# driver.get_screenshot_as_file("C:\\Users\\Mansi Patel\\PycharmProjects\\pythonProject\\selenium_python\\day1\\homepage1.png")


#  save screenshots in binary formate
# driver.get_screenshot_as_base64()
# driver.get_screenshot_as_png()
