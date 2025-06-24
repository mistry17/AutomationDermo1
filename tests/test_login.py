import time

import pytest

from conftest import driver_initialize
from pages.Login import LoginPage
from utils.Utils import Utils

class TestLoginCases:
    logs = Utils.custom_logger()

    @pytest.mark.parametrize('username,password',
                             [('admin', 'admin123')
                              ])
    def test_login_with_username_password(self, driver_initialize, username, password):
        driver = driver_initialize
        login_page = LoginPage(driver)
        self.logs.info("Enter username")
        login_page.enter_username(username)
        self.logs.info("Enter password")
        login_page.enter_password(password)
        self.logs.info("Click on login button")
        login_page.click_on_login_button()
        title_of_pge = login_page.get_title(driver)
        time.sleep(3)
        assert "OrangeHRM" == title_of_pge


