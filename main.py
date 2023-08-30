from pathlib import Path
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage



dotenv_path = Path('data/.env')
load_dotenv(dotenv_path = dotenv_path)

driver = webdriver.Firefox()

# base = BasePage(driver, WebDriverWait(driver, 35))
