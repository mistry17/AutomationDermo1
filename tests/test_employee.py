import time

from pages.Dashboard import Dashboard
from pages.PIM_Page.Add_Employee.Add_Employee import Add_Employee
from pages.PIM_Page.Employee_List.Employee_List import Employee_List
from utils.Utils import Utils
from pages.PIM_Page.PIM import PIM
from tests.test_login import TestLoginCases
import json
import pytest

file_path = "../test_data/Login_data.json"
with open(file_path) as data_file:
    json_data = json.load(data_file)
    lists_data_login = json_data["login_data"]
    list_data_employee = json_data["employee_data"]
    combined_data = list(zip(lists_data_login, list_data_employee))

class Test_Employees:
    logs = Utils.custom_logger()

    @pytest.mark.parametrize("login_data, employee_data", combined_data)
    def test_add_verify_employee(self, driver_initialize, login_data, employee_data):
        driver = driver_initialize
        login = TestLoginCases()
        login.test_login_with_username_password(driver, login_data)
        dashboard = Dashboard(driver)
        self.logs.info("Click on PIM")
        dashboard.click_on_pim()
        pim = PIM(driver)
        self.logs.info("Click on add employee button on PIM page")
        pim.click_on_add_employee()
        add_employee = Add_Employee(driver)
        self.logs.info("Add first name of employee")
        add_employee.enter_first_name(employee_data["first_name"])
        self.logs.info("Add middle name of employee")
        add_employee.enter_middle_name(employee_data["middle_name"])
        self.logs.info("Add last name of employee")
        add_employee.enter_last_name(employee_data["last_name"])
        emp_id = add_employee.enter_emp_id()
        self.logs.info(emp_id)
        self.logs.info("Click on save button")
        add_employee.click_on_save()
        assert "OrangeHRM" == driver.title
        emp_list = Employee_List(driver)
        emp_list.wait_for_confirmation()
        emp_list.wait_for_first_name()
        emp_list.click_on_save_btn()
        dashboard.click_on_profile_dropdown()
        dashboard.click_on_logout()

    @pytest.mark.parametrize("login_data , employee_data", combined_data)
    def test_delete_emp(self, driver_initialize, employee_data, login_data):
        driver = driver_initialize
        login_page = TestLoginCases()
        login_page.test_login_with_username_password(driver, login_data)
        dashboard = Dashboard(driver)
        dashboard.click_on_pim()
        pim = PIM(driver)
        pim.click_on_employee_list()
        emp_list = Employee_List(driver)
        full_name = employee_data["first_name"] + " " + employee_data["middle_name"]
        emp_list.enter_first_name(full_name)
        emp_list.click_on_search_btn()
        emp_name = emp_list.get_employee_name()
        self.logs.info(f"Full name is {full_name} equal to {emp_name}")
        time.sleep(5)
        assert emp_name.__eq__(full_name)
        emp_list.click_on_delete_icon()
        emp_list.click_on_delete_yes_btn()
        self.logs.info(f"Deleted the {emp_name} record")
        dashboard.click_on_profile_dropdown()
        dashboard.click_on_logout()
