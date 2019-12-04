
import unittest
import pytest_forked
from selenium import webdriver
import datetime
from SaleOrder_Package.Resources.myConfig import RootDirectory
from SaleOrder_Package.TestPackage.Generics.CommonFunctions import CommonFunctionLibrary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class EnvironmentSetUp(unittest.TestCase):
    #Setup contains the browser setup attributes
    def setUp(self): 
        print("Execution STARTED")
        executable_path = RootDirectory+"\\\\Resources\\\\chromedriver.exe"
        print(executable_path)
        capabilities = DesiredCapabilities.CHROME.copy()
        optionss = webdriver.ChromeOptions()
        optionss.add_argument('window-size=1920x1080')
        optionss.add_argument('--ignore-certificate-errors')
        optionss.accept_untrusted_certs = True
        optionss.assume_untrusted_cert_issuer = True
        self.driver = webdriver.Chrome(executable_path=executable_path,options= optionss)           
#         self.driver = webdriver.Chrome(executable_path)    
#         self.driver.maximize_window()
        
        print("Run started at :"+str(datetime.datetime.now()))
        print("Chrome Environment set up")
        print("---------------------------------------------------------------------------------")
    
    
    #tearDown method to close the browser instance and then quit
    def tearDown(self):
        if(self.driver != None):
            print("---------------------------------------------------------------------------------")
            print("Test Environment closed")
            print("Run Completed at :"+str(datetime.datetime.now()))
            self.driver.quit()



