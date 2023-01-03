
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.dummyticket.com/dumy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element(By.XPATH,"//a[contains(text(),'Buy Ticket')]").click()

# date of birth element

driver.find_element(By.XPATH,"//input[@id='dob']").click()  # opens datepicker

a=driver.find_element(By.XPATH,"//select[@aria-label='Select month']")
datepicker_month=Select(a)
datepicker_month.select_by_visible_text("Jan")

b=driver.find_element(By.XPATH,"//select[@aria-label='Select year']")
datepicker_year=Select(b)
datepicker_year.select_by_visible_text("2020")

dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for i in dates:
    if i.text=="24":
        i.click()
        break
