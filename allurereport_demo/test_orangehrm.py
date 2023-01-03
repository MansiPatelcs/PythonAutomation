from allure_commons.types import AttachmentType
from selenium import webdriver
import allure
import pytest
from selenium.webdriver.common.by import By

@allure.severity(allure.severity_level.NORMAL)
class TestHRM:
    @allure.severity(allure.severity_level.MINOR)

    def test_Logo(self):
        self.driver=webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.implicitly_wait(10)
        status=self.driver.find_element(By.XPATH,"//img[@alt='company-branding']").is_displayed()
        if status==True:
            assert True
        else:
            assert False
        self.driver.close()

    @allure.severity(allure.severity_level.NORMAL)
    def test_listemployees(self):
        pytest.skip("Skipping test... Later I will implement..")

    @allure.severity(allure.severity_level.CRITICAL)
    def test_Login(self):
        self.driver=webdriver.Chrome("C:\Drivers\chromedriver_win32\chromedriver.exe")
        self.driver.implicitly_wait(10)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
        self.driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin@123")
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
        act_title=self.driver.title

        if act_title=="OrangeHRM":
            self.driver.close()
            assert True
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="testLoginScreen",attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False

