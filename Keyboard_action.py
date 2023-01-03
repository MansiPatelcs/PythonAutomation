# ctrl +A
# ctrl +C
# Tab
# ctrl + V

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://text-compare.com/")
driver.maximize_window()

input1=driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
input2=driver.find_element(By.XPATH,"//textarea[@id='inputText2']")

input1.send_keys("welcome to selenium")

act=ActionChains(driver)

# input1 --> ctrl+A select the text

# act.key_down(Keys.CONTROL)
# act.send_keys("a")
# # release keys
# act.key_up(Keys.CONTROL)
# act.perform()

act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

#  input1 --> ctrl+C copy text

act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

# press Tab key to navigate to input2

act.send_keys(Keys.TAB).perform()

#  input2 --> ctrl + V paste text

act.key_down(Keys.CONTROL).send_keys("V").key_up(Keys.CONTROL).perform()
