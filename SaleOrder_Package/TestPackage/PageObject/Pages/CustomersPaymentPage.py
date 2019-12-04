'''
Created on Nov 22, 2019

@author: ramyb
'''
from selenium.webdriver.common.by import By
from SaleOrder_Package.TestPackage.PageObject.Locators import Locator
from SaleOrder_Package.TestPackage.Generics.CommonFunctions import CommonFunctionLibrary
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class CustomerPaymentsPg(object):    
    
    def __init__(self,driver):
        self.driver=driver            
        self.wait = WebDriverWait(driver, 60)
    
    def pleaseWaitPopup(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH,Locator.pleaseWaitstr)))
            time.sleep(1)
        except Exception as e:
            print (e)
    
    def selectPaymentMethod(self,cardType):
        try:
            time.sleep(2)
            self.wait.until(EC.element_to_be_clickable((By.XPATH,Locator.paymentMethodDropdown)))
            paymentMethodDropdownElement = self.driver.find_element_by_xpath(Locator.paymentMethodDropdown)
            paymentMethodDropdownElement.click()
            time.sleep(2)
            self.wait.until(EC.element_to_be_clickable((By.XPATH,Locator.paymentMethodFilter)))
            paymentMethodFilterElement = self.driver.find_element_by_xpath(Locator.paymentMethodFilter)
            paymentMethodFilterElement.click()
            time.sleep(1)
            self.wait.until(EC.element_to_be_clickable((By.NAME,Locator.paymentFilterTextbox)))
            paymentFilterTextboxElement = self.driver.find_element_by_name(Locator.paymentFilterTextbox)
            paymentFilterTextboxElement.click()
            paymentFilterTextboxElement.clear()
            time.sleep(2)
            paymentFilterTextboxElement.send_keys(cardType, Keys.ENTER)
            time.sleep(2)
            self.wait.until(EC.element_to_be_clickable((By.NAME,Locator.paymentMethodRecord)))
            paymentMethodRecordElement = self.driver.find_element_by_name(Locator.paymentMethodRecord)
            paymentMethodRecordElement.click()
            time.sleep(2)
            print("Selected Card Type as: "+cardType)
        except Exception as e:
            print (e)
            
    def selectCardNumber(self, cardName):
        try:
            time.sleep(2)
            self.wait.until(EC.element_to_be_clickable((By.XPATH,Locator.careNumberDrpDwn)))
            careNumberDrpDwnElement = self.driver.find_element_by_xpath(Locator.careNumberDrpDwn)
            careNumberDrpDwnElement.click()
            time.sleep(2)
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,Locator.cardHolderFilter)))
            cardHolderFilterElement = self.driver.find_element_by_css_selector(Locator.cardHolderFilter)
            cardHolderFilterElement.click()
            time.sleep(1)
            
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,Locator.cardHolderNameFilterTxtBx)))
            cardHolderNameFilterTxtBxElement = self.driver.find_element_by_css_selector(Locator.cardHolderNameFilterTxtBx)
            cardHolderNameFilterTxtBxElement.click()
            cardHolderNameFilterTxtBxElement.clear()
            time.sleep(2)
            cardHolderNameFilterTxtBxElement.send_keys(cardName, Keys.ENTER)
            time.sleep(2)
            self.wait.until(EC.element_to_be_clickable((By.NAME,Locator.creditCardname)))
            creditCardnameElement = self.driver.find_element_by_name(Locator.creditCardname)
            creditCardnameElement.click()
            time.sleep(2)
            print("Entered Card Number!!")
        except Exception as e:
            print (e)
            