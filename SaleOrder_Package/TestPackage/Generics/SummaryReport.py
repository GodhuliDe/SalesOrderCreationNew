import os
import socket
import re
import webbrowser
from datetime import datetime,date
from _datetime import time
from TestPackage.Generics.CommonFunctions import CommonFunctionLibrary

class SummaryReport():
    
    strResultSummaryHeader =""
    sFailCount=""
    sPassCount=""
    TestCaseDesc=""
    sEnv=""
    sProjectName=""  
    sPattern=""
    sStartTime=""
    sEndTime=""
    duration=""
    
    
    '''**********************************************************************************************************************************************************************
    Function Name      : totalExecutionTime
    Input Parameters   : TimeToAdd - Pass all the step time details which needs to be added
    Output Parameters  : TotalExecutionTime -  Returns Total Execution Time
    Description        : It will sum up all the step time to total execution time
    Version            : 1.0
    Author             : Mohan Parasuraam
    *************************************************************************************************************************************************************************'''
    def totalExecutionTime(self,TimeToAdd):
        from datetime import datetime
        from datetime import timedelta
        
        self.totalTime = TimeToAdd.split(",")
        TotalExecutionTime=timedelta(hours=0,minutes=0,seconds=0)
        for i in range(len(self.totalTime)):
            (h,m,s)= self.totalTime[i].split(':')
            T1= timedelta(hours=int(h),minutes=int(m),seconds=int(s))
            TotalExecutionTime=TotalExecutionTime+T1
        return TotalExecutionTime
    
    '''**********************************************************************************************************************************************************************
    Function Name      : SummaryReport
    Input Parameters   : ProjectName - Name of the project
    Output Parameters  : N.A
    Description        : It will generate the summary report
    Version            : 1.0
    Author             : Mohan parasuraam
    *************************************************************************************************************************************************************************'''
    @staticmethod
    def SummaryReport(ProjectName):
        SummaryReport.sFailCount= 0
        SummaryReport.sPassCount = 0
        SummaryReport.individualExecutionTime="0:0:0"
        SummaryReport.TestCaseDesc=""
        SummaryReport.sEnv = "QA"
        SummaryReport.sProjectName = ProjectName  
        SummaryReport.Totaltime = "0:0:0"   
        sCheck = True 
        time=""  
        HTMLReportPath=CommonFunctionLibrary.ReporterResultPath
        strHRMLReport = HTMLReportPath.replace('\\','/')
        HTMLResultPath = strHRMLReport.replace("//","/")
        
        strResultSummaryHeader = """<meta http-equiv=X-UA-Compatible content=IE=edge><table id='Logos'> <colgroup> <col style='width: 25%' /> <col style='width: 25%' /> <col style='width: 25%' /> <col style='width: 25%' />
        </colgroup> <thead>  <tr class='content'> <th class = 'Logos' colspan='2' > <img align ='center' src='https://lda.lowes.com/is/image/Lowes/NSI_Lowes_logo_no_tagline?$JPEG-HQ$&wid=147'></img> 
        </th> </tr> </thead> </table> <html> <head> <script src='http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js' 
        type='text/javascript'></script></script><script src='http://code.highcharts.com/highcharts.js'></script><script src='http://code.highcharts.com/highcharts-3d.js'></script>
        <script src='http://code.highcharts.com/modules/exporting.js'></script><meta charset='UTF-8'> <title>Lowe's - Automation Execution Results Summary</title>
        <style type='text/css'>body {background-color: #FFFFFF; font-family: Verdana, Geneva, sans-serif; text-align: center; } small { font-size: 0.7em; } 
        table { box-shadow: 9px 9px 10px 4px #BDBDBD;border: 0px solid #4D7C7B;border-collapse: collapse; border-spacing: 0px; width: 1000px; margin-left: auto; margin-right: auto; } 
        tr.heading { background-color: #041944;color: #FFFFFF; font-size: 0.7em; font-weight: bold;} tr.subheading { background-color: #6A90B6;color: #000000; font-weight: bold; font-size: 0.7em; text-align:justify; }
        tr.section { background-color: #A4A4A4; color: #333300; cursor: pointer; font-weight: bold;font-size: 0.8em; text-align: justify;background:-o-linear-gradient(bottom, #56aaff 5%, #e5e5e5 100%);
        background:-webkit-gradient( linear, left top, left bottom,color-stop(0.05, #56aaff), color-stop(1, #e5e5e5) );background:-moz-linear-gradient( center top, #56aaff 5%, #e5e5e5 100% );filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#56aaff, endColorstr=#e5e5e5);background:-o-linear-gradient(top,#56aaff,e5e5e5);} tr.subsection { cursor: pointer; } 
        tr.content { background-color: #FFFFFF; color:#000000; font-size: 0.7em; display: table-row; } tr.content2 { background-color:#;E1E1E1border: 1px solid #4D7C7B;color: #000000; font-size: 0.7em; display: table-row; }
        td, th { padding: 5px; border: 1px solid #4D7C7B; text-align: inherit/; } th.Logos {padding: 5px; border: 0px solid #4D7C7B; text-align: inherit /;} 
        td.justified { text-align: Center;font-size: 110%; } td.pass {font-weight: bold; color: green;}td.fail { font-weight: bold; color: red; } 
        td.done, td.screenshot { font-weight: bold; color: black; } td.debug { font-weight: bold;color: blue; } td.warning { font-weight: bold; color: orange; } </style> </head> <body> 
        </br><table id='header'> <colgroup> <col style='width: 25%' /> <col style='width: 25%' /> <col style='width: 25%' /> 
        <col style='width: 25%' /> </colgroup> <thead> <tr class='heading'> <th colspan='4' style='font-family:Copperplate Gothic Bold;font-size:1.4em;'> """+SummaryReport.sProjectName+""" - Automation Execution Results Summary</th>
        </tr> <tr class='subheading'> <th>&nbsp;Date&nbsp;&&nbsp;Time&nbsp</th> <th>&nbsp;&nbsp;"""+datetime.now().strftime("%d/%m/%Y %H:%M:%S %p")+"""</th><th>&nbsp;Application</th> <th>&nbsp;&nbsp;"""+SummaryReport.sProjectName+"""</th> </tr>
        <tr class='subheading'> <th>&nbsp;Environment</th> <th>&nbsp;&nbsp;"""+SummaryReport.sEnv+"""</th> <th>&nbsp;Host Name</th><th>&nbsp;&nbsp;"""+socket.gethostname()+"""</tr></thead></table>
        <table id='main'> <colgroup> <col style='width: 10%' /> <col style='width: 40%' /> <col style='width: 20%' /> <col style='width:20%' />
        <col style='width:10%' /> </colgroup> <thead> <tr class='heading'> <th>Test Case ID</th> <th>Test Case Description</th> <th>Status</th> <th>Time</th></tr> </thead> <tbody>""" 
        print(HTMLResultPath)
        oF = open(HTMLResultPath+"Summary.html","w+")
        oF.write(strResultSummaryHeader)
        path=HTMLResultPath
        print(HTMLResultPath)
        dirs =  os.listdir(path)        
        for file in dirs:
            SummaryReport.TestCaseDesc=file.split(".")[0]
            if ".html"  in file: 
                if not "Summary" in file:
                    try:
                        sPattern = re.findall(r"[\d]+:[\d]+:[\d]+[a-z A-z]+",open(path+file).read())
                        sStartTime = sPattern[0].replace(" ","").replace("PM","").replace("AM","")
                        sEndTime = sPattern[len(sPattern)-1].replace(" ","").replace("PM","").replace("AM","")
                        time = datetime.strptime(sEndTime, "%H:%M:%S") - datetime.strptime(sStartTime, "%H:%M:%S")
                        if "red-cross.svg" in open(path+file).read():                    
                            sStatus= """<tr class='content2'><td class='justified'><font color='#153e7e' size='1' face='arial'><b>"""+SummaryReport.TestCaseDesc+"""</b>                                    
                                    </font></td><td class='justified'> <a href=../"""+HTMLResultPath[:-1].split('/')[-1]+"""/"""+file+""" target='about_blank'>"""+SummaryReport.TestCaseDesc+"""</a></td>
                                    <td class='justified'><img  src= https://openclipart.org/download/166859/red-cross.svg  width='30' height='30'/></td><td class='justified'>"""+str(time)+"""</td></tr></tbody>"""
                            SummaryReport.sFailCount = SummaryReport.sFailCount+1
                            oF.write(sStatus) 
                        else :
                            sStatus = """<tr class='content2'><td class='justified'><font color='#153e7e' size='1' face='arial'><b>"""+SummaryReport.TestCaseDesc+"""</b>
                             </font></td><td class='justified'> <a href=../"""+HTMLResultPath[:-1].split('/')[-1]+"""/"""+file+""" target='about_blank'>"""+SummaryReport.TestCaseDesc+"""</a></td>
                             <td class='justified'><img  src= https://openclipart.org/download/159733/green-tick.svg  width='30' height='30'/></td><td class='justified'>"""+str(time)+"""</td></tr></tbody>"""
                            SummaryReport.sPassCount = SummaryReport.sPassCount+1
                            oF.write(sStatus)                    
                        SummaryReport.individualExecutionTime= SummaryReport.individualExecutionTime+","+str(time)
                    except Exception:
                        print ("Test Case file(s) not generated.")
                        sCheck=False
                        break                    
        if sCheck:
            TotalExecTime = SummaryReport().totalExecutionTime(SummaryReport.individualExecutionTime)           
            Summarytrailer = """</table> <table id='footer'> <colgroup> <col style='width: 25%' /> <col style='width: 25%' /> <col style='width: 25%' /> <col style='width: 25%' /> </colgroup>
             <tfoot> <tr class='heading'>    <th colspan='4'>Total Duration (Including Report Creation) :"""+str(TotalExecTime)+"""</th> </tr> <tr class='content'>
            <td class='pass'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tests passed</td><td class='pass'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"""+str(SummaryReport.sPassCount)+"""</td> <td class='fail'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            Tests failed</td><td class='fail'>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; """+str(SummaryReport.sFailCount)+"""</td> </tr> </tfoot> </table>"""
            oF.write(Summarytrailer)
            os.startfile(path.replace("/","\\")+"Summary.html")
            print("Execution Completed")
        else:
            oF.close()
            os.remove(path+"Summary.html")
            print("Report Summary not generated.")