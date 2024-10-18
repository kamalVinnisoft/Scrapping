
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import undetected_chromedriver as uc
import requests
from selenium_stealth import stealth
import pickle
from itertools import cycle
import random
user_agents = [
   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.105 Safari/537.36',
    
]
random_user_agent = random.choice(user_agents)

options = uc.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)
options.add_argument(f'user-agent={random_user_agent}')
driver = uc.Chrome(version_main=129, options=options)
# driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
print(">>>>>>>>>>>>>>>>>>>>>>>>",driver)
# Navigate to the website
driver.get("https://chatgpt.com/")
driver.maximize_window()
driver.refresh()
time.sleep(1000)