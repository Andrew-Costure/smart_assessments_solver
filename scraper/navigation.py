from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxWebDriver
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait


from . import dashboard
from .utils import logger_setup, encoded_url

logger = logger_setup(__name__)


def open_assessment(
    driver: FirefoxWebDriver | ChromeWebDriver,
    name: str | None = None,
    url: str | None = None,
):
    if not url and name:
        search_assessment(driver, name)
        url = get_assessment_url(driver, name)
    elif not name:
        raise ValueError("Either name or url must be provided")

    driver.get(url)
    WebDriverWait(driver, 20).until(EC.url_to_be(url))

def search_assessment(driver: FirefoxWebDriver | ChromeWebDriver, name: str):
    driver.find_element(*dashboard.SEARCH).send_keys(name)
    driver.find_element(*dashboard.SEARCH).send_keys(Keys.RETURN)
    WebDriverWait(driver, 20).until(EC.url_to_be(encoded_url(name)))


def get_assessment_url(driver: FirefoxWebDriver | ChromeWebDriver, name: str):
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(dashboard.COURSE_CARDS)
    )

    course_cards = driver.find_elements(*dashboard.COURSE_CARDS)

    for title, url in get_cards_metadata(course_cards):
        if title == name:
            return url

    # TODO: Handle the case when the results are spanned across multiple pages
    # (i.e. the courses matching the name are more than 6)

    # If the title doesn't match then raise a ValueError
    logger.error("Assessment Not Found! Exiting...")

def get_cards_metadata(course_cards: list[WebElement]):
    cards_data = []
    for card in course_cards:
        title = card.find_element(*dashboard.COURSE_TITLE).text
        url = card.find_element(*dashboard.COURSE_LINK).get_attribute("href")
        cards_data.append((title, url))
    return cards_data
