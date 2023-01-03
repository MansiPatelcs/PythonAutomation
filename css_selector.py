from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://www.facebook.com/")
driver.maximize_window()
time.sleep(5)

""" Tag and ID """

# driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc")
# driver.find_element(By.CSS_SELECTOR,"#email").send_keys("abc")

""" Tag and Class """

# driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("abc")
# driver.find_element(By.CSS_SELECTOR,".inputtext").send_keys("abc")

""" Tag and attribute """

# driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys("abc")
# driver.find_element(By.CSS_SELECTOR,"[data-testid=royal_email]").send_keys("abc")

""" Tag, Class and Attribute """

# driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_pass]").send_keys("abc")
driver.find_element(By.CSS_SELECTOR,".inputtext[data-testid=royal_pass]").send_keys("abc")
time.sleep(5)
