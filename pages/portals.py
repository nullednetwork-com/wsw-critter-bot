import datetime
from threading import Timer
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class Portals(BasePage):
    """
    Portals class for managing the portal page and any relevant methods.
    """
    def __init__(self, parent):
        """
        Constructor for the Portals class.
        
        Args:
            parent (:obj): The "parent" parameter is the BasePage object from which the current class 
                is derived. It is used to access the driver, wait, base_url, and locator attributes of the parent class.
            
        Attributes:
            portal_url (str): Uses base_url to generate a portal base url.
            portal_timers (dict of str: str): Dict of portal name and last time of opening.
        """
        self.portal_url = parent.base_url + "/portaltest.php?portal="
        self.portal_timers = {}
        super().__init__(parent.driver, parent.wait, parent.base_url)

    def open(self, portal: str):
        """
        Opens a portal, waits for the page to load, checks for staleness of an element,
            retrieves the portal name, and returns the portal name and the current date and time.
        
        Args:
            portal (str): The "portal" parameter is a string that represents the URL of the portal that needs
                to be opened.
        
        Returns:
            The open() method returns a list containing the portal name and the current date and time in the
        format "mm/dd/yyyy, hh:mm:ss".
        """
        staleness_check_ele = self.driver.find_element(*self.locator.PORTAL_STALENESS_CHECK_ELE)
        self.go_to_page(portal)
        self.wait.until(EC.url_to_be(portal))
        self.wait.until(EC.staleness_of(staleness_check_ele))
        portal_name = self.wait.until(EC.visibility_of_element_located(self.locator.PORTAL_NAME)).text
        return [portal_name, datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")]

    def open_all(self, _min: int, _max: int):
        """
        Iterates through a range of portal IDs, sets the URL for each portal, opens
            it, and records the portal name and opening time as a dictionary in the instances portal_timers attribute.
        
        Args:
            _min (int): Sets the lower bound of the portal IDs to loop through. It
                determines the starting point of the loop.
            _max (int): Sets the upper bound of the portal IDs to loop through. It is used to
                determine the range of portal ID's to iterate over in the `open_all` method.
        """
        _max = _max + 1
        for i in range(_min, _max):
            base_portal_id = 310
            current_portal = self.portal_url + str(base_portal_id + i)
            portal_name, portal_time = self.open(current_portal)
            self.portal_timers[portal_name] = [portal_time]
            if i == _max - 1:
                print(f'[{portal_time}]: Portal opening routine completed.')

    def start_portal_loop(self, event):
        """
        Starts a portal event loop, sets a threading event flag to break out of ongoing threads, runs
        the open_all() method, sets a timer to generate a perpetually timed loop, and clears the event flag
        after finishing.
        
        Args:
            event (:obj): Instance of the threading.Event class. It is used to
                synchronize and communicate between different threads. Controls the
                execution of the loop by setting and clearing the event flag.
        """
        event.set()
        self.open_all(2, 8)
        portal_timer = Timer(120.0, self.start_portal_loop, [event])
        portal_timer.start()
        event.clear()
