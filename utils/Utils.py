import inspect
import logging
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Utils:
    def __init__(self,driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def custom_logger(loggers = logging.DEBUG):
        calls_func = inspect.stack()[1][3]
        logger = logging.getLogger(calls_func)
        logger.setLevel(loggers)
        format_date_and_time = logging.Formatter('%(asctime)s - %(levelname)s : %(message)s', datefmt= '%d/%m/%Y %I:%M:%S %p')
        #sh = logging.StreamHandler()
        fh = logging.FileHandler("cases.logs")
        #sh.setFormatter(format_date_and_time)
        fh.setFormatter(format_date_and_time)
        logger.addHandler(fh)
        return logger

    def custom_implicit_wait(self, locator, timeout=200):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_element_to_be_clickable(self, locator, timeout=200):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def generate_emp_id(self):
        emp_id = random.randint(1000,9999)
        return emp_id
