from datetime import time

import self as self
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import time

class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome("C:\\Users\\ishamishra\\Downloads\\chromedriver_win32\\chromedriver.exe")
        driver.get("https://hashedin-frontend-urtjok3rza-wl.a.run.app/")

        # username visible
        # a = driver.find_element(By.XPATH, '//input[@name="username"]')
        # a.is_displayed()
        # self.assertTrue(a, " username is not enabled")
        # print("username field is present")

        # checking username field  is present or not
        un = driver.find_element(By.XPATH, '//input[@name="username"]')
        un.is_displayed()
        self.assertTrue(un, "username field is not present")
        print("username field is present")
        time.sleep(3)

        # checking username is taking text:
        un.is_enabled()
        self.assertTrue(un, "username text box is not enabled")
        print("username field is enabled and ready to take input from the user")
        time.sleep(3)

        #entering username as manager
        un.send_keys("testmanager")
        time.sleep(5)

        # checking password field is available on webpage

        p=driver.find_element(By.ID,"password")
        p.is_displayed()
        self.assertTrue(p, "password field is not present")
        print("password field is present on the webpage")
        time.sleep(2)

        # checking the password field is enabled:
        p.is_enabled()
        self.assertTrue(p, "password field is not enabled")
        print("password field is ready to take input from the user")
        time.sleep(3)

        #entering password as manager
        p.send_keys("manager")
        time.sleep(5)

        # whether login button is present
        lb=driver.find_element(By.ID,"login")
        lb.is_displayed()
        self.assertTrue(lb,"login button is not present")
        print("login button is present")

        # clicking the login button
        lb.click()
        time.sleep(5)

        #validating the login successful as manager
        i=driver.current_url
        self.assertEqual("https://hashedin-frontend-urtjok3rza-wl.a.run.app/manager",i, "login not successful")
        print("login successful as manager")

        #checking logout button is present on web page or not
        lo=driver.find_element(By.XPATH,'//a[@class="dropdown-toggle nav-link"]')
        lo.click()
        time.sleep(5)
        lo.is_displayed()
        self.assertTrue(lo,"logout button  is  not present")
        print("logout button is present")

        #clicking on logout button
        lob=driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[1]/div[2]/div/div/div/a')
        lob.click()
        time.sleep(5)

        #checking logout successfully or not
        m=driver.current_url
        self.assertEqual("https://hashedin-frontend-urtjok3rza-wl.a.run.app/",m,"logout failed")
        print("logout successfully as manager")
        time.sleep(7)


        # login as employee
        un1=driver.find_element(By.XPATH,'//input[@name="username"]')
        un1.send_keys("testemployee")
        time.sleep(3)
        p1=driver.find_element(By.ID,"password")
        p1.send_keys("employee")
        time.sleep(3)
        lb1=driver.find_element(By.ID,"login")
        lb1.click()
        time.sleep(5)
        i1=driver.current_url
        self.assertEqual("https://hashedin-frontend-urtjok3rza-wl.a.run.app/employee",i1,"login as employee failed")
        print("login successful as employee")
        time.sleep(5)


        #checking logout for employee
        lo1 = driver.find_element(By.XPATH, '//a[@class="dropdown-toggle nav-link"]')
        lo1.click()
        time.sleep(5)
        lo1.is_displayed()
        self.assertTrue(lo1, "logout button  is  not present")
        print("logout button is present")


        #clicking logout for employee
        # clicking the login button
        lob1 = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[2]/div[1]/div[2]/div/div/div/a')
        lob1.click()
        time.sleep(5)


        #checking logout successfully or not
        m1=driver.current_url
        self.assertEqual("https://hashedin-frontend-urtjok3rza-wl.a.run.app",m1,"logout failed")
        print("logout successfully as employee")
        time.sleep(7)













                #
        # # username visible
        # a = driver.find_element(By.XPATH, '//input[@name="username"]')
        # print(a.text)
        # assert a.text != "username"
        # time.sleep(3)
        # # visible passwordfield
        # b = driver.find_element(By.XPATH, "//input[@name='password']")
        # print(b.text)
        # assert b.text != "password"
        # time.sleep(3)
        #
        # # visible login button
        # c = driver.find_element(By.XPATH, "//input[@id='login']")
        # print(c.text)
        # assert c.text != "login"
        #
        # driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/div/div[2]/div/form/div[1]/input').send_keys(
        #     "testemployee")
        #
        # # pass employee password
        # driver.find_element(By.XPATH, "//input[@name='password']").send_keys("employee")
        # time.sleep(3)
        # # click login button
        # driver.find_element(By.XPATH, "//input[@class='btn btn-block login-btn mb-4']").click()
        # time.sleep(3)
        # # logout
        # driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[1]/div[2]/div/div').click()  # dropdown
        # time.sleep(3)
        # driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[1]/div[2]/div/div/div').click()
        # time.sleep(9)
        #
        driver.quit()

