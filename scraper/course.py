from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

# ============ LOCATORS ===================
LOADER = (By.ID, "loader-1")
COURSES = (
    By.XPATH,
    "/html/body/div[1]/div[2]/div[2]/div/div[1]/div/nav/div/div[4]/div",
)
LESSONS = (By.XPATH, "div[2]/ul/li")
LESSON_TYPE = (By.XPATH, "a/div[2]/div")
                # .text.splitlines()[0]
                # .strip()
                # .lower()

# ============ FUNCTIONS ===================
def get_lessons(driver, _type: str = "assessments") -> list[WebElement]:
    lessons = []
    for course in driver.find_elements(*COURSES):
        all_lessons = course.find_elements(*LESSONS)
        for lesson in all_lessons:
            if lesson.find_element(*LESSON_TYPE).text == _type:
                lessons.append(lesson)
    return lessons
