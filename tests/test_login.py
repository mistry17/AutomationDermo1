import time
import json
import pytest
from conftest import driver_initialize
from pages.Login import LoginPage
from utils.Utils import Utils

file_path = "../test_data/Login_data.json"
with open(file_path) as file_path:
    json_data = json.load(file_path)
    list_of_data = json_data["login_data"]


class TestLoginCases:
    logs = Utils.custom_logger()


    @pytest.mark.parametrize("test_datas", list_of_data)
    def test_login_with_username_password(self, driver_initialize,test_datas):
        driver = driver_initialize
        login_page = LoginPage(driver)
        self.logs.info("Enter username")
        login_page.enter_username(test_datas["username"])
        self.logs.info("Enter password")
        login_page.enter_password(test_datas["password"])
        self.logs.info("Click on login button")
        login_page.click_on_login_button()
        title_of_pge = login_page.get_title()
        time.sleep(3)
        assert "OrangeHRM" == title_of_pge
        self.logs.info("Login Successful")


