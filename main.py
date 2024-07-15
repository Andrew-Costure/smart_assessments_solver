from selenium.webdriver.support.ui import WebDriverWait
from dotenv import load_dotenv

from scraper.dev import init
from scraper.assessment import solve
from scraper.utils import logger_setup

logger = logger_setup(__name__)

load_dotenv()

if __name__ == "__main__":
    # this is just to show how it can work
    url = "assessment_url_here"
    driver = init(browser='firefox', landing_url=url) # or 'chrome'
    for quiz, answer in solve(driver, wait=WebDriverWait(driver, 20), solver_id="ollama", model="llama3"):
        print(f"Quiz: {quiz}\nAnswer: {answer}") # or you can save the quiz and answer to local files
        # all things will be done behind the scenes


    # ================
    # from scraper import navigation, course
    # from scraper.utils import encoded_url
    
    # if you don't want to open the url or complete it in batch using names etc
    # assessments_name = ["assessment_name", "another_name"]
    # for assessment_name in assessments_name:
    #    navigation.open_assessment(
    #        driver,
    #        assessments_name,
    #    )
    #    assessments = course.get_lessons(driver, "quiz")
    #    for assessment in assessments:
    #       print(assessment.text)
    #    pass
