import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from utils.Utils import Utils


class Employee_List(Utils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    sv_btn = (By.XPATH, "(//button[@type='submit'][normalize-space()='Save'])[1]")
    employee_name = (By.XPATH, "(//input[@placeholder='Type for hints...'])[1]")
    search_btn = (By.XPATH, "//button[normalize-space()='Search']")
    employee_in_list = (By.XPATH, "(//div[@role='cell'])[3]")
    delete_icon = (By.XPATH, "(//*[@class='oxd-table-cell-actions'])[1]")
    yes_delete_button = (By.XPATH, "//button[normalize-space()='Yes, Delete']")
    save_confirmation = (By.ID, "oxd-toaster_1")
    first_name = (By.NAME, "firstName")

    def click_on_save_btn(self):
        time.sleep(3)
        self.wait_for_element_to_be_clickable(self.sv_btn).click()

    def enter_first_name(self, emp_name):
        self.custom_implicit_wait(self.employee_name).send_keys(emp_name)

    def click_on_search_btn(self):
        self.driver.find_element(*self.search_btn).click()

    def get_employee_name(self):
        name = self.driver.find_element(*self.employee_in_list).text
        return name

    def click_on_delete_icon(self):
        self.driver.find_element(*self.delete_icon).click()

    def click_on_delete_yes_btn(self):
        self.driver.find_element(*self.yes_delete_button).click()

    def wait_for_confirmation(self):
        self.custom_implicit_wait(self.save_confirmation)

    def wait_for_first_name(self):
        self.custom_implicit_wait(self.first_name)

