import os
import json

from dotenv import load_dotenv
from selenium import webdriver

from .scraper.login import login

def init(browser="chrome"):
    load_dotenv()
    
    if browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "chrome":
        driver = webdriver.Chrome()
    else:
        raise NotImplementedError("It supports firefox and chrome only")
    
    COOKIE_FILE = os.getenv("COOKIE_FILE")
    USERNAME=os.getenv("USERNAME")
    PASSWORD=os.getenv("PASSWORD")

    cookies = None
    if COOKIE_FILE:
        with open(COOKIE_FILE, 'r') as cookiefile:
            cookies = json.load(cookiefile)

    login(driver, USERNAME, PASSWORD, cookies)
    return driver
