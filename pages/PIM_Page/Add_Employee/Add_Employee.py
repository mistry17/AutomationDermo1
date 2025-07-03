from selenium.webdriver.common.by import By


class Add_Employee:
    def __init__(self, driver):
        self.driver = driver

    first_name = (By.CSS_SELECTOR, ".orangehrm-firstname")
    middle_name = (By.CSS_SELECTOR, ".orangehrm-middlename")
    last_name = (By.CSS_SELECTOR, ".orangehrm-lastname")
    cancel_btn = (By.XPATH, "//button[normalize-space()='Cancel']")
    save_btn = (By.XPATH, "//button[normalize-space()='Save']")

    def enter_first_name(self, name):
        self.driver.find_element(*self.first_name).send_keys(name)

    def enter_middle_name(self, middle_name):
        self.driver.find_element(*self.middle_name).send_keys(middle_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(*self.last_name).send_keys(last_name)

    def click_on_save(self):
        self.driver.find_element(*self.save_btn).click()

    def click_on_cancel(self):
        self.driver.find_element(*self.cancel_btn).click()