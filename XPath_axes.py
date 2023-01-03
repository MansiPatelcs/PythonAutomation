from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()
time.sleep(5)

"""Self"""

# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'Sequent Scientific')]").text
# print(text_msg)

"""parent"""

# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'Sequent Scientific')]/parent::td").text
# print(text_msg)

"""child"""

# childs=driver.find_elements(By.XPATH,"//a[contains(text(),'Sequent Scientific')]/ancestor::tr/child::td")
# print(len(childs))

""" ancestor"""

# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'Sequent Scientific')]/ancestor::tr").text
# print(text_msg)

"""Descendant"""

# descendants=driver.find_elements(By.XPATH,"//a[contains(text(),'Sequent Scientific')]/ancestor::tr/descendant::*")
# print(len(descendants))

"""following"""

# followings=driver.find_elements(By.XPATH,"//a[contains(text(),'Sequent Scientific')]/ancestor::tr/following::*")
# print(len(followings))

"""following-sibling"""

# followingsiblings=driver.find_elements(By.XPATH,"//a[contains(text(),'Sequent Scientific')]/ancestor::tr/following-sibling::*")
# print(len(followingsiblings))

"""preceding"""

# precedings=driver.find_elements(By.XPATH,"//a[contains(text(),'Sequent Scientific')]/ancestor::tr/preceding::*")
# print(len(precedings))

"""preceding-sibling"""

# precedingsiblings=driver.find_elements(By.XPATH,"//a[contains(text(),'Sequent Scientific')]/ancestor::tr/preceding-sibling::*")
# print(len(precedingsiblings))
