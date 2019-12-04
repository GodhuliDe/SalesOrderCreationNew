'''
Created on Nov 21, 2019

@author: ramyb
'''

from TestPackage.PageObject.Pages.LoginPage import Login
from TestPackage.PageObject.Pages.DashBoard import DashBrd
from TestPackage.PageObject.Pages.CustomersPaymentPage import CustomerPaymentsPg
from TestPackage.Scripts.ExcelDriver import ExcelDriver
from TestPackage.TestBase.Environment import EnvironmentSetUp
from TestPackage.Generics.CommonFunctions import CommonFunctionLibrary
from selenium.webdriver.support.wait import WebDriverWait
from TestPackage.PageObject.Locators import Locator
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from TestPackage.PageObject.Pages.AllSalesOrdersPage import AllSalesOrderPage
 
class SalesOrderSingleLine(EnvironmentSetUp):
    
    def test_SalesOrderNumber(self):
        
        #Initializing TestCaseName, SheetName , driver
        TestCaseName="SalesOrder_SingleLine"
        driver =self.driver
        
        Excel = ExcelDriver()
        
        Environment = Excel.GetCellData(TestCaseName,"Environment","Data")
        URL = Excel.GetCellData(Environment,"Link","URL")
        UserName = Excel.GetCellData(TestCaseName,"UserName","Data")
        customerAccount = Excel.GetCellData(TestCaseName,"CustomerAccount","Data")
        
        ItemNumber = Excel.GetCellData(TestCaseName,"ItemNumber","Data")
        Quantity = Excel.GetCellData(TestCaseName,"Quantity","Data")
        MOD = Excel.GetCellData(TestCaseName,"DeliveryMode","Data")
        SalesTaxGroup = Excel.GetCellData(TestCaseName,"SalesTaxGroup","Data")
        Site = Excel.GetCellData(TestCaseName,"Site","Data")
        Warehouse = Excel.GetCellData(TestCaseName,"WareHouse","Data")
        ItemSalesTax = Excel.GetCellData(TestCaseName,"ItemSalesTax","Data")
        CardType = Excel.GetCellData(TestCaseName,"CardType","Data")
        CardHolderName = Excel.GetCellData(TestCaseName,"CardHolderName","Data")
        
        
        print(UserName)
        Password = Excel.GetCellData(TestCaseName,"Password","Data")
        print(Password)
        self.assertTrue(CommonFunctionLibrary.EnterURL(driver,URL,"Sign in to your account"))
        print("Navigated to the URL")
  
        #Login to D365 Application  
        login = Login(driver)
        login.LoginIntoD365(UserName, Password)
        login.validateLogin()
        print("Successfully Logged into the Application")
        
        dp = DashBrd(driver)
        dp.clickLeftNavigationpane()
        dp.clickSalesAndMarketingLink()
        dp.clickAllSalesOrders()
        
        so = AllSalesOrderPage(driver)
        so.clickNewButton()
        so.selectCustomerAccount(customerAccount)
        
        SalesOrderNumber = so.getSalesOrderNum()
        print("Sales Order generated is: "+SalesOrderNumber)
        
        so.clickOkBtn()
        
        print("-----ITEM CREATION-----")
        
        so.selectItem(ItemNumber)
        so.selectQuantity(Quantity)
        so.clickLineDetailsHeader()
        so.clickSetupTab()
        so.selectItemSalesTax(ItemSalesTax)
        so.selectSalestax(SalesTaxGroup)
        so.clickProductTab()
        so.selectStorageSite(Site)
        so.selectStorageWarehouse(Warehouse)
        so.clickDeliveryTab()
        so.selectModeOfDelevery(MOD)
        
        print("-----SALES ORDER PAYMENT-----")
        
        so.clickcompleteHeader()

        so.clickAddBtn()
        
        cp = CustomerPaymentsPg(driver)
        cp.selectPaymentMethod(CardType)
        
        cp.selectCardNumber(CardHolderName)
        so.clickOKButtonPayment()
        so.clickSubmitBtn()
        
        