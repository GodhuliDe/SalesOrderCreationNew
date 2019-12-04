'''
Created on Nov 25, 2019

@author: godde
'''


from SaleOrder_Package.TestPackage.PageObject.Pages.LoginPage import Login
from SaleOrder_Package.TestPackage.PageObject.Pages.DashBoard import DashBrd
from SaleOrder_Package.TestPackage.PageObject.Pages.CustomersPaymentPage import CustomerPaymentsPg
from SaleOrder_Package.TestPackage.Scripts.ExcelDriver import ExcelDriver
from SaleOrder_Package.TestPackage.TestBase.Environment import EnvironmentSetUp
from SaleOrder_Package.TestPackage.Generics.CommonFunctions import CommonFunctionLibrary
from selenium.webdriver.support.wait import WebDriverWait
from SaleOrder_Package.TestPackage.PageObject.Locators import Locator
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
import pytest_parallel

from SaleOrder_Package.TestPackage.PageObject.Pages.AllSalesOrdersPage import AllSalesOrderPage
print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__,__name__,str(__package__)))
 
class test_SalesOrderMultiLine(EnvironmentSetUp):
    
#     @pytest.mark.parametrize("count",[1,2,3])
    def test_SalesOrderMultiLine(self):
        
        #Initializing TestCaseName, SheetName , driver
        TestCaseName="test_SalesOrderMultiLine"
        driver =self.driver
        
        Excel = ExcelDriver()
        
        Environment = Excel.GetCellData("test_SalesOrderMultiLine","Environment","Data")
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
        ItemCount=Excel.GetCellData(TestCaseName,"ItemCount","Data")
        print("type")
        print(type(ItemCount))
        print(ItemCount)
        ItemCount=int(ItemCount)
        ItemN=ItemNumber.split("|")
        Qty=Quantity.split("|")
        SiteV=Site.split("|")
        WarehouseV=Warehouse.split("|")
        DeliveryMode=MOD.split("|")
        SalesTaxGroup=SalesTaxGroup.split("|")
        ItemSalesTax=ItemSalesTax.split("|")
        
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
       
        
        for i in range(0,ItemCount):
         
            so.selectItemMulti(ItemN[i],i)
            so.selectQuantityMulti(Qty[i],i)
            so.clickLineDetailsHeader()
            so.clickSetupTab()
            so.selectItemSalesTax(ItemSalesTax[i])
            so.selectSalestax(SalesTaxGroup[i])
            so.clickProductTab()
            so.selectStorageSiteMulti(SiteV[i])
            so.selectStorageWarehouse(WarehouseV[i])
            so.clickDeliveryTab()
            so.selectModeOfDelevery(DeliveryMode[i])
            
            if i!=ItemCount-1 :
                so.ClickAddLineSearchedItem()
        
        
        print("-----SALES ORDER PAYMENT-----")
        
        so.clickcompleteHeader()

        so.clickAddBtn()
        
        cp = CustomerPaymentsPg(driver)
        cp.selectPaymentMethod(CardType)
        
        cp.selectCardNumber(CardHolderName)
        so.clickOKButtonPayment()
        so.clickSubmitBtn()
            