from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
# driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()
time.sleep(5)

"Absolute xpath"

# driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin")
# driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123")
# time.sleep(5)

"Relative xpath"

# driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin")
# driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123")
# time.sleep(5)

"or"

# driver.find_element(By.XPATH,"//input[@name='username' or @placeholder='Username']").send_keys("Admin")
# driver.find_element(By.XPATH,"//input[@name='password' or @placeholder='password']").send_keys("admin123")
# time.sleep(5)

"and"

# driver.find_element(By.XPATH,"//input[@name='username' and @placeholder='Username']").send_keys("Admin")
# driver.find_element(By.XPATH,"//input[@name='password' and @placeholder='Password']").send_keys("admin123")
# time.sleep(5)

""" Contains()" & start-with() """

# driver.find_element(By.XPATH,"//input[contains(@name,'username')]").send_keys("Admin")
# driver.find_element(By.XPATH,"//input[starts-with(@name,'password')]").send_keys("admin123")
# time.sleep(5)

""" text() """

driver.find_element(By.XPATH, "//a[text()='Register']").click()
time.sleep(5)
