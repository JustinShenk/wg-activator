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

# Login
driver = webdriver.Chrome('/Applications/chromedriver')
driver.get('https://wg-gesucht.de')
# Remove cookie button
btn = driver.find_element_by_id("cookie-confirm").click()
driver.find_element_by_link_text("LOGIN").click()
username = driver.find_element_by_id("login_email_username")
password = driver.find_element_by_id("login_password")
username.send_keys(USERNAME)
password.send_keys(PASSWORD)
driver.find_element(By.XPATH, "//*[@id='login_basic']/div[5]/input").click()
time.sleep(5)

while True:
    # Open listing
    driver.get(
        LISTING_URL)
    time.sleep(5)
    driver.find_element_by_id("step_one_submit").click()

    # Refresh listing
    elem = driver.find_element_by_class_name('btn-orange')
    elem.click()
    assert 'zehn Minuten' in driver.page_source
    print("Reloaded at {}".format(datetime.now().strftime("%Y-%m-%d %H:%M")))
    time.sleep(DELAY)
