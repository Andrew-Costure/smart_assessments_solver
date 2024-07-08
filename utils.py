from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxWebDriver
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from selenium.webdriver.support.ui import WebDriverWait


def login(driver: FirefoxWebDriver | ChromeWebDriver,
          username: str | None = None,
          password: str | None = None,
          cookies: list[dict[str, str]] = None) -> None:
    """
    Logs in to portal.alnafi.com

    - If cookies has been passed, username and password will be ignored, else username and password will be used to login to the portal.
    
    - This should successfully land the user on the dashboard of the portal.

    return None
    """
    page_login = "https://portal.alnafi.com/users/sign_in"
    page_404 = "https://portal.alnafi.com/404"
    page_dashboard = "https://portal.alnafi.com/enrollments"

    if cookies: # cookies will be preferred
        driver.get(page_404) # cookies load best on a 404 page
        for cookie in cookies:
            cookie = cleanup_cookie(cookie)
            driver.add_cookie(cookie)
        driver.get(page_dashboard)

    elif username and password:
        print("Using Username and Password. Manual Intervention might be required!")
        driver.get(page_login)
        username_field = driver.find_element(By.NAME, "user[email]")
        password_field = driver.find_element(By.NAME, "user[password]")
        username_field.send_keys(username)
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)
        WebDriverWait(driver, 20).until(EC.url_to_be(page_dashboard))

def cleanup_cookie(cookie: dict[str, str]):
    if (
        cookie["sameSite"] == "unspecified"
        or cookie["sameSite"] == "no_restriction"
    ):
        cookie["sameSite"] = "None"
    elif cookie["sameSite"] == "lax":
        cookie["sameSite"] = "Lax"
    elif cookie["sameSite"] == "strict":
        cookie["sameSite"] = "Strict"
    return cookie