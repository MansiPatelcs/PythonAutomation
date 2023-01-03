# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
#
# serv_obj=Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
# driver=webdriver.Chrome(service=serv_obj)
# driver.implicitly_wait(10)
#
# driver.get("https://www.dummyticket.com/dumy-ticket-for-visa-application/")
# driver.maximize_window()
#
# driver.find_element(By.XPATH,"//a[contains(text(),'Buy Ticket')]").click()
#
# driver.find_element(By.XPATH,"//input[@id='product_551']").click()
# driver.find_element(By.XPATH,"//input[@id='travname']").send_keys("abc")
# driver.find_element(By.XPATH,"//input[@id='travlastname']").send_keys("xyz")
# driver.find_element(By.XPATH,"//input[@id='dob']").click()
#
# month=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select month']"))
# month.select_by_visible_text("Jan")
#
# year=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select year']"))
# year.select_by_visible_text("2020")
#
# dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
# for i in dates:
#     if i=="24":
#         i.click()
#         break
#
# driver.find_element(By.XPATH,"//input[@id='sex_1']").click()
# driver.find_element(By.XPATH,"//input[@id='addmorepax']").click()
#
# driver.find_element(By.XPATH,"//span[@id='select2-addpaxno-container']").click()
#
# b=Select(driver.find_element(By.XPATH,"//input[@role='combobox']"))
# b.select_by_index(1)
#
# time.sleep(5)


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
# driver.implicitly_wait(20)
# mywait=WebDriverWait(driver,10)

driver.get("https://magento.softwaretestingboard.com/")

driver.find_element(By.XPATH, "//span[normalize-space()='Women']").click()

driver.find_element(By.XPATH, "//a[contains(text(),'Tops')]").click()

driver.find_element(By.XPATH, "//img[@alt='Breathe-Easy Tank']").click()
driver.find_element(By.XPATH, "//div[@id='option-label-size-143-item-167']").click()
driver.find_element(By.XPATH, "//div[@id='option-label-color-93-item-59']").click()
driver.find_element(By.XPATH, "//span[normalize-space()='Add to Cart']").click()

driver.find_element(By.XPATH, "//img[@alt='Gabrielle Micro Sleeve Top']").click()
driver.find_element(By.XPATH, "//div[@id='option-label-size-143-item-167']").click()
driver.find_element(By.XPATH, "//div[@id='option-label-color-93-item-53']").click()
driver.find_element(By.XPATH, "//span[normalize-space()='Add to Cart']").click()

driver.back()
driver.back()

driver.find_element(By.XPATH, "//img[@alt='Nona Fitness Tank']").click()
driver.find_element(By.XPATH, "//div[@id='option-label-size-143-item-168']").click()
driver.find_element(By.XPATH, "//div[@id='option-label-color-93-item-50']").click()
driver.find_element(By.XPATH, "//span[normalize-space()='Add to Cart']").click()

driver.back()

driver.find_element(By.XPATH, "//img[@alt='Lucia Cross-Fit Bra ']").click()
driver.find_element(By.XPATH, "//div[@id='option-label-size-143-item-166']").click()
driver.find_element(By.XPATH, "//div[@id='option-label-color-93-item-57']").click()
driver.find_element(By.XPATH, "//span[normalize-space()='Add to Cart']").click()

driver.back()

driver.find_element(By.XPATH, "//img[@alt='Celeste Sports Bra']").click()
driver.find_element(By.XPATH, "//div[@id='option-label-size-143-item-167']").click()
driver.find_element(By.XPATH, "//div[@id='option-label-color-93-item-58']").click()
driver.find_element(By.XPATH, "//span[normalize-space()='Add to Cart']").click()

driver.find_element(By.XPATH, "//a[@class='action showcart']").click()
driver.find_element(By.XPATH, "//button[@id='top-cart-btn-checkout']").click()
driver.find_element(By.XPATH, "//input[@id='GYFW9NE']").send_keys("admin")
driver.find_element(By.XPATH, "//input[@id='NVJAHI1']").send_keys("abc")
driver.find_element(By.XPATH, "//input[@id='UHFVAAI']").send_keys("california")
driver.find_element(By.XPATH, "//input[@id='Q5I73Q2']").send_keys("california")

a = Select(driver.find_element(By.XPATH, "//select[@id='FXFGTI6']")).click()
a.select_by_visible_text("California")

driver.find_element(By.XPATH, "//input[@id='QDIAJDM']").send_keys("90210")
driver.find_element(By.XPATH, "//input[@id='R71EV52']").send_keys("+123145675868")
driver.find_element(By.XPATH, "//input[@name='ko_unique_9']").click()
driver.find_element(By.XPATH, "//button[@class='button action continue primary']").click()
driver.find_element(By.XPATH, "//span[normalize-space()='Place Order']").click()

driver.close()

# driver.find_element(By.XPATH, "//span[normalize-space()='Men']").click()
# driver.find_element(By.XPATH, "//a[contains(text(),'Hoodies & Sweatshirts')]").click()
#
# driver.find_element(By.XPATH, "//img[@alt='Hero Hoodie']").click()
# driver.find_element(By.XPATH, "//div[@id='option-label-size-143-item-168']").click()
# driver.find_element(By.XPATH, "//div[@id='option-label-color-93-item-52']").click()
# driver.find_element(By.XPATH, "//span[normalize-space()='Add to Cart']").click()
#
# driver.back()
#
# driver.find_element(By.XPATH, "//img[@alt='Bruno Compete Hoodie']").click()
# driver.find_element(By.XPATH, "//div[@id='option-label-size-143-item-167']").click()
# driver.find_element(By.XPATH, "//div[@id='option-label-color-93-item-49']").click()
# driver.find_element(By.XPATH, "//button[@id='product-addtocart-button']").click()
#
#
# button=mywait.until(EC.presence_of_element_located((By.XPATH, "//a[@class='action showcart']")))
# button.click()
#
# driver.find_element(By.XPATH, "//a[@title='Remove item']").click()
#
# alertwindow =driver.switch_to.alert
# alertwindow.accept()
#
# driver.find_element(By.XPATH, "//a[@title='Remove item']").click()
#
# alertwindow = driver.switch_to.alert
# alertwindow.accept()
#
# driver.close()
