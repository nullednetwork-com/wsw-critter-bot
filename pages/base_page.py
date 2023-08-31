from selenium.webdriver.support import expected_conditions as EC
from data.locators import PageLocators

class BasePage:

    def __init__(self, driver, wait, url):
        self.driver = driver
        self.wait = wait
        self.locator = PageLocators
        self.base_url = url

    def go_to_page(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def wait_for_login(self):
        self.wait.until(EC.url_changes(self.driver.current_url))
        self.wait.until(EC.presence_of_element_located(self.locator.CARD_DECK))
