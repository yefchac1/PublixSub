
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


# This is the path to the chromedriver on my computer called Anita.

anita_path = "/Users/yeferson/Desktop/CodePath/GitHub/PublixSub/chromedriver"

webdriver = webdriver.Chrome(anita_path)

webdriver.get("https://www.publix.com/mc/order-ahead/order-deli-online")

time.sleep(5)

webdriver.quit()