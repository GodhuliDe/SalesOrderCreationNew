'''
Created on Nov 21, 2019

@author: ramyb
'''

from selenium.webdriver.common.by import By
from SaleOrder_Package.TestPackage.PageObject.Locators import Locator
from SaleOrder_Package.TestPackage.Generics.CommonFunctions import CommonFunctionLibrary
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class DashBrd(object):    
    
    def __init__(self,driver):
        self.driver=driver
        self.wait = WebDriverWait(driver, 20)           
        
    def clickLeftNavigationpane(self):
        try:
            time.sleep(2)
            navigationPaneButton = self.driver.find_element(By.XPATH,Locator.navigationPane)
            navigationPaneButton.click()
            print("Clicked on Left Navigation Pane!")
            time.sleep(4)
        except Exception as e:
            print (e)
            
    def clickModulesLink(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH,Locator.modulesLink)))        
            MLink = self.driver.find_element_by_xpath(Locator.modulesLink)
            LinkClass = MLink.get_attribute("class")
            while(not LinkClass.contains("isExpanded")):
                self.driver.find_element_by_xpath(Locator.moduleminimizedlink).click()
                print("clicked on Modules")
                break
            print("Clicked on Module link")
        except Exception as e:
            print (e)
    
    def clickSalesAndMarketingLink(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH,Locator.salesAndMarketingLink)))        
            time.sleep(2)
            SMLink = self.driver.find_element_by_xpath(Locator.salesAndMarketingLink)
            SM_Link = SMLink.get_attribute("aria-selected")
            if (SM_Link.lower() == "false"):
                self.driver.find_element_by_xpath(Locator.salesAndMarketingLink).click()
                time.sleep(2)
                print("clicked on Sales and Marketing Link")
        except Exception as e:
            print (e)
    
    def pleaseWaitPopup(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH,Locator.pleaseWaitstr)))
            time.sleep(1)
        except Exception as e:
            print (e)
             
    def clickAllSalesOrders(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH,Locator.allSalesOrdersLink)))
            self.driver.find_element_by_xpath(Locator.allSalesOrdersLink).click()
            time.sleep(2)
            print("clicked on All sales order link")
        except Exception as e:
            print (e)
    