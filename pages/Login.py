from selenium.webdriver.common.by import By
from utils.Utils import Utils

class LoginPage(Utils):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    username = (By.NAME, "username")
    password = (By.NAME, "password")
    login_button = (By.XPATH, "//button[@type='submit']")

    def enter_username(self, username):
        self.custom_implicit_wait(self.username).send_keys(username)
        #self.driver.find_element(*self.username).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)

    def click_on_login_button(self):
        self.driver.find_element(*self.login_button).click()