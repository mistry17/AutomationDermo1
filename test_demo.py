import time

import pytest

def tests_case(driver_initialize):
    driver = driver_initialize
    time.sleep(3)
    driver.get("https://www.google.com")