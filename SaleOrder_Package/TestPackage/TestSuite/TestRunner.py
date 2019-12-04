'#===================================================================================================='
' Module:        TestRunner.py'
' Description:   Run the test cases specified in the RunManager spreadsheet.'
' Author:        Idris'
' Date Created:  28/11/2018'
'----------------------------------------------------------------------------------------------------'
' Modifications:'
' Date        Modified By      Change Description'
' ----------  ---------------  ----------------------------------------------------------------------'
'13/03/2019    Steffi'
'===================================================================================================='
'#IMPORTS'
import os
import sys
# from xl2dict.xlextractor import XlToDict 
objRootDir = os.path.dirname(os.path.dirname(__file__))
print(objRootDir)


import pytest
import subprocess
import datetime

  
environment="REG"#argvenv
strRootDirectory = objRootDir
print("root directory: "+strRootDirectory)
# libpackmodule = strRootDirectory + "/PyTestPkg"
# print(libpackmodule)
driverpath = strRootDirectory + "\Drivers\\"
# print(driverpath)
print("driverpath: "+driverpath)
RunManagerPath = strRootDirectory + "\Resources\RunManager.xlsx"
print("RunManagerPath: "+RunManagerPath)
Runpath=strRootDirectory + "\TestSuite\Run.cmd"
print("Runpath: "+Runpath)  

  
  
'#VARIABLES'
# SuiteName = "CreateBroadcast.robot"
strTestCases = ""
strSheetName = "Run_Manager"
RecordCount = ""

# def GetValueResponse(key,dictionary):
#     for k, v in dictionary.items():
#         if k == key:
#             yield v
#         elif isinstance(v, dict):
#             for result in GetValueResponse(key, v):
#                 yield result
#         elif isinstance(v, list):
#             for d in v:
#                 for result in GetValueResponse(key, d):
#                     yield result  
# '#Select the test cases to be executed'
# try:
#     myxlobject = XlToDict()
#     dictionary = myxlobject.fetch_data_by_column_by_sheet_name(file_path=RunManagerPath,sheet_name="Run_Manager",filter_variables_dict={"Execute" : "YES"})
#     testcases = ""
#     if (len(dictionary) > 0):
#         for x in range(len(dictionary)):
#             testcase = list(GetValueResponse("TestCase", dictionary[x]))
#             testcase = str(testcase).replace("]","").replace("[","").replace("'","")
#             testcases = testcases +str(testcase)+".py" + " "
#     strTestCases = testcases
# except Exception as e:
#     print("Exception Raised :"+ e)
  
'#CREATE A FOLDER TO STORE RESULTS'
strTimeStamp = '{:%Y%m%d_%H%M%S}'.format(datetime.datetime.now())
folderName = strRootDirectory + "\Results\\" + strTimeStamp
print(folderName)

marker="smoke"
threadcount="2"
count="3"
strTestCases="test_SalesOrderMultiLine.py"

# os.mkdir(folderName)
'#Create a command file to trigger execution'
objFile = open("Run.cmd","w+")
objFile.write("@cd " + strRootDirectory + "/Scripts" + "\n")
# objFile.write("pytest "+strTestCases+" -v -n "+threadcount+" --count="+count)
# objFile.write("pytest "+strTestCases+" --workers 2 --tests-per-worker "+count)
objFile.write("pytest -v "+strTestCases+" --dist=each --tx "+count+"*popen")

objFile.close()
  
'#Run the command file'
print('TO RUN CMD FILE') 
completed=subprocess.Popen(Runpath)

htmlfilepath=folderName+"////"        
print(htmlfilepath)          
# from GenericPackage.SummaryReport import SummaryReport
# SummaryReport.SummaryReport("Dip Summary report",htmlfilepath)
