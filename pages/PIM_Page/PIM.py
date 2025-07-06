from selenium.webdriver.common.by import By
from utils.Utils import Utils

class PIM:
    def __init__(self, driver):
        self.driver = driver

    employee_list = (By.XPATH, "//a[text()='Employee List']")
    add_employee = (By.XPATH, "//a[text()='Add Employee']")
    reports = (By.XPATH, "//a[text()='Reports']")


    def click_on_employee_list(self):
        self.driver.find_element(*self.employee_list).click()

    def click_on_add_employee(self):
        self.driver.find_element(*self.add_employee).click()

    def click_on_reports(self):
        self.driver.find_element(*self.reports).click()
