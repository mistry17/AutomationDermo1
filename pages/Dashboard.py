from utils.Utils import Utils
from selenium.webdriver.common.by import By

class Dashboard:

    def __init__(self, driver):
        #super().__init__()
        self.driver = driver

    search = (By.XPATH, "//input[@placeholder = 'Search']")
    admin = (By.XPATH, "//ul[@class= 'oxd-main-menu']/li[1]")
    pim = (By.XPATH, "//ul[@class= 'oxd-main-menu']/li[2]")
    leave = (By.XPATH, "//ul[@class= 'oxd-main-menu']/li[3]")
    time = (By.XPATH, "//ul[@class= 'oxd-main-menu']/li[4]")
    recruitment = (By.XPATH, "//ul[@class= 'oxd-main-menu']/li[5]")
    my_info = (By.XPATH, "//ul[@class= 'oxd-main-menu']/li[6]")
    performance = (By.XPATH, "//ul[@class= 'oxd-main-menu']/li[7]")
    dashboard = (By.XPATH, "//ul[@class= 'oxd-main-menu']/li[8]")
    directory = (By.XPATH, "//ul[@class= 'oxd-main-menu']/li[9]")
    maintenance = (By.XPATH, "//ul[@class= 'oxd-main-menu']/li[10]")
    claim = (By.XPATH, "//ul[@class= 'oxd-main-menu']/li[11]")
    buzz = (By.XPATH, "//ul[@class= 'oxd-main-menu']/li[12]")
    profile_dropdown = (By.CSS_SELECTOR, ".oxd-userdropdown-tab")
    log_out = (By.LINK_TEXT, "Logout")

    def click_on_pim(self):
        self.driver.find_element(*self.pim).click()

    def click_on_profile_dropdown(self):
        self.driver.find_element(*self.profile_dropdown).click()

    def click_on_logout(self):
        self.driver.find_element(*self.log_out).click()