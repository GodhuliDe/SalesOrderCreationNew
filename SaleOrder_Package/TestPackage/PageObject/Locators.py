

class Locator(object):
    
#LoginPage Locators
    UserName="i0116"
    nextButton = "idSIButton9"
    PasswordBox="//input[@name='passwd']"
    yesButton = "//input[@value='Yes']"
    signInButton="login-jsp-btn"
    
#dashboard

    validateLogo = "NavBarD365_label"
    navigationPane = "//div[@class='modulesPane-opener']"
    modulesLink = "//div[@title='Modules']"
    moduleminimizedlink = "//div[@class='modulesPane-groupHeading  CaretRight-symbol'][@title='Modules']"
    salesAndMarketingLink = "//a[contains(text(),'Sales and marketing')]"
    allSalesOrdersLink = "//a[text()='All sales orders']"
    
    pleaseWaitstr = "//div[@id='ShellProcessingDiv']"
    
#AllSalesOrderPage
    newButton = "//span[contains(@id,'SystemDefinedNewButton_label')]"
    custAccountTab = "//input[contains(@id,'SalesTable_CustAccount_input')]"
    custAccountRecord = "//input[contains(@id,'DirPartyTable_Name_input')]"
    yes_Button = "//button[contains(@id,'Yes')]"
    generalTab = "//header[contains(@id,'General_header')]"
    salesOrderNum = "SalesTable_SalesId"
    itemnumberTextB = "//input[@name='SalesLine_ItemId']"
    itemQtyTextbox = "//input[@name='SalesLine_SalesQty']"
    lineDetailsHeader = "//header[contains(@id,'LineViewLineDetails_header')]"
    setupTab = "//span[text()='Setup']"
    itemSalesTextBox = "//input[@name='LineSalesTax_TaxItemGroup']"
    SalesTaxGroupBox = "LineSalesTax_TaxGroup"
    storageSiteBox = "InventoryDimensions_InventSiteId"
    storageWarehouseBox = "InventoryDimensions_InventLocationId"
    deliveryTab = "//span[text()='Delivery']"
    productTab = "//span[text()='Product']"
    modeOfDelivery = "//input[@name='SalesLineDeliveryGroup_DlvMode']"
    saveButton = "//span[text()='Save']"
    completeHeader = "//span[contains(text(),'Complete')]"
    paymentBlade = "[id*='_SalesOrderSummaryPayments_header']"
    addButton = "AddBtn"
    paymentMethodDropdown = "//input[@name='Identification_TenderTypeId']/following-sibling::div"
    paymentMethodFilter = "//div[@data-dyn-columnname='Lookup_RetailTenderTypeName']//div[text()='Payment method name']"
    paymentFilterTextbox = "FilterField_Lookup_RetailTenderTypeName_RetailTenderTypeName_Input_0"
    paymentMethodRecord = "Lookup_RetailTenderTypeName"
    
    careNumberDrpDwn = "//input[@name='CreditCard_M_editCreditCard']/following-sibling::div"
    cardHolderFilter = "[id*='_CustCreditCard_Name_0'][aria-label='Card holder']"
    
    cardHolderNameFilterTxtBx = "[name*='FilterField_CustCreditCard_Name_Name_Input_']"
    creditCardname = "CustCreditCard_Name"
    submitBtn = "SubmitButton"
    okpaymentBtn = "//button[@name='OKButton']"
    
    addSOlineBtn = "//span[contains(@id,'LineStripNew_label')]"