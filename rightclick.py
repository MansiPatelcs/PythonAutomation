from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()

button=driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")

act=ActionChains(driver)

act.context_click(button).perform()

driver.find_element(By.XPATH,"/html/body/ul/li[3]/span").click()
time.sleep(5)
driver.switch_to.alert.accept()

time.sleep(5)
