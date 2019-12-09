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
    CSS_Day = ".react-datepicker__week:nth-child(1) > .react-datepicker__day--sat"
# -------------------------------
    ID_Date_Incidence = "start_date_incidence"
    CSS_Navigation_Horizontal = ".DayPickerNavigation_leftButton__horizontal > .DayPickerNavigation_svg__horizontal"
    CSS_Day_From = ".CalendarMonthGrid_month__horizontal:nth-child(2) tr:nth-child(5) > .CalendarDay:nth-child(5)"
    CSS_Day_To = ".CalendarMonthGrid_month__horizontal:nth-child(3) tr:nth-child(2) > .CalendarDay:nth-child(4)"
    XPath_Acept_New_Manual_Nomina = "/html/body/div[5]/div/div/div/div[2]/form/div[3]/button[2]"





