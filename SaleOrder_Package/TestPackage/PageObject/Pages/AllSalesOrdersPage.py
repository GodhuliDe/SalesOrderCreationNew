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


class AllSalesOrderPage(object):    
    
    def __init__(self,driver):
        self.driver=driver            
        self.wait = WebDriverWait(driver, 60)
    
    def pleaseWaitPopup(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH,Locator.pleaseWaitstr)))
            time.sleep(1)
        except Exception as e:
            print (e)
                
    def clickNewButton(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH,Locator.newButton)))
            self.driver.find_element_by_xpath(Locator.newButton).click()
            time.sleep(2)
            AllSalesOrderPage.pleaseWaitPopup(self)
            print("Clicked on the New Button")
        except Exception as e:
            print (e)
                    
    def selectCustomerAccount(self, CustNumber):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH,Locator.custAccountTab)))
            self.driver.find_element_by_xpath(Locator.custAccountTab).send_keys(CustNumber)
            self.driver.find_element_by_xpath(Locator.custAccountTab).send_keys(Keys.TAB)
            time.sleep(2)
            self.wait.until(EC.element_to_be_clickable((By.XPATH,Locator.yes_Button)))
            self.driver.find_element_by_xpath(Locator.yes_Button).click()
            time.sleep(1)
            print("Selected the Customer Account: "+CustNumber)
            time.sleep(2)
        except Exception as e:
            print (e)   
    
    def selectGeneralTab(self):
        try:
            AllSalesOrderPage.pleaseWaitPopup(self)
            time.sleep(1)
            generalTabElement = self.driver.find_element_by_xpath(Locator.generalTab)
            self.driver.execute_script("arguments[0].scrollIntoView();", generalTabElement)
            self.wait.until(EC.element_to_be_clickable((By.XPATH,Locator.generalTab)))
            G_Tab = generalTabElement.get_attribute("aria-selected")
            if (G_Tab.lower() == "false"):
                generalTabElement.click()
                time.sleep(2)
                print("clicked on General Tab")
        except Exception as e:
            print (e)
            
    def getSalesOrderNum(self):
        try:
            salesOrderNumElement  = self.driver.find_element_by_name(Locator.salesOrderNum)
            salesOrder = salesOrderNumElement.get_attribute("title")
            length = len(salesOrder)-22
            salesNum = salesOrder[0:length]
            print(salesNum)
            return salesNum
        except Exception as e:
            print (e)
            
    def clickOkBtn(self):
        try:
            time.sleep(1)
            self.driver.find_element_by_xpath(Locator.custAccountTab).send_keys(Keys.ALT,Keys.ENTER)
            time.sleep(1)
            AllSalesOrderPage.pleaseWaitPopup(self)
        except Exception as e:
            print (e)
    
    def clickOKButtonPayment(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH,Locator.okpaymentBtn)))
            time.sleep(1)
            self.driver.find_element_by_xpath(Locator.okpaymentBtn).click()
            time.sleep(1)
            print("Clicked on Ok Button")
        except Exception as e:
            print (e)
    
    def selectItem(self, ItemNbr):
        try:
            time.sleep(3)
            self.wait.until(EC.element_to_be_clickable((By.XPATH,Locator.itemnumberTextB)))
            itemnumberTextBox = self.driver.find_element_by_xpath(Locator.itemnumberTextB)
            time.sleep(2)
            itemnumberTextBox.click()
            itemnumberTextBox.send_keys(str(ItemNbr),Keys.ENTER)
            time.sleep(2)
            print("Entered the Item Number as: "+ItemNbr)
        except Exception as e:
            print (e)   
                 
    def selectItemMulti(self, ItemNbr,LoopVar):
        try:
            time.sleep(2)
            self.wait.until(EC.element_to_be_clickable((By.XPATH,"(//input[@name='SalesLine_ItemId'])["+str(LoopVar+1)+"]")))
            itemnumberTextBox = self.driver.find_element_by_xpath("(//input[@name='SalesLine_ItemId'])["+str(LoopVar+1)+"]")
            time.sleep(1)
            itemnumberTextBox.click()
            itemnumberTextBox.send_keys(str(ItemNbr),Keys.ENTER)
            time.sleep(1)
            print("Entered the Item Number as: "+ItemNbr)
        except Exception as e:
            print (e)
    
    def selectQuantity(self, qty):
        try:
            itemQtyTextboxElment = self.driver.find_element_by_xpath(Locator.itemQtyTextbox)
            time.sleep(2)
            itemQtyTextboxElment.send_keys(str(qty),Keys.ENTER)
            time.sleep(2)
            print("Entered the Quantity as: "+qty)
        except Exception as e:
            print (e)
    
    def selectQuantityMulti(self, qty, LoopVar):
        try:
            itemQtyTextboxElment = self.driver.find_element_by_xpath("(//input[@name='SalesLine_SalesQty'])["+str(LoopVar+1)+"]")
            time.sleep(1)
            itemQtyTextboxElment.send_keys(str(qty),Keys.ENTER)
            time.sleep(1)
            print("Entered the Quantity as: "+qty)
        except Exception as e:
            print (e)
            
    def clickLineDetailsHeader(self):
        try:
            time.sleep(4)
            self.wait.until(EC.element_to_be_clickable((By.XPATH,Locator.lineDetailsHeader)))
            LineHeaderTab = self.driver.find_element_by_xpath(Locator.lineDetailsHeader)
            LH_Tab = LineHeaderTab.get_attribute("aria-expanded")
            if (LH_Tab.lower() == "false"):
                LineHeaderTab.click()
                time.sleep(2)
                print("clicked on Line Header Tab")
        except Exception as e:
            print (e)
    
    def clickSetupTab(self):
        try:
            time.sleep(4)
            self.wait.until(EC.element_to_be_clickable((By.XPATH,Locator.setupTab)))
            setupTabElement = self.driver.find_element_by_xpath(Locator.setupTab)
            time.sleep(2)
            setupTabElement.click()
            print("Clicked on Setup Tab!")
        except Exception as e:
            print (e)
    
    def selectItemSalesTax(self,SalesTax):
        try:
            time.sleep(2)
            self.wait.until(EC.element_to_be_clickable((By.XPATH,Locator.itemSalesTextBox)))
            itemSalesTextBoxElement = self.driver.find_element_by_xpath(Locator.itemSalesTextBox)
            itemSalesTextBoxElement.click()
            itemSalesTextBoxElement.clear() 
            time.sleep(2)
            itemSalesTextBoxElement.send_keys(str(SalesTax), Keys.ENTER)
            time.sleep(2)
            print("Entered Item Sales Tax")
        except Exception as e:
            print (e)
    
    
    def selectSalestax(self, taxgroup):
        try:
            time.sleep(2)
            self.wait.until(EC.element_to_be_clickable((By.NAME,Locator.SalesTaxGroupBox)))
            SalesTaxGroupBoxElement = self.driver.find_element_by_name(Locator.SalesTaxGroupBox)
            SalesTaxGroupBoxElement.click()
            SalesTaxGroupBoxElement.clear() 
            time.sleep(2)
            SalesTaxGroupBoxElement.send_keys(str(taxgroup), Keys.ENTER)
            time.sleep(2)
            print("Entered Sales Tax Group")
        except Exception as e:
            print (e)
    
    
    def selectStorageSite(self, site):
        try:
            time.sleep(2)
            self.wait.until(EC.element_to_be_clickable((By.NAME,Locator.storageSiteBox)))
            storageSiteBoxElement = self.driver.find_element_by_name(Locator.storageSiteBox)
            storageSiteBoxElement.click()
            time.sleep(1) 
            storageSiteBoxElement.clear()
            storageSiteBoxElement.send_keys(str(site), Keys.TAB)
            time.sleep(1)
            print("Entered Site as "+site)
        except Exception as e:
            print (e)
    
    def selectStorageSiteMulti(self, site):
        try:
            time.sleep(2)
            self.wait.until(EC.element_to_be_clickable((By.NAME,Locator.storageSiteBox)))
            storageSiteBoxElement = self.driver.find_element_by_name(Locator.storageSiteBox)
            storageSiteBoxElement.click()
            time.sleep(1) 
            storageSiteBoxElement.send_keys(Keys.CONTROL, "a")
            time.sleep(1) 
            storageSiteBoxElement.send_keys(Keys.DELETE)
            time.sleep(2) 
            storageSiteBoxElement.send_keys(str(site), Keys.TAB)
            time.sleep(1)
            print("Entered Site as "+site)
        except Exception as e:
            print (e)
    
    def selectStorageWarehouse(self, warehouse):
        try:
            time.sleep(2)
            self.wait.until(EC.element_to_be_clickable((By.NAME,Locator.storageWarehouseBox)))
            storageWarehouseBoxElement = self.driver.find_element_by_name(Locator.storageWarehouseBox)
            storageWarehouseBoxElement.click()
            time.sleep(2) 
            storageWarehouseBoxElement.clear() 
            time.sleep(2)
            storageWarehouseBoxElement.send_keys(str(warehouse), Keys.TAB)
            time.sleep(2)
            print("Entered Warehouse as : "+warehouse)
        except Exception as e:
            print (e)
        
    def clickDeliveryTab(self):
        try:
            time.sleep(2)
            self.wait.until(EC.element_to_be_clickable((By.XPATH,Locator.deliveryTab)))
            deliveryTabElement = self.driver.find_element_by_xpath(Locator.deliveryTab)
            deliveryTabElement.click() 
            time.sleep(2)
            print("Clicked on Delivery Tab")
        except Exception as e:
            print (e)
            
    def selectModeOfDelevery(self, MOD):
        try:
            time.sleep(2)
            self.wait.until(EC.element_to_be_clickable((By.XPATH,Locator.modeOfDelivery)))
            modeOfDeliveryElement = self.driver.find_element_by_xpath(Locator.modeOfDelivery)
            modeOfDeliveryElement.click()
#             modeOfDeliveryElement.clear() 
            modeOfDeliveryElement.send_keys(str(MOD), Keys.TAB)
            time.sleep(2)
            print("Entered Mode of Delivery")
        except Exception as e:
            print (e)
    
    def clickProductTab(self):
        try:
            time.sleep(2)
            self.wait.until(EC.element_to_be_clickable((By.XPATH,Locator.productTab)))
            productTabElement = self.driver.find_element_by_xpath(Locator.productTab)
            productTabElement.click() 
            time.sleep(2)
            print("Clicked on Product Tab")
        except Exception as e:
            print (e)
            
    def clickSave(self):
        try:
            time.sleep(1)
            self.wait.until(EC.element_to_be_clickable((By.XPATH,Locator.saveButton)))
            saveButtonElement = self.driver.find_element_by_xpath(Locator.saveButton)
            saveButtonElement.click() 
            time.sleep(2)
            time.sleep(1)
            AllSalesOrderPage.pleaseWaitPopup(self)
            print("Clicked on Save Button")
        except Exception as e:
            print (e)
        
    def clickcompleteHeader(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH,Locator.completeHeader)))
            completeHeaderElement = self.driver.find_element_by_xpath(Locator.completeHeader)
            time.sleep(4)
            completeHeaderElement.click() 
            time.sleep(2)
            time.sleep(1)
            print("Clicked on Complete Header")
        except Exception as e:
            print (e)
    
    def clickPaymentBlade(self):
        try:
            time.sleep(1)
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,Locator.paymentBlade)))
            paymentBladeElement = self.driver.find_element_by_css_selector(Locator.paymentBlade)
            paymentBladeElement.double_click() 
            time.sleep(2)
            time.sleep(1)
            print("Clicked on Payment Blade")
        except Exception as e:
            print (e)
            
    def clickAddBtn(self):
        try:
            time.sleep(1)
            self.wait.until(EC.element_to_be_clickable((By.NAME,Locator.addButton)))
            addButtonElement = self.driver.find_element_by_name(Locator.addButton)
            addButtonElement.click() 
            time.sleep(3)
            print("Clicked on Add Button")
        except Exception as e:
            print (e)
            
    def clickSubmitBtn(self):
        try:
            time.sleep(1)
            self.wait.until(EC.element_to_be_clickable((By.NAME,Locator.submitBtn)))
            submitBtnElement = self.driver.find_element_by_name(Locator.submitBtn)
            submitBtnElement.click() 
            time.sleep(2)
            time.sleep(1)
            AllSalesOrderPage.pleaseWaitPopup(self)
            print("Clicked on Submit Button")
        except Exception as e:
            print (e)
            
            
    #for MultiLine        
    def ClickAddLineSearchedItem(self):
        try:
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable((By.XPATH, Locator.addSOlineBtn)))
            self.driver.find_element_by_xpath(Locator.addSOlineBtn).click()
            time.sleep(2)
            print("Clicking on +AddLine SO Searched Item");
            
        except Exception as e:
            print (e)   