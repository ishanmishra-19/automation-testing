from datetime import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome("C:\\Users\\ishamishra\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://hashedin-frontend-urtjok3rza-wl.a.run.app/")

#username visible
a=driver.find_element(By.XPATH,"//input[@name='username']")
print(a.text)
assert a.text =="username"
#pass manager username
driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div[2]/div/form/div[1]/input').send_keys("testmanager")
driver.maximize_window()
time.sleep(3)
#pass manager  password
driver.find_element(By.XPATH,'/html/body/div/div/main/div/div/div/div[2]/div/form/div[2]/input').send_keys("manager")
time.sleep(3)
#click login button
driver.find_element(By.XPATH,'/html/body/div/div/main/div/div/div/div[2]/div/form/input').click()
time.sleep(3)
#logout
driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[1]/div[2]/div/div').click()   #dropdown
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[2]/div[1]/div[2]/div/div/div').click()
time.sleep(9)


#-ve testcase
#pass manager username
driver.find_element(By.XPATH, '/html/body/div/div/main/div/div/div/div[2]/div/form/div[1]/input').send_keys("tesmanager")
driver.maximize_window()
time.sleep(3)
#pass manager  password
driver.find_element(By.XPATH,'/html/body/div/div/main/div/div/div/div[2]/div/form/div[2]/input').send_keys("manage")
time.sleep(3)
#click login button
driver.find_element(By.XPATH,'/html/body/div/div/main/div/div/div/div[2]/div/form/input').click()
time.sleep(3)

#click ok on popup

driver.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div/button').click()
driver.refresh()


## for employee

#def __init__(self):
  #  self.username = "testemployee"
  #  self.password = "employee"


#def employee_login(self):
    # change the creds here
   # self.username = "testemployee"
    ##self.password = "employee"
    #username = driver.find_element(by=By.ID, value="username")
    #username.click()
    #username.send_keys(self.username)
    #password = driver.find_element(by=By.ID, value="password")
    #password.click()
    #password.send_keys(self.password)
    #password.send_keys(Keys.RETURN)
driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/div/div[2]/div/form/div[1]/input').send_keys("testemployee")

time.sleep(3)
#pass employee password
driver.find_element(By.XPATH,'/html/body/div[1]').send_keys("employee")
time.sleep(3)
#click login button
driver.find_element(By.XPATH,'/html/body/noscript').click()
time.sleep(3)
#logout

