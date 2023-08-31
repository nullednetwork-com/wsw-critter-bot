from selenium.webdriver.common.by import By

class PageLocators:

    CARD_DECK = (By.CLASS_NAME, "card-deck")
    CARDS = (By.CLASS_NAME, "cards")

    PORTAL_NAME = (By.XPATH, "//div/h3")
    PORTAL_TIMER = (By.ID, "timer")
    PORTAL_STALENESS_CHECK_ELE = (By.XPATH, "//body/div[@class='container']/*[position()=2]")
    