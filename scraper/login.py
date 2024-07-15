import os

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .utils import cleanup_cookie
from .utils import logger_setup
from .types import WebDriver

logger = logger_setup(__name__)

def login(driver: WebDriver,
          landing_url: str,
          username: str | None = None,
          password: str | None = None,
          cookies: list[dict[str, str]] = None,
          ) -> None:
    """
    Logs in to portal

    - If cookies has been passed, username and password will be ignored, else username and password will be used to login to the portal.
    
    - This should successfully land the user on the dashboard of the portal.

    return None
    """
    page_login = "https://{PORTAL_URL}/users/sign_in".format(
        PORTAL_URL=os.environ["PORTAL_URL"]
    )
    page_404 = "https://{PORTAL_URL}/404".format(PORTAL_URL=os.environ["PORTAL_URL"])

    if cookies: # cookies will be preferred
        driver.get(page_404) # cookies load best on a 404 page
        for cookie in cookies:
            cookie = cleanup_cookie(cookie)
            driver.add_cookie(cookie)
        driver.get(landing_url)

    elif username and password:
        logger.info("Using Username and Password. Manual Intervention might be required!")
        driver.get(page_login)
        username_field = driver.find_element(By.NAME, "user[email]")
        password_field = driver.find_element(By.NAME, "user[password]")
        username_field.send_keys(username)
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)

    else:
        raise ValueError("You must provide a username and password OR cookies to log into the portal")

    WebDriverWait(driver, 20).until(EC.url_to_be(landing_url))
