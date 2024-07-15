from typing import Generator

from selenium.webdriver.common.by import By

from .utils import logger_setup
from .types import WebDriver, WebElement

# ============ LOCATORS ===================
LOADER = ()
COURSES = ()
LESSONS = ()
LESSON_TYPE = ()


# ============ SETUP ---------------------
logger = logger_setup(__name__)

# ============ FUNCTIONS ===================
def get_lessons(driver: WebDriver, _type: str = "quiz") -> Generator[WebElement, None, None]:
    for course in driver.find_elements(*COURSES):
        course.click()
        all_lessons = course.find_elements(*LESSONS)
        for lesson in all_lessons:
            lesson_type = lesson.find_element(*LESSON_TYPE).text.splitlines()[0].strip()
            if lesson_type.lower() == _type.lower():
                print(lesson_type)
                yield lesson
