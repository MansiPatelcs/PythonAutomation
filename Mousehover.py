from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()

# Admin--->user management--->users

admin=driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a")

usermgmt=driver.find_element(By.XPATH,"//span[normalize-space()='User Management']")
users=driver.find_element(By.XPATH,"//ul[@role='menu']//li")

# mouse hover

act=ActionChains(driver)
act.move_to_element(admin).move_to_element(usermgmt).move_to_element(users).click().perform()


time.sleep(10)
