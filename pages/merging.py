import datetime
from threading import Timer
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class Merging(BasePage):
    """
    Merging class for managing the merging page and any relevant methods.
    """
    def __init__(self, parent):
        """
        Constructor for the Merging class.
        
        Args:
            parent (:obj): The "parent" parameter is the BasePage object from which the current class 
                is derived. It is used to access the driver, wait, base_url, and locator attributes of the parent class.
                
        Attributes:
            merge_url (str): Uses base_url to generate a merge base url.
            merge_timers (dict of str: str): Dict of merge name and last time of opening.
        """
        self.merge_url = parent.base_url + "/merge.php?merge="
        self.merge_timers = {}
        super().__init__(parent.driver, parent.wait, parent.base_url)

    def merge(self, merge_url):
        """
        Checks if the current URL matches the merge URL, navigates to the merge URL if
        necessary, waits for the merge page to load, checks for the merge error message, clicks the merge submit
        button if no errors are found, and returns an array of the merge name and current datetime.
        
        Args:
            merge_url (str): URL of the current targeted merging level page.
        
        Returns:
            Returns either `False` or a list containing the merge name and the current date and time.
        """
        if not merge_url in self.driver.current_url:
            self.go_to_page(merge_url)
            self.wait.until(EC.url_to_be(merge_url))
            self.wait.until(EC.visibility_of_element_located(self.locator.MERGE_NAME))
            self.wait.until(EC.text_to_be_present_in_element(self.locator.MERGE_NAME, "Merging"))
        merge_error = self.driver.find_elements(*self.locator.MERGE_ERROR)
        if not merge_error:
            self.wait.until(EC.element_to_be_clickable(self.locator.MERGE_SUBMIT)).click()
            return False
        merge_name = self.wait.until(EC.visibility_of_element_located(self.locator.MERGE_NAME)).text
        return [merge_name , datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")]

    def merge_all(self, _min, _max, event):
        """
            Iterates through a range of merge IDs, sets the URL for each merge page and opens it using
            the merge() class method. While merge() returns False and the threading.Event flag is not set, continue merging.
            If threading.Event flag is set, return quietly. If merge() returns with a list, set or append current merge
            name and current datetime to the class instance dictionary attribute, merge_timers.
        
        Args:
            _min (int): Sets the lower bound of the merge IDs to loop through. It
                determines the starting point of the loop.
            _max (int): Sets the upper bound of the merge IDs to loop through. It is used to
                determine the range of merge ID's to iterate over in the `merge_all` method.
            event (:obj): Instance of the threading.Event class. It is used to
                synchronize and communicate between different threads. Controls the
                execution of the loop by setting and clearing the event flag.
        """
        _max = _max + 1
        current_merge = self.merge_url + str(_min + len(self.merge_timers)) #: Calculate current merging url by getting the count of key value pairs in merge_timers.
        res = False
        while res is False:
            if event.is_set():
                break
            res = self.merge(current_merge)
        if not event.is_set():
            merge_name, merge_time = res
            self.merge_timers[merge_name] = [merge_time]
            print(f"[{merge_time}]: Ran out of '{merge_name.replace(' Merging', '')}' merges.")

    def start_merge_loop(self, event):
        """
        Starts a merge event loop, runs the merge_all() class method, and starts a threading.Timer object to generate a perpetual timed loop of itself.
        
        Args:
            event (:obj): Instance of the threading.Event class. It is used to
                synchronize and communicate between different threads. Controls the
                execution of the loop by setting and clearing the event flag.
        """
        self.merge_all(3, 7, event)
        Timer(0.3, self.start_merge_loop, [event]).start()
