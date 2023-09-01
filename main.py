import os
from pathlib import Path
from threading import Event
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
from pages.portals import Portals
from pages.merging import Merging


#: Safely get environment varables and assign to variable
dotenv_path = Path('data/.env')
load_dotenv(dotenv_path = dotenv_path)
BASE_URL = os.environ.get("BASE_URL")


#: Start a Selenium webdriver instance
driver = webdriver.Firefox()


#: Create the BasePage instance of Selenium's Page Object Model. Open url and wait to login.
base = BasePage(driver, WebDriverWait(driver, 35), BASE_URL)
base.go_to_page(BASE_URL)
base.wait_for_login()


#: Create an instance of Portals and an instance of Merging
portals = Portals(base)
merging = Merging(base)


#: Generate a threading.Event object so that we can start and stop the event loop threads when we need to.
event = Event()


#: Start the event loops
portals.start_portal_loop(event)
merging.start_merge_loop(event)
