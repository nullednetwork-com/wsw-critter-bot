from selenium.webdriver.support import expected_conditions as EC
from data.locators import PageLocators

class BasePage:
    """
    BasePage class modeled from the Selenium Page Object Model
    """
    def __init__(self, driver, wait, url):
        """
        Constructor for the BasePage class.
        
        Args:
            driver (:obj): Instance of a Selenium web driver. It is responsible for controlling the browser and interacting with web elements on the
                page.
            wait (:obj): Instance of a Selenium WebDriverWait class. Waits for an element to be present or visible before throwing an exception.
                It is typically used to ensure that the web page has finished loading before interacting with its elements.
            url (str): Base URL of the website that you want to automate. It is used to
                navigate to different pages within the website.
                
        Attributes:
            locator (:obj): Class instance of Selenium Page Locators.
        """
        self.driver = driver
        self.wait = wait
        self.base_url = url
        self.locator = PageLocators

    def go_to_page(self, url):
        """
        Opens url in Selenium web driver

        Args:
            url (str): URL to open
        """
        self.driver.get(url)

    def get_title(self):
        """
        Returns:
            The title of the web page that is currently being displayed in the browser.
        """
        return self.driver.title

    def wait_for_login(self):
        """
        Waits for the login process to complete by checking for a change in the URL and the
            presence of a specific element.
        """
        self.wait.until(EC.url_changes(self.driver.current_url))
        self.wait.until(EC.presence_of_element_located(self.locator.CARD_DECK))
