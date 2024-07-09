import os
from pathlib import Path
import json

from dotenv import load_dotenv
from selenium import webdriver

from .login import login


def init(browser="chrome", landing_url: str = "https://portal.alnafi.com/enrollments"):
    load_dotenv()

    if browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "chrome":
        driver = webdriver.Chrome()
    else:
        raise NotImplementedError("It supports firefox and chrome only")

    COOKIE_FILE = Path(os.getenv("COOKIE_FILE")).absolute()
    USERNAME=os.getenv("USERNAME")
    PASSWORD=os.getenv("PASSWORD")

    print(COOKIE_FILE, USERNAME, PASSWORD)
    cookies = None
    if COOKIE_FILE:
        with open(COOKIE_FILE, 'r', encoding='utf-8') as cookie_file:
            cookies = json.load(cookie_file)

    login(driver, landing_url, USERNAME, PASSWORD, cookies)
    return driver
