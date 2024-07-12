from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from .types import WebDriver

# ============ LOCATORS ===================
LOADER = (By.ID, "loader-1")
COURSES = (
    By.XPATH,
    "/html/body/div[1]/div[2]/div[2]/div/div[1]/div/nav/div/div[4]/div",
)
LESSONS = (By.XPATH, "div[2]/ul/li")
LESSON_TYPE = (By.XPATH, "a/div[2]/div")

# ============ FUNCTIONS ===================
def get_lessons(driver: WebDriver, _type: str = "assessments") -> list[WebElement]:
    lessons = []
    for course in driver.find_elements(*COURSES):
        all_lessons = course.find_elements(*LESSONS)
        for lesson in all_lessons:
            # remove extra characters like diamonds etc.
            lesson_type = lesson.find_element(*LESSON_TYPE).text.splitlines()[0].strip()
            if  lesson_type.lower() == _type.lower():
                lessons.append(lesson)
    return lessons
