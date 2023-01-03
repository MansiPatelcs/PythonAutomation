from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://www.opencart.com/index.php?route=account/register")
driver.maximize_window()

# a=driver.find_element(By.XPATH,"//select[@id='input-country']")
# b=Select(a)

"""select options from dropdown"""

# b.select_by_visible_text("India")
# b.select_by_value("10")
# b.select_by_index(13)

# time.sleep(5)

"""find total option and print them"""

# x=b.options
# print("Total number of options:",len(x))

# for i in x:
#     print(i.text)

""'select option from dropdown without using built-in method"""

# for i in x:
#     if i.text=="India":
#         i.click()
#         break
# time.sleep(5)

# c=driver.find_elements(By.XPATH,"//select[@id='input-country']/option")
# print(len(c))
