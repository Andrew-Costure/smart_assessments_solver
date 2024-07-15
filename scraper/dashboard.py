from selenium.webdriver.common.by import By

# Selectors to use in selenium for navigation
SEARCH = ()
COURSE_CARDS = ()
COURSE_TITLE = ()
COURSE_LINK = ()

# Search URL
# This helps in checking whether the browser has reached a specific url or not
# The encoded text is used to search for courses with certain keywords in their names
# It is simply a representation of the query made by the portal itself
SEARCH_URL = "https://{PORTAL_URL}/enrollments?q={encoded_search}&status=all"
