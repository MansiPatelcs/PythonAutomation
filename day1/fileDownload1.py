import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# import os
# location=os.getcwd()

# def chrome_setup():
#     from selenium.webdriver.chrome.service import Service
#     serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
#
#     """download file in your desire location """
#     # preferences = {"download.default_directory":location}  # save files in desired location
#     # preferences = {"download.default_directory":"C:\Users\Mansi Patel\PycharmProjects\pythonProject\selenium_python\day1"}
#
#     preferences = {"download.default_directory":location}
#     ops=webdriver.ChromeOptions()
#     ops.add_experimental_option("prefs", preferences)  # desired location
#
#     driver=webdriver.Chrome(service=serv_obj,options=ops)
#     return driver
#
# driver=chrome_setup()
#
# driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.find_element(By.XPATH,"//tbody/tr[1]/td[5]/a[1]").click()
# time.sleep(20)

"""for firefox browser"""

def firefox_setup():
    from selenium.webdriver.firefox.service import Service
    serv_obj=Service("C:\Drivers\geckodriver-v0.32.0-win-aarch64\geckodriver.exe")

    # settings
    ops=webdriver.FirefoxOptions()
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk","application/msword")
    ops.set_preference("browser,download.manager.showWhenStarting", False)
    driver=webdriver.Firefox(service=serv_obj,options=ops)
    return driver

driver=firefox_setup()

driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH,"//tbody/tr[1]/td[5]/a[1]").click()
time.sleep(20)
