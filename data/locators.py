from selenium.webdriver.common.by import By


class PageLocators:
    """
    The `PageLocators` class contains Selenium locators for various elements on a web page.
    """
    CARD_DECK = (By.CLASS_NAME, "card-deck")
    CARDS = (By.CLASS_NAME, "cards")

    PORTAL_NAME = (By.XPATH, "//div/h3")
    PORTAL_TIMER = (By.ID, "timer")
    PORTAL_STALENESS_CHECK_ELE = (By.XPATH, "//body/div[@class='container']/*[position()=2]")

    MERGE_NAME = (By.XPATH, "//div/h2")
    MERGE_SUBMIT = (By.XPATH, "//div/form/input[@value='Merge Critters']")
    MERGE_ERROR = (By.XPATH, "//*[text()[contains(., 'ERROR')]]")
