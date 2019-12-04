from datetime import datetime
import os
import pyautogui
import traceback
from SaleOrder_Package.Resources import myConfig
import pyodbc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
# import requests
class CommonFunctionLibrary(object):
    
    global TimeDateFolder
    global ScreenshotPath
    global filePath
    global file1        
    global ScreenshotPath
    global HeaderDetails
    global f
    global r
    driver=None
    PathOfScreenshot=""    
    ResultsFolderPath=myConfig.ResultFolderPath
    TimeDateFolder= datetime.now().strftime("%Y%m%d_%H%M%S")    
    filePath=ResultsFolderPath+"\\"+ TimeDateFolder      
    ScreenshotPath = filePath+"\\Screenshots"
    FileNameHTML = ""
    IndividualHTMLResultFileName = ""
    StepNum=0
    HTMLResultPath = ""      
    HeaderDetails = "" 
    
    #******************************************************************************************************************
    #Variables accessible in ReportEventFunction
    ReporterResultPath=ResultsFolderPath+"\\\\"+TimeDateFolder+"\\\\" # This variable is assigned, so that it is accessible in ReportEventFunction
    ReporterScreenshotPath=ResultsFolderPath+"\\\\"+ TimeDateFolder+"\\\\Screenshots\\\\" # This variable is assigned, so that it is accessible in ReportEventFunction     
    ScreenshotPath=ReporterScreenshotPath
    HTMLReportPath=ReporterResultPath
    strHRMLReport = HTMLReportPath.replace('\\','/')
    HTMLResultPath = strHRMLReport.replace("//","/")
    #********************************************************************************************************************
    HeaderDetails = """<html>
    <head> 
    <meta http-equiv=X-UA-Compatible content=IE=edge> 
    <title>CAWS_LAR.CAWS.CIT.0001_sourcelowes.com Automation Execution Results</title>
    <style type='text/css'>
    body { background-color: #FFFFFF; font-family: Verdana, Geneva, sans-serif; text-align: center; } small { font-size: 0.7em; }table { box-shadow: 9px 9px 10px 4px #BDBDBD;border: 0px solid #4D7C7B; border-collapse: collapse;border-spacing: 0px; width: 1000px; margin-left: auto; margin-right: auto; }tr.heading { background-color: #041944;color: #FFFFFF; font-size: 0.7em; font-weight: bold;} tr.subheading { background-color: #FFFFFF; color: #000000;font-weight: bold; font-size: 0.7em; text-align: justify; } tr.section { background-color: #A4A4A4; color: #333300; cursor: pointer; font-weight: bold; font-size: 0.7em; text-align: justify; background:-o-linear-gradient(bottom, #56aaff 5%, #e5e5e5 100%);background:-webkit-gradient( linear, left top, left bottom, color-stop(0.05, #56aaff), color-stop(1, #e5e5e5));background:-moz-linear-gradient( center top, #56aaff 5%, #e5e5e5 100%);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#56aaff, endColorstr=#e5e5e5);background: -o-linear-gradient(top,#56aaff,e5e5e5);}tr.subsection { cursor: pointer; } tr.content { background-color: #FFFFFF;color: #000000; font-size: 0.7em; display: table-row; } tr.content2 { background-color: #E1E1E1; border: 1px solid #4D7C7B;color: #000000; font-size: 75%; display: table-row; } td, th { padding: 5px; border: 1px solid #4D7C7B; text-align: inherit /; } th.Logos { padding: 5px; border: 0px solid #4D7C7B; text-align: inherit /;} td.justified { text-align: Center; font-size: 110%; } td.pass { font-weight: bold; color: green; } td.fail { font-weight: bold; color: red; }td.done, td.screenshot { font-weight: bold; color: black; } td.debug { font-weight: bold;color: blue; } td.warning { font-weight: bold; color: orange; } </style>
    </head><body></br><table id='Logos'><colgroup><col style='width: 25%' /><col style='width: 25%' /><col style='width: 25%' />
    <col style='width: 25%' /></colgroup><thead><tr class='content'><th class ='Logos' colspan='2' >
    <img align ='center' src='https://lda.lowes.com/is/image/Lowes/NSI_Lowes_logo_no_tagline?$JPEG-HQ$&wid=147'></img>
    </th></tr></thead></table><table id='header'><colgroup><col style='width: 25%' />    <col style='width: 25%' />
    <col style='width: 25%' /> <col style='width: 25%' /></colgroup><thead><tr class='heading'> 
    <th colspan='4' style='font-family:Copperplate Gothic Bold;font-size:1.4em;'> **Remedy Automation Execution Results **</th> 
    </tr><tr class='subheading'><th align='left'>&nbsp;Date&nbsp;&&nbsp;Time:&nbsp;"""+datetime.now().strftime("%d/%m/%Y %H:%M:%S %p")+"""</th>
    <th align='Right'>Operating&nbsp;System&nbsp;:&nbsp;Microsoft Windows 7 Workstation&nbsp;&nbsp;&nbsp;</th>
    </tr></thead></table><table id='main'><colgroup><col style='width: 5%' /><col style='width: 26%' /><col style='width: 51%' /> 
    <col style='width: 8%' /><col style='width: 10%' /></colgroup><thead><tr class='heading'><th>S.NO</th> <th>Steps</th> <th>Details</th><th>Status</th><th>Time</th>
    </tr></html>"""
    def __init__(self,driver= None):
        self.driver=driver


    @staticmethod
    def Reporter(TestCaseName):                    
        FileNameHTML = TestCaseName+'.html'
        IndividualHTMLResultFileName= CommonFunctionLibrary.HTMLResultPath+FileNameHTML                  
        CommonFunctionLibrary.f = open(IndividualHTMLResultFileName,"w+")    
    
    '''**********************************************************************************************************************************************************************
    Function Name      : getScreenshot
    Input Parameters   : N/A
    Output Parameters  : ScreenshotPATH -  Returns the path of the folder where screenshots will be stored
    Description        : It will capture the screenshot and returns the Screenshot PATH
    Version            : 1.0
    Author             : Keerthi
    Modified           : MohanParasuraam
    *************************************************************************************************************************************************************************'''  
    @staticmethod
    def getScreenshot():                
        img = pyautogui.screenshot()
        #ScreenshotName=  "//"+SnshotName+".png"   
        ScreenshotName =datetime.now().strftime("%Y%m%d_%H%M%S")+".png"
        img.save(ScreenshotPath+ScreenshotName)
        absoluteScreenshotPath= ScreenshotPath+ScreenshotName
        absoluteScreenshotPath1 = absoluteScreenshotPath.replace('\\','/')
        ScreenshotPATH = absoluteScreenshotPath1.replace("//","/")
        img=""        
        return ScreenshotPATH 

    '''**********************************************************************************************************************************************************************
    Function Name      : ReportEvent
    Input Parameters   : 1.Description -  Pass the description of the step
                        2. Status - Pass the status of the step
                        3. TakeScreenshot - (Optional) -  By default it is set to "NO",User should explicitly specify "YES"- if screenshot is required
    Output Parameters  : N.A
    Description        : This function will write the steps to the respective HTML file
    Version            : 1.0
    Author             : Keerthi
    Last Modified      : MohanParasuraam(6-June-2018,18-June-2018)
    *************************************************************************************************************************************************************************'''
    @staticmethod
    def ReportEvent(Description,Status,TakeScreenshot="NO"):        
        CommonFunctionLibrary.StepNum += 1
        if CommonFunctionLibrary.StepNum == 1:            
            CommonFunctionLibrary.f.write(HeaderDetails)             
        DataToWrite1 ="""<tr bgcolor='#8B9292'>
        <td colspan='5'><center><b>
        </center></b>
        </td>
        </tr>
        <tr class='content2'>
        <td class='justified'>"""+str(CommonFunctionLibrary.StepNum)+"""</td> <td class='justified'> Step-"""+str(CommonFunctionLibrary.StepNum)+"""</td> <td class='justified'>"""+Description+"""</td>"""
        if TakeScreenshot.upper() == "YES":
            PathOfScreenshot=CommonFunctionLibrary.getScreenshot()
            print(PathOfScreenshot)
            if Status.upper() == "PASS":
                print("Entered the loop")
                DataToWrite2="""<td class='Pass' align='center'><a href='.."""+PathOfScreenshot.split('Results')[-1]+"""' target='_blank'><img  src= https://openclipart.org/download/159733/green-tick.svg  width='30' height='30'/></a></td><td class='justified'>"""+datetime.now().strftime("%H:%M:%S %p")+"""</td> </tr>"""
            elif Status.upper() == "FAIL":
                DataToWrite2="""<td class='Fail' align='center'><a href='.."""+PathOfScreenshot.split('Results')[-1]+"""' target='_blank'><img  src= https://openclipart.org/download/166859/red-cross.svg  width='30' height='30'/></a></td><td class='justified'>"""+datetime.now().strftime("%H:%M:%S %p")+"""</td> </tr>"""
            elif Status.upper() == "STOP":
                DataToWrite2="""<td class='Fail' align='center'><a href='.."""+PathOfScreenshot.split('Results')[-1]+"""' target='_blank'><img  src= https://openclipart.org/download/46213/Stop-02-Sign.svg  width='30' height='30'/></a></td><td class='justified'>"""+datetime.now().strftime("%H:%M:%S %p")+"""</td> </tr>"""
                CommonFunctionLibrary.fileClose()
        else:
            if Status.upper() == "PASS":
                DataToWrite2="""<td class='Pass' align='center'><img  src= https://openclipart.org/download/159733/green-tick.svg  width='30' height='30'/></td><td class='justified'>"""+datetime.now().strftime("%H:%M:%S %p")+"""</td> </tr>"""
            elif Status.upper() == "FAIL":
                DataToWrite2="""<td class='Fail' align='center'><img  src= https://openclipart.org/download/166859/red-cross.svg  width='30' height='30'/></td><td class='justified'>"""+datetime.now().strftime("%H:%M:%S %p")+"""</td> </tr>"""
            elif Status.upper() == "STOP":   
                DataToWrite2="""<td class='Fail' align='center'><img  src= https://openclipart.org/download/46213/Stop-02-Sign.svg  width='30' height='30'/></td><td class='justified'>"""+datetime.now().strftime("%H:%M:%S %p")+"""</td> </tr>"""
                CommonFunctionLibrary.fileClose() 
        CommonFunctionLibrary.f.write(DataToWrite1+DataToWrite2)
    
    '''**********************************************************************************************************************************************************************
    Function Name      : fileClose
    Input Parameters   : N.A
    Output Parameters  : N.A
    Description        : This function will close the HTML file which is opened
    Version            : 1.0
    Author             : MohanParasuraam
    *************************************************************************************************************************************************************************'''
    @staticmethod
    def fileClose():
        CommonFunctionLibrary.f.close()
        CommonFunctionLibrary.StepNum=0
    '''************************************************************************************************************************
    Function Name      : getFolderToStoreResults
    Input Parameters   : N/A  
    Output Parameters  : filePath - It returns the filepath where the results can be stored 
    Description        : Takes the screenshot by addressing with the specified name    
    Version            : 1.0
    ************************************************************************************************************************''' 
    @staticmethod   
    def getFolderToStoreResults():        
        os.mkdir(filePath)
        os.mkdir(filePath+"\\Screenshots")
        return filePath 
    '''************************************************************************************************************************
    Function Name      : EnterURL
    Input Parameters   : 1. url -  Specify the URL to navigate to 
                         2. expectedPageTitle - Specify the title of expected page
    Output Parameters  : Boolean Value - return true or false 
    Description        : Navigates to the specified URL and validates the page title   
    Version            : 1.0
    ************************************************************************************************************************'''
    @staticmethod
    def EnterURL(driver,url,expectedPageTitle):
        driver.get(url)
        time.sleep(3)
        actPageTitle = driver.__getattribute__("title")
        #self.assertEqual(actPageTitle.upper(), expectedPageTitle.upper(), "Navigated to the expected page")        
        #self.ObjunitTestCase.assertEqual(actPageTitle.upper(), expectedPageTitle.upper(), "Navigated to the expected page")  
        if actPageTitle.upper() == expectedPageTitle.upper():           
            print("Navigated to the expected page")          
            return True
        else:
            print("Error while navigating to expected page")
#             CommonFunctionLibrary.ReportEvent("Unable to Navigate to expected page", "FAIL", "YES")  
            return False
        
    '''************************************************************************************************************************
    Function Name      : waitForElementToBeClickable
    Input Parameters   : 1. driver -  pass the driver instance object 
                         2. XPATH_LocatorVal - Specify the XPATH Locator value
    Output Parameters  : N/A
    Description        : Wait for the element to be clickable until the specified interval of time  
    Version            : 1.0
    ************************************************************************************************************************'''    
    def waitForElementToBeClickable(self,driver,XPATH_LocatorVal):
        wait = WebDriverWait(driver,60)
        try:            
            wait.until(EC.element_to_be_clickable(By.XPATH,XPATH_LocatorVal))        
        except Exception as e:
            print(e)
    
    
    
    '''************************************************************************************************************************
    Function Name      : GetTestCases
    Input Parameters   : SheetName -  Specify the sheetname from where data needs to be fetched                         
    Output Parameters  : Values - Returns the values of test case names to execute
    Description        : Gets the test case names which needs to be executed  
    Version            : 1.0
    Author            : Ramya B
    **********************************************************************************************************************'''
    def GetTestCases(self,SheetName):
        try:
            Values=[]
            ExcelPath=myConfig.RunManagerPath
            xl_workbook = pd.ExcelFile(ExcelPath)  # Load the excel workbook
            df = xl_workbook.parse(myConfig.SheetName)  # Parse the sheet into a dataframe
            aList = df.loc[df.Execute == 'YES', 'TestCase']
            print(aList)       
        except Exception as e:   
            print("Exception Raised :"+ e)
    
    
    '''************************************************************************************************************************
    Function Name      : GetCellData
    Input Parameters   : 1. TestCaseName -  Test case name from where data needs to be fetched
                         2. ColumnName - Name of the column to fetch the data for
                         3. SheetName - Specify the sheet name
    Output Parameters  : ValueToFetch[0][0] - Returns the value from the specified cell
    Description        : Gets the specified cell value based on the test case name, sheet  and column name  
    Version            : 1.0
    **********************************************************************************************************************'''   
    @staticmethod
    def GetCellData(TestCaseName,ColumnName,SheetName):
        try:            
            con = ("Driver={Microsoft Excel Driver (*.xls)};DBQ="+myConfig.TestDataPath+";ReadOnly = True;")        
            Query = "Select "+ ColumnName +" from ["+SheetName+"$] where TestCase = '"+TestCaseName+"'"            
            cnxn = pyodbc.connect(con, autocommit=True)
            cursor= cnxn.cursor()
            cursor.execute(Query)
            ValueToFetch = cursor.fetchall()            
            return ValueToFetch[0][0]            
            
        except Exception as e:
            print(e)
        cnxn.close()


#****************************************************************************************
    #Function Name : Web_Click
    #Description   : Function to click on any Web Element
    #Author        : Idris
    #Parameters    : Driver,Property Type and Property Value
    #****************************************************************************************
    @staticmethod
    def Web_Click(driver,p_propertyType,p_propertyValue):
        CommonFunctionLibrary.Web_Wait(driver, p_propertyType, p_propertyValue, "CLICK")
        try:
            eval("driver.find_element(By." + p_propertyType + "," + chr(34) + p_propertyValue + chr(34) + ").click()")
            return True
        except Exception as e:
            CommonFunctionLibrary.ReportEvent("Web_Click : Unable to click on the element of "+ p_propertyType + ": " + p_propertyValue, "FAIL", "YES") 
            print(e)
            
    #****************************************************************************************
    #Function Name : Web_Set
    #Description   : Function to Set a value in any Web Edit
    #Author        : Idris
    #Parameters    : Driver,Property Type and Property Value and text value
    #****************************************************************************************
    @staticmethod
    def Web_Set(driver,p_propertyType,p_propertyValue,p_InputText):
        CommonFunctionLibrary.Web_Wait(driver, p_propertyType, p_propertyValue, "CLICK")
        try:
            eval("driver.find_element(By." + p_propertyType + "," + chr(34) + p_propertyValue + chr(34) + ").send_keys(" + chr(34) + p_InputText + chr(34) + ")")
        except Exception as e:
            CommonFunctionLibrary.ReportEvent("Web_Set : Unable to set value for the element of "+ p_propertyType + ": " + p_propertyValue, "FAIL", "YES")
            print(e)
            
            
    #****************************************************************************************
    #Function Name : Web_GetValue
    #Description   : Function to Get a value from a WebElement
    #Author        : Idris
    #Parameters    : Driver,Property Type and Property Value and text value
    #****************************************************************************************
    @staticmethod
    def Web_GetValue(driver,p_propertyType,p_propertyValue):
        CommonFunctionLibrary.Web_Wait(driver, p_propertyType, p_propertyValue, "EXIST")
        try:
            value = eval("driver.find_element(By." + p_propertyType + "," + chr(34) + p_propertyValue + chr(34) + ").get_attribute('value')")
            if value == None:
                value = eval("driver.find_element(By." + p_propertyType + "," + chr(34) + p_propertyValue + chr(34) + ").get_attribute('textContent')")
            return value
        except Exception as e:
            CommonFunctionLibrary.ReportEvent("Web_GetValue : Unable to Get value for the element of "+ p_propertyType + ": " + p_propertyValue, "FAIL", "YES")
            print(e)
            
    
    #****************************************************************************************
    #Function Name : Web_Select
    #Description   : Function to Set a value in any WebEdit
    #Author        : Idris
    #Parameters    : Driver,Property Type and Property Value and text value
    #****************************************************************************************
    @staticmethod
    def Web_Select(driver,p_propertyType,p_propertyValue,p_selectValue):
        objFunctionLibrary = CommonFunctionLibrary(driver)
        objFunctionLibrary.Web_Wait(driver, p_propertyType, p_propertyValue, "CLICK")
        try:
            WebObject = eval("driver.find_element(By." + p_propertyType + "," + chr(34) + p_propertyValue + chr(34) + ")")
            select = Select(WebObject)
            select.select_by_visible_text(p_selectValue)
            print("Selected :" + p_selectValue + " from weblist having "+ p_propertyType + ": " + p_propertyValue)
        except Exception as e:
            CommonFunctionLibrary.ReportEvent("Web_Select : Unable to Select value for the element of "+ p_propertyType + ": " + p_propertyValue, "FAIL", "YES")
            print(e)
            
            

   
    #****************************************************************************************
    #Function Name : Web_Wait
    #Description   : Function to wait for any WebElement
    #Author        : Idris
    #Parameters    : Driver,Property Type and Property Value
    #****************************************************************************************
    @staticmethod
    def Web_Wait(driver,p_propertyName,p_propertyValue,p_status):
        wait = WebDriverWait(driver,60)
        p_status = p_status.upper()
        l_statusArray = ["CLICK","EXIST"]
        if (p_status in l_statusArray):
            pass
        else:
            CommonFunctionLibrary.ReportEvent("Enter the valid status of the object for the function Web_Wait", "FAIL", "NO")
            print("Enter the valid status of the object for the function Web_Wait")
            return
        if p_status == "EXIST":
            try:
                eval("wait.until(EC.presence_of_element_located((By." + p_propertyName + "," + chr(34) + p_propertyValue + chr(34) + ")))")
            except Exception as e:
                print(e)
        elif p_status == "CLICK":
            try:
                eval("wait.until(EC.element_to_be_clickable((By." + p_propertyName + "," + chr(34) + p_propertyValue + chr(34) + ")))")
            except Exception as e:
                print(e)
                
                
    #****************************************************************************************
    #Function Name : Web_IsExist
    #Description   : Function to check existence of any WebElement
    #Author        : Idris
    #Parameters    : Driver,Property Type and Property Value
    #****************************************************************************************
    @staticmethod
    def Web_IsExist(driver,p_propertyName,p_propertyValue):
        wait = WebDriverWait(driver,60)
        try:
            eval("wait.until(EC.presence_of_element_located((By." + p_propertyName + "," + chr(34) + p_propertyValue + chr(34) + ")))")
            return True
        except Exception as e:
            print(e)
            
            
    #****************************************************************************************
    #Function Name : Web_GetWindowTitle
    #Description   : Function to get the title of Browser
    #Author        : Idris
    #Parameters    : Driver
    #****************************************************************************************
    @staticmethod
    def Web_GetWindowTitle(driver):
        l_BrowserTitle = ""
        try:
            l_BrowserTitle = driver.find_element_by_tag_name("title").get_attribute('text')
        except Exception as e:
            print(e)
        return l_BrowserTitle
    
    #****************************************************************************************
    #Function Name : Web_Open
    #Description   : Function to open the URL
    #Author        : Idris
    #Parameters    : Driver
    #****************************************************************************************
    @staticmethod
    def Web_Open(driver,p_URL):
        try:
            driver.get(p_URL)
        except Exception as e:
            print(e)
            
            
    #****************************************************************************************
    #Function Name : Web_CloseBrowser
    #Description   : Function to close the Browser
    #Author        : Idris
    #Parameters    : Driver
    #****************************************************************************************
    @staticmethod
    def Web_CloseBrowser(driver):
        try:
            driver.close()
            driver.quit()
        except Exception as e:
            print(e)
            
    #****************************************************************************************
    #Function Name : Web_CountBrowsers
    #Description   : Function to count number of browsers
    #Author        : Idris
    #Parameters    : Driver
    #****************************************************************************************
    @staticmethod
    def Web_CountBrowsers(driver):
        l_BrowsersCount = ""
        try:
            l_BrowsersCount = len(driver.window_handles)
        except Exception as e:
            print(e)
        return l_BrowsersCount
    
    #****************************************************************************************
    #Function Name : Web_GetRowCount
    #Description   : Function to get the row count of a table
    #Author        : Preethi
    #Parameters    : Driver,PropertyType,PropertyValue
    #****************************************************************************************
    @staticmethod
    def Web_GetRowCount(driver,p_PropertyType,p_PropertyValue):
        l_RowCount = ""
        CommonFunctionLibrary.Web_Wait(driver, p_PropertyType, p_PropertyValue, "EXIST")
        try:
            WebObject = eval("driver.find_element(By." + p_PropertyType + "," + chr(34) + p_PropertyValue + chr(34) + ")")
            l_RowCount= len(WebObject.find_elements(By.TAG_NAME,"tr"))
            return l_RowCount
        except Exception as e:
            CommonFunctionLibrary.ReportEvent("Web_GetRowCount : Unable to get the Row count for the element of "+ p_PropertyType + ": " + p_PropertyValue, "FAIL", "YES")
            print(e)

    
    #****************************************************************************************
    #Function Name : Web_GetColumnCount
    #Description   : Function to get the column count for a particular row
    #Author        : Idris
    #Parameters    : Driver,Property Type,Property Value,Row Number
    #****************************************************************************************
    @staticmethod
    def Web_GetColumnCount(driver,p_PropertyType,p_PropertyValue,RowNumber):
        l_ColumnCount = ""
        CommonFunctionLibrary.Web_Wait(driver, p_PropertyType, p_PropertyValue, "EXIST")
        try:
            WebObject = eval("driver.find_element(By." + p_PropertyType + "," + chr(34) + p_PropertyValue + chr(34) + ")")
            l_ColumnCount = len(WebObject.find_elements(By.TAG_NAME,"tr")[RowNumber].find_elements(By.TAG_NAME,"td"))
            return l_ColumnCount
        except Exception as e:
            CommonFunctionLibrary.ReportEvent("Web_GetColumnCount : Unable to get the column count of Row " + RowNumber.convert_to_string() + " for the element of "+ p_PropertyType + ": " + p_PropertyValue, "FAIL", "YES")
            print(e)
            
            
    #****************************************************************************************
    #Function Name : Web_GetCellValue
    #Description   : Function to get the the value of particular cell in the webtable
    #Author        : Idris
    #Parameters    : Driver,Property Type,Property Value,Row Number
    #****************************************************************************************
    @staticmethod
    def Web_GetCellValue(driver,p_PropertyType,p_PropertyValue,RowNumber,ColumnNumber):
        l_CellValue = ""
        CommonFunctionLibrary.Web_Wait(driver, p_PropertyType, p_PropertyValue, "EXIST")
        try:
            WebObject = eval("driver.find_element(By." + p_PropertyType + "," + chr(34) + p_PropertyValue + chr(34) + ")")
            l_CellValue = WebObject.find_elements(By.TAG_NAME,"tr")[RowNumber].find_elements(By.TAG_NAME,"td")[ColumnNumber].get_attribute('textContent')
            return l_CellValue
        except Exception as e:
            CommonFunctionLibrary.ReportEvent("Web_GetCellValue : Unable to get the cell value of Row " + RowNumber.convert_to_string() + "column " + ColumnNumber.convert_to_string() + " for the element of "+ p_PropertyType + ": " + p_PropertyValue, "FAIL", "YES")
            print(e)
            
            
    #****************************************************************************************
    #Function Name : Web_GetRowWithCellText
    #Description   : Function to get the row of particular cell in the webtable
    #Author        : Idris
    #Parameters    : Driver,Property Type,Property Value,CellText
    #****************************************************************************************
    @staticmethod
    def Web_GetRowWithCellText(driver,p_PropertyType,p_PropertyValue,p_CellText):
        l_CellText = ""
        l_TextExist = "NotExist"
        CommonFunctionLibrary.Web_Wait(driver, p_PropertyType, p_PropertyValue, "EXIST")
        l_RowCount = CommonFunctionLibrary.Web_GetRowCount(driver, p_PropertyType, p_PropertyValue)
        l_ColumnCount = CommonFunctionLibrary.Web_GetColumnCount(driver, p_PropertyType, p_PropertyValue, 1)
        
        try:
            WebObject = eval("driver.find_element(By." + p_PropertyType + "," + chr(34) + p_PropertyValue + chr(34) + ")")
            for ix in range(1,l_RowCount):
                for iy in range(0,l_ColumnCount):
                    l_CellText = WebObject.find_elements(By.TAG_NAME,"tr")[ix].find_elements(By.TAG_NAME,"td")[iy].get_attribute('textContent')
                    if l_CellText == p_CellText:
                        l_TextExist = "Exist"
                        return ix
        except Exception as e:
            CommonFunctionLibrary.ReportEvent("Web_GetRowWithCellText : Unable to get the Row Number for the text " +  p_CellText + " for the Table of "+ p_PropertyType + ": " + p_PropertyValue, "FAIL", "YES")
            print(e)
        
        if l_TextExist == "NotExist":
            CommonFunctionLibrary.ReportEvent(p_CellText + "Does not exist in the webtable", "FAIL", "YES")
            print(p_CellText + "Does not exist in the webtable")
            
            
    #****************************************************************************************
    #Function Name : Web_GetColumnWithCellText
    #Description   : Function to get the column of particular cell in the webtable
    #Author        : Idris
    #Parameters    : Driver,Property Type,Property Value,CellText
    #****************************************************************************************
    @staticmethod
    def Web_GetColumnWithCellText(driver,p_PropertyType,p_PropertyValue,p_CellText):
        l_CellText = ""
        l_TextExist = "NotExist"
        CommonFunctionLibrary.Web_Wait(driver, p_PropertyType, p_PropertyValue, "EXIST")
        l_RowCount = CommonFunctionLibrary.Web_GetRowCount(driver, p_PropertyType, p_PropertyValue)
        l_ColumnCount = CommonFunctionLibrary.Web_GetColumnCount(driver, p_PropertyType, p_PropertyValue, 1)
        
        try:
            WebObject = eval("driver.find_element(By." + p_PropertyType + "," + chr(34) + p_PropertyValue + chr(34) + ")")
            for ix in range(1,l_RowCount):
                for iy in range(0,l_ColumnCount):
                    l_CellText = WebObject.find_elements(By.TAG_NAME,"tr")[ix].find_elements(By.TAG_NAME,"td")[iy].get_attribute('textContent')
                    if l_CellText == p_CellText:
                        l_TextExist = "Exist"
                        return iy
        except Exception as e:
            CommonFunctionLibrary.ReportEvent("Web_GetColumnWithCellText : Unable to get the Column Number for the text " +  p_CellText + " for the Table of "+ p_PropertyType + ": " + p_PropertyValue, "FAIL", "YES")
            print(e)
        
        if l_TextExist == "NotExist":
            CommonFunctionLibrary.ReportEvent(p_CellText + "Does not exist in the webtable", "FAIL", "YES")
            print(p_CellText + "Does not exist in the webtable")
            
            
    #****************************************************************************************
    #Function Name : Web_ClickCell
    #Description   : Function to click on a particular cell in the webtable
    #Author        : Idris
    #Parameters    : Driver,Property Type,Property Value,CellText
    #****************************************************************************************
    @staticmethod
    def Web_ClickCell(driver,p_PropertyType,p_PropertyValue,p_CellText):
        CommonFunctionLibrary.Web_Wait(driver, p_PropertyType, p_PropertyValue, "CLICK")
        l_RowNumber = CommonFunctionLibrary.Web_GetRowWithCellText(driver, p_PropertyType, p_PropertyValue, p_CellText)
        l_ColumnNumber = CommonFunctionLibrary.Web_GetColumnWithCellText(driver, p_PropertyType, p_PropertyValue, p_CellText)
        
        try:
            WebObject = eval("driver.find_element(By." + p_PropertyType + "," + chr(34) + p_PropertyValue + chr(34) + ")")
            WebObject.find_elements(By.TAG_NAME,"tr")[l_RowNumber].find_elements(By.TAG_NAME,"td")[l_ColumnNumber].click()
        except Exception as e:
            CommonFunctionLibrary.ReportEvent("Web_Set : Unable to click on the cell " +  p_CellText + " for the Table of "+ p_PropertyType + ": " + p_PropertyValue, "FAIL", "YES")
            print(e)
            
    #****************************************************************************************
    #Function Name : Web_SendKeys
    #Description   : Function to sendkeys on a particular webtable
    #Author        : Preethi
    #Parameters    : Driver,Property Type,Property Value,Input String,Iterations
    #****************************************************************************************   
    @staticmethod     
    def Web_SendKeys(driver,p_PropertyType,p_PropertyValue,p_InputString, p_Iterations):
        try:
            for i in range(int(p_Iterations)):
                eval("driver.find_element(By." + p_PropertyType + "," + chr(34) + p_PropertyValue + chr(34) + ")" + ".send_keys("+ p_InputString +")")
        except Exception as e:
                CommonFunctionLibrary.ReportEvent("Web_SendKeys : Send Keys failed for the element of "+ p_PropertyType + ": " + p_PropertyValue, "FAIL", "YES")
                print(e)
    

    @staticmethod
    def ErrorMessage():
        sText=""
        sMessage =traceback.format_exc().splitlines()
        for sText in reversed(sMessage):
            if sText!="":
                return "Testcase is Failed :"+sText                   
                break
            
    @staticmethod
    def Web_ClickListItem(driver,p_propertyType,p_propertyValue,p_childType,p_childValue,p_selectValue):
        CommonFunctionLibrary.Web_Wait(driver, p_propertyType, p_propertyValue, "EXIST")
        try:
            WebObject = eval("driver.find_element(By." + p_propertyType + "," + chr(34) + p_propertyValue + chr(34) + ")")
            options = eval("WebObject.find_elements(By." + p_childType + "," + chr(34) + p_childValue + chr(34) + ")")
            l_Clicked = False
            for option in options:                    
                if option.text.strip() == p_selectValue.strip():
                    option.click()
                    l_Clicked = True;
                    break    
             
            if  l_Clicked == True:
                CommonFunctionLibrary.ReportEvent("Selected :" + chr(34) + p_selectValue + chr(34) +  " from weblist having "+ p_propertyType + ": " + p_propertyValue, "PASS", "YES")
                return True
            else:
                CommonFunctionLibrary.ReportEvent("Failed to select the option '"+ chr(34) + p_selectValue + chr(34) + "' " + "From the list having" + p_propertyType + ": " + p_propertyValue, "FAIL", "YES")
                return False
        except Exception as e:
            CommonFunctionLibrary.ReportEvent("Web_Select : Unable to Select value for the element of "+ p_propertyType + ": " + p_propertyValue, "FAIL", "YES")
            return False
            print(e)
            
    @staticmethod
    def Web_MoveToElement(driver,p_propertyType,p_propertyValue):
        wait = WebDriverWait(driver,60)
        action_chains = ActionChains(driver)
        eval("action_chains.move_to_element(" + "driver.find_element(By."+ p_propertyType + "," + chr(34) + p_propertyValue + chr(34)+ ")).perform()")
        
    @staticmethod 
    def Web_WaitTillPresence(driver,p_propertyType,p_propertyValue,TimeToWait):
        driverwait = WebDriverWait(driver,1)
        for ix in range(TimeToWait):
            try:
                eval("driverwait.until(EC.element_to_be_clickable((By." + p_propertyType + "," + chr(34) + p_propertyValue + chr(34) + ")))")
                return True
            except Exception as e:
                time.sleep(1)
                if ix == TimeToWait:
                    print(e)
                    return False
                
    @staticmethod            
    def Web_ExplicitWait(TimeToWait):
        time.sleep(TimeToWait)
     
        
    #****************************************************************************************
    #Function Name : Web_Clear
    #Description   : Function to Clear a value in any Web Edit
    #Author        : Lokesh
    #Parameters    : Driver,Property Type and Property Value and text value
    #****************************************************************************************
    @staticmethod
    def Web_Clear(driver,p_propertyType,p_propertyValue):
        CommonFunctionLibrary.Web_Wait(driver, p_propertyType, p_propertyValue, "CLICK")
        try:
            eval("driver.find_element(By." + p_propertyType + "," + chr(34) + p_propertyValue + chr(34) + ").clear()")
            return True
        except Exception as e:
            CommonFunctionLibrary.ReportEvent("Web_Set : Unable to Clear value for the element of "+ p_propertyType + ": " + p_propertyValue, "FAIL", "YES")
            print(e)
            return False

                    
            
          
        

