import time

from selenium.webdriver.support.select import Select

import XLutils

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj= Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.implicitly_wait(10)

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()

file="location of file"

rows=XLutils.getRowCount(file,sheetName)

for r in range(2,rows+1):
    # reading data from excel
    pric=XLutils.readData(file,sheetname,r,1)
    rateofinterest=XLutils.readData(file,sheetname,r,2)
    per1=XLutils.readData(file,sheetname,r,3)
    per2=XLutils.readData(file,sheetname,r,4)
    fre=XLutils.readData(file,sheetname,r,5)
    exp_mvalue=XLutils.readData(file,sheetname,r,6)

    # passing data to the application
    driver.find_element(By.XPATH,"//input[@id='principal']").send_keys(pric)
    driver.find_element(By.XPATH,"//input[@id='interest']").send_keys(rateofinterest)
    driver.find_element(By.XPATH,"//input[@id='tenure']").send_keys(per1)

    perioddrp=Select(driver.find_element(By.XPATH,"//select[@id='tenurePeriod']"))
    perioddrp.select_by_visible_text(per2)

    fredrp=Select(driver.find_element(By.XPATH,"//select[@id='frequency']"))
    fredrp.select_by_visible_text(fre)

    driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[1]/img").click()
    act_mvalue=driver.find_element(By.XPATH,"//span[@id='resp_matval']/strong").text

    # validation
    if float(exp_mvalue)==float(act_mvalue):
        print("test passed")
        XLutils.writeData(file,SheetName,r,8,"Passed")
        XLutils.fillGreenColor(file,sheetName,r,8)
    else:
        print("test failed")
        XLutils.writeData(file,SheetName,r,8,"failed")
        XLutils.fillRedColor(file,sheetName,r,8)
    driver.find_element(By.XPATH,"//img[@class='PL5']").click
    time.sleep(5)
