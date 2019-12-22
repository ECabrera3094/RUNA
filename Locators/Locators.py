class MyLocators():

    # Login Page
    ID_Username = "email"
    ID_Password = "password"
    XPath_Button = "//*[@id='root']/div/div/div/form/button"

    # Logout Page
    XPath_Active_User = "//*[@id ='root']/div/div/div/nav/div[2]/div[2]/div[2]/div[1]"
    CSS_Logout = ".header-dropdown-item:nth-child(5)"

    # Main Page
    XPath_Cancel_ChangePassword = "/html/body/div[4]/div/div/div/div[3]/form/div[2]/button[1]"
    XPath_Nominas = "//*[@id='root']/div/div/aside/ul/li[3]/a/span"
    Class_Close_Video = "video-close-icon"
    Text_Nominas_Activas = "Activas"


    # Nominas
    XPath_Button_Nueva_Nomina = "//*[@id='root']/div/div/div/div/section/nav[2]/button"
    CSS_Nomina_Group = ".react-select__placeholder"
    ID_Nomina_Group = "react-select-payroll_group_id-input"
# -------------------------------
    ID_Start_Date = "start_date"
    CSS_Navigation_Previous = ".react-datepicker__navigation--previous"
    CSS_Day = ".react-datepicker__week:nth-child(2) > .react-datepicker__day--sat"
# -------------------------------
    ID_Date_Incidence = "start_date_incidence"
    CSS_Navigation_Horizontal = ".DayPickerNavigation_leftButton__horizontal > .DayPickerNavigation_svg__horizontal"
    CSS_Day_From = ".CalendarMonthGrid_month__horizontal:nth-child(2) tr:nth-child(2) > .CalendarDay:nth-child(5)"
    CSS_Day_To = ".CalendarMonthGrid_month__horizontal:nth-child(2) tr:nth-child(3) > .CalendarDay:nth-child(4)"
    XPath_Acept_New_Manual_Nomina = "/html/body/div[5]/div/div/div/div[2]/form/div[3]/button[2]"
# -------------------------------
    XPath_Button_Comenzar = "//*[@id='root']/div/div/div/div/section/div[4]/div/div[2]/div[2]/button"
    CSS_Detail_Employee_1 = ".toggleable-row:nth-child(1) #Capa_1"
    XPath_Enter_New_Salary = "/html/body/div[@id='root']/div/div[@class='home-wrapper']/div[@class='home-right']/div[@class='home-container']/section[@class='base-container']/div[3]/div[@class='payroll-calculator ']/div[2]/div[@class='new-payroll']/div[@class='table-wrapper-container ']/table[@class='table-container toggleable-table payroll-table']/tbody/tr[@class='toggleable-row with-inset-border new-payroll-details new-payroll-row']/td[5]/div[1]/div[@class='inline-edit']/div[@class='vertical-align-container']/span[@class='inline-edit-value']"
    XPath_Button_Accept_Modify_Salary = "//*[@id='root']/div/div/div/div/section/div[3]/div/div[2]/div[1]/div[1]/table/tbody/tr[2]/td[7]/button"

    CSS_Detail_Employee_3 = ".toggleable-row:nth-child(3) #Capa_1"
    XPath_Delete_Employee = "/html/body/div[@id='root']/div/div[@class='home-wrapper']/div[@class='home-right']/div[@class='home-container']/section[@class='base-container']/div[3]/div[@class='payroll-calculator ']/div[2]/div[@class='new-payroll']/div[@class='table-wrapper-container ']/table[@class='table-container toggleable-table payroll-table']/tbody/tr[@class='toggleable-row with-inset-border new-payroll-details new-payroll-row']/td[@class='toggleable-row-detail-header']/button[@class='delete-icon-text-container']/span"

    CSS_Confirm_Delete = ".buttonsWrapper:nth-child(3) > .is-submit"

    XPath_Button_Continuar = "//*[@id='root']/div/div/div/div/section/div[3]/div/div[3]/button[2]"
    ID_Checkbox_Seleccionar_Todos = "selectMainCheckbox"

    XPath_Link_Calcular = "//*[@id='root']/div/div/div/div/section/div[2]/article[1]/h3/strong"
    XPath_Delete_Nomina = "//div[@id='root']/div/div/div/div/section/div[3]/div/div[2]/button/span"
