import os
import logging
import time
import random
from sys import argv
from pyvirtualdisplay import Display
from selenium import webdriver

logging.getLogger().setLevel(logging.INFO)

DOMAIN_NAME = "wireshark"

url_to_request = [
    "http://wireshark:14500/login.html",
]
cookies = [
    {"name": "username", "value": "admin"},
    {"name": "session", "value": "image_this_to_be_a_complicated_token_for_a_user_session"},
    {"name": "session", "value": "image_this_to_be_a_complicated_token_for_the_admin_session"},
]


def request_in_order(driver, time_between_request: int = 1):
    for cookie in cookies:
        driver.add_cookie({'name':'foo','value':'bar'})
        for url in url_to_request:
            driver.get(url)
            logging.info("Accessed %s ..", url)
            logging.info("Page title: %s", driver.title)
        #driver.delete_all_cookies()
        time.sleep(time_between_request)


def request_random(driver,number_of_request: int = 1, time_between_request: int = 1):
    for _ in range(0, number_of_request):
        driver.add_cookie(random.choice(cookies))
        url_requested = random.choice(url_to_request)
        driver.get(url_requested)
        driver.delete_all_cookies()
        time.sleep(time_between_request)
        logging.info("Accessed %s ..", url_requested)
        logging.info("Page title: %s", driver.title)


def launch_request():
    display = Display(visible=0, size=(800, 600))
    display.start()
    logging.info("Initialized virtual display..")

    # Set options for chromedriver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_experimental_option(
        "prefs",
        {
            "download.default_directory": os.getcwd(),
            "download.prompt_for_download": False,
        },
    )
    logging.info("Prepared chrome options..")
    #Wait for the Wireshark docker to run
    time.sleep(15)
    browser = webdriver.Chrome(options=chrome_options)
    logging.info("Initialized chrome browser..")
    # First request to set the domain and be able to add cookies after
    browser.get(url_to_request[0])

    while True:
        request_random(browser)
   
    #browser.quit()
    #display.stop()


if __name__ == "__main__":
    launch_request()
