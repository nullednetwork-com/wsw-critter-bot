import datetime
import threading
from threading import Timer
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class Portals(BasePage):
    def __init__(self, instance):
        self.locator = instance.locator
        self.portal_url = instance.base_url + "/portaltest.php?portal="
        self.portal_timers = {}
        self.portal_lock = threading.Lock()
        super().__init__(instance.driver, instance.wait, instance.base_url)

    def open(self, portal):
        staleness_check_ele = self.driver.find_element(*self.locator.PORTAL_STALENESS_CHECK_ELE)
        self.go_to_page(portal)
        self.wait.until(EC.url_to_be(portal))
        self.wait.until(EC.staleness_of(staleness_check_ele))
        portal_name = self.wait.until(EC.visibility_of_element_located(self.locator.PORTAL_NAME)).text
        print([portal_name, datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")])
        return [portal_name, datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")]

    def open_all(self, _min, _max):
        _max = _max + 1
        for i in range(_min, _max):
            base_portal_id = 310
            current_portal = self.portal_url + str(base_portal_id + i)
            portal_name, portal_time = self.open(current_portal)
            self.portal_timers[portal_name] = [portal_time]

    def start_portal_loop(self):
        with self.portal_lock:
            self.open_all(2, 8)
            portal_timer = Timer(120.0, self.start_portal_loop)
            portal_timer.start()
