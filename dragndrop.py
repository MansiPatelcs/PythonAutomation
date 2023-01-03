from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

source_element=driver.find_element(By.XPATH,"")
target_element=driver.find_element(By.XPATH,"")

act=ActionChains(driver)
act.drag_and_drop(source_element,target_element).perform()
