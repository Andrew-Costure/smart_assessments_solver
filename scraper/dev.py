import os
from pathlib import Path
import json

from selenium import webdriver

from .login import login


def init(browser="chrome", landing_url: str = "https://{PORTAL_URL}/enrollments"):

    if browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "chrome":
        driver = webdriver.Chrome()
    else:
        raise NotImplementedError("It supports firefox and chrome only")

    driver.implicitly_wait(5)  # should be no more than 10 seconds

    COOKIE_FILE = Path(os.getenv("COOKIE_FILE")).absolute()
    USERNAME=os.getenv("USERNAME")
    PASSWORD=os.getenv("PASSWORD")

    cookies = None
    if COOKIE_FILE:
        with open(COOKIE_FILE, 'r', encoding='utf-8') as cookie_file:
            cookies = json.load(cookie_file)

    login(
        driver,
        landing_url.format(PORTAL_URL=os.environ["PORTAL_URL"]),
        USERNAME,
        PASSWORD,
        cookies,
    )
    return driver
