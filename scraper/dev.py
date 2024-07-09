import os
from pathlib import Path
import json

from dotenv import load_dotenv
from selenium import webdriver

from scraper.login import login

def init(browser="chrome"):
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

    login(driver, USERNAME, PASSWORD, cookies)
    return driver
