from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()


# a=driver.find_element(By.XPATH,"//iframe[@class='demo-frame']")
# driver.switch_to.frame(a)
driver.switch_to.frame(0)

# driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("02/17/1998")  # mm/dd/yyyy
# time.sleep(5)

year="2020"
month="January"
date="24"

driver.find_element(By.XPATH,"//input[@id='datepicker']").click()  # open datepicker

while True:
    mon=driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yr=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text

    if mon==month and yr==year:
        break;
    else:
        # driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[2]").click()   # next arrow
        driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-w']").click()   # right arrow

#  select date

dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for ele in dates:
    if ele.text==date:
        ele.click()
        break



