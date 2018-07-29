#!/usr/bin/env python3
import time
from configparser import ConfigParser

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Load configuration
config = ConfigParser()
conf_file = open('config.ini')
config.readfp(conf_file)
USERNAME = config.get('Login', 'email')
PASSWORD = config.get('Login', 'password')
LISTING_URL = config.get('Listing', 'listing_url')
DELAY = int(config.get('Driver', 'delay'))
CHROMEDRIVER_PATH = '/usr/local/bin/chromedriver' # mac-only

# Login
driver = webdriver.Chrome(CHROMEDRIVER_PATH)
driver.get('https://wg-gesucht.de')
# Remove cookie button
btn = driver.find_element_by_id("cookie-confirm").click()
driver.find_element_by_link_text("LOGIN").click()
time.sleep(1)
username = driver.find_element_by_name("login_email_username")
password = driver.find_element_by_id("login_password")
username.send_keys(USERNAME)
password.send_keys(PASSWORD)
driver.find_element_by_id('login_submit').click()
time.sleep(5)

while True:
    # Open listing
    driver.get(
        LISTING_URL)
    time.sleep(3)
    contact = driver.find_element_by_class_name('bottom_contact_box')
    edit = contact.find_element_by_link_text('ANGEBOT BEARBEITEN')
    edit.send_keys(Keys.TAB)
    time.sleep(1)
    edit.click()
    time.sleep(3)

    # Refresh listing
    btn = driver.find_element_by_class_name('btn-orange') # weiter
    btn.send_keys(Keys.TAB)
    time.sleep(2)
    btn.send_keys(Keys.SPACE)
    btn = driver.find_element_by_class_name('btn-orange') # Änderungen ubernehmen
    btn.send_keys(Keys.TAB)
    time.sleep(2)
    btn.send_keys(Keys.SPACE)
    assert 'zehn Minuten' in driver.page_source
    print("Reloaded at {}".format(datetime.now().strftime("%Y-%m-%d %H:%M")))
    time.sleep(DELAY)
