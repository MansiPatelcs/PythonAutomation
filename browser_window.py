from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("http://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
time.sleep(10)

# windowID=driver.current_window_handle
# print(windowID)  # CDwindow-53A9011DE7D116B0C2762EC654F1F8C3
                 # CDwindow-0DE179A831862FDADB9342375D15D9CC

driver.find_element(By.XPATH,"//a[normalize-space()='OrangeHRM, Inc']").click()
time.sleep(5)
# windowIDs=driver.window_handles

# parentwindowid=windowIDs[0]
# childwindowid=windowIDs[1]
#
# # print(parentwindowid,childwindowid)
#
# driver.switch_to.window(childwindowid)
# print("Title of the child window:",driver.title)
#
# driver.switch_to.window(parentwindowid)
# print("Title of the parent window:",driver.title)

############################
# for i in windowIDs:
#     driver.switch_to.window(i)
#     print(driver.title)

###########################
# for i in windowIDs:
#     driver.switch_to.window(i)
#     if driver.title=='OrangeHRM':
#         driver.close()
# time.sleep(5)
