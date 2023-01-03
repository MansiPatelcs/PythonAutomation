#Test Case

# 1) Open Web Browser(Chrome/firefox/Edge)
# 2) Open URL https://opensource-demo.orangehrmlive.com/
# 3) Provide username (admin)
# 4) Provide password (admin123)
# 5) Click on login
# 6) Capture title of the home page (Actual title)
# 7) Verify title of the page: " OrangeHRM" (Expected)
#  8) Close browser


# Assignment

# 1) Open Web Browser(chrome,firefox,edge)
# 2) Open URL https://admin-demo.nopcommerce.com/login
# 3)Provide Email(admin@yourstore.com)
# 4) Provide password(admin)
# 5)click on login
# 6) Capture title of the dashboard page(Actual title)
# 7) Verify title of the page:"Dashboard/nopCommerce administration"(Expected)
# 8) Close Browser


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://admin-demo.nopcommerce.com/login")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.ID,"Email").clear()
driver.find_element(By.ID,"Email").send_keys("admin@yourstore.com")
time.sleep(5)

driver.find_element(By.NAME,"Password").clear()
driver.find_element(By.NAME,"Password").send_keys("admin")
time.sleep(5)

driver.find_element(By.CSS_SELECTOR,"button.button-1").click()
time.sleep(5)

act_title=driver.title
exp_title="Dashboard / nopCommerce administration"

if act_title==exp_title:
    print("Login Test Passed")
else:
    print("Login Test Failed")

driver.close()

""" selenium 3 """

# from selenium import webdriver
# import time
#
# driver = webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
# time.sleep(5)
#
# driver.get("https://opensource-demo.orangehrmlive.com")
# time.sleep(10)
#
# driver.find_element_by_name("username").send_keys("Admin")
# time.sleep(5)
# driver.find_element_by_name("password").send_keys("admin123")
# time.sleep(5)
# driver.find_element_by_Xpath("//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
#
# act_title=driver.title
# exp_title="OrangeHRM"
# if act_title==exp_title:
#     print("Login Test Passed")
# else:
#     print("Login Test Failed")
# driver.close()


""" Selenium 4 """

# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# import time
#
# serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
#
# driver= webdriver.Chrome(service=serv_obj)
# time.sleep(5)
#
# driver.get("https://opensource-demo.orangehrmlive.com")
# time.sleep(10)
#
# driver.find_element(By.NAME,"username").send_keys("Admin")
# time.sleep(5)
# driver.find_element(By.NAME,"password").send_keys("admin123")
# time.sleep(5)
# driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
# time.sleep(5)
#
# act_title=driver.title
# exp_title="OrangeHRM"
# if act_title==exp_title:
#     print("Login Test Passed")
# else:
#     print("Login Test Failed")
# driver.close()


