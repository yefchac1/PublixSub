
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# This is the path to the chromedriver on my computer called Anita.

anita_path = "/opt/homebrew/bin/chromedriver"

service = Service(anita_path)
web_driver = webdriver.Chrome(service=service)
web_driver.get("https://www.publix.com/mc/order-ahead/order-deli-online")

#time.sleep(5)

web_driver.quit()