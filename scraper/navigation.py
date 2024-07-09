from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxWebDriver
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver

SEARCH_SELECTOR = (By.NAME, 'q')

def search_assessment(driver: FirefoxWebDriver | ChromeWebDriver, name: str | None = None, url: str | None = None):
    if url:
        driver.get(url)
    elif name:
        driver.find_element(*SEARCH_SELECTOR).send_keys(name)
        driver.find_element(*SEARCH_SELECTOR).send_keys(Keys.RETURN)
    else:
        raise ValueError('Either `name` or `url` must be provided')

