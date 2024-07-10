from scraper.dev import init
from scraper import navigation
from scraper.utils import logger_setup

logger = logger_setup(__name__)

if __name__ == "__main__":
    driver = init(browser='firefox') # or 'chrome'

    navigation.open_assessment(
        driver,
        "Assessments for Internship and Resume (Diploma in Cloud Cyber Security)",
    )
    driver.quit()
