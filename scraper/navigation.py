import sys

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from . import dashboard, course
from .utils import logger_setup, encoded_url
from .types import WebDriver, WebElement


logger = logger_setup(__name__)

def open_assessment(
    driver: WebDriver,
    name: str | None = None,
    url: str | None = None,
):
    # 20 seconds is enough to wait for something to load or hide
    wait = WebDriverWait(driver, 20)

    if not url and name:
        search_assessment(driver, name, wait)
        url = get_assessment_url(driver, name, wait)
    elif not name:
        raise ValueError("Either name or url must be provided")
    
    if url:
        driver.get(url)
        wait.until(EC.url_to_be(url))
        wait.until(EC.invisibility_of_element(course.LOADER))
    else:
        logger.error("Could not find assessment with name: %s", name)
        sys.exit(1)

def search_assessment(driver: WebDriver, name: str, wait: WebDriverWait):
    if not driver.current_url == encoded_url(name):
        driver.get(encoded_url(name))
        wait.until(EC.url_to_be(encoded_url(name)))


def get_assessment_url(driver: WebDriver, name: str, wait: WebDriverWait):
    wait.until(EC.presence_of_element_located(dashboard.COURSE_CARDS))

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
