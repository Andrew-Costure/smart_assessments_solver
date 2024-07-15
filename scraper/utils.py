import os
import logging
from urllib.parse import quote

from . import dashboard

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

def logger_setup(name):
    # setup a logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Create handlers
    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler("scraper.log")
    c_handler.setLevel(logging.INFO)
    f_handler.setLevel(logging.DEBUG)

    # Create formatters and add it to handlers
    c_format = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
    f_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    return logger

def encoded_url(name: str):
    encoded_search = quote(name).replace("%20", "+")
    encoded__url = dashboard.SEARCH_URL.format(encoded_search=encoded_search, PORTAL_URL=os.environ["PORTAL_URL"])
    return encoded__url
