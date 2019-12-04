
#*************************************************************************************************************************
#Credentails
SheetName ="Run_Manager"
#*********************************************************************************************************************
import os
RootDir = os.path.dirname(os.path.dirname(__file__))
RootDirectory = RootDir.replace('\\','\\\\')
RunManagerPath=RootDirectory+"\\\\Resources\\\\RunManager.xls"
TestDataPath=RootDirectory+"\\\\Resources\\\\TestData.xls"
ResultFolderPath=RootDirectory+"\\\\TestPackage\\\\Results"
TextFilePath = RootDirectory+"\\\\Resources\\\\MajorIncident.txt"
#************************************************************************************************************************


