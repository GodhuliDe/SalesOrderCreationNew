
'''
Created on Nov 21, 2019

@author: ramyb
'''

from selenium.webdriver.common.by import By
from SaleOrder_Package.TestPackage.PageObject.Locators import Locator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from SaleOrder_Package.TestPackage.Generics.CommonFunctions import CommonFunctionLibrary 
from selenium.webdriver.support import expected_conditions as EC
import time
from SaleOrder_Package.Resources import myConfig
print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__,__name__,str(__package__)))

class Login(object):    
    
    def __init__(self,driver):
        self.driver=driver 
        self.wait = WebDriverWait(driver, 20)           
             
    def validateLogin(self):  
        self.driver.refresh()
        time.sleep(4)     
        WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.ID, Locator.validateLogo)))
        WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, Locator.navigationPane)))
        actPageTitle = self.driver.__getattribute__("title")
        if actPageTitle.upper() == "Dashboard -- Finance and Operations".upper():           
            print("Navigated to the expected page")          
        else:
            print("Error while navigating to expected page")
    
    def LoginIntoD365(self,UName,PWD):
        WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.ID, Locator.UserName)))
        self.UserName = self.driver.find_element(By.ID,Locator.UserName)
        self.UserName.send_keys(UName)
        WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.ID, Locator.nextButton)))
        self.NextButton = self.driver.find_element(By.ID,Locator.nextButton)
        self.NextButton.click();
        print("Entered the UserName")
        time.sleep(3)
        self.pwd=self.driver.find_element(By.XPATH,Locator.PasswordBox)
        self.pwd.send_keys(PWD)
        time.sleep(2)
        self.pwd.send_keys(Keys.ENTER)
        print("Entered the Password")
        WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, Locator.yesButton)))
        try:
            self.YesButton=self.driver.find_element(By.XPATH,Locator.yesButton)
            self.YesButton.click();               
        except Exception as e:
            print(e)     

    