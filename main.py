import os
from pathlib import Path
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
from pages.portals import Portals

dotenv_path = Path('data/.env')
load_dotenv(dotenv_path = dotenv_path)
BASE_URL = os.environ.get("BASE_URL")

driver = webdriver.Firefox()

base = BasePage(driver, WebDriverWait(driver, 35), BASE_URL)
base.go_to_page(BASE_URL)
base.wait_for_login()

portals = Portals(base)
portals.start_portal_loop()
