from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import undetected_chromedriver as uc

import pickle
import random
from urllib.parse import urlparse
from selenium_stealth import stealth
import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import json
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
]
random_user_agent = random.choice(user_agents)



# Create Chrome options
options = uc.ChromeOptions()
user_data_dir = r"C:\Users\VIS\AppData\Local\Google\Chrome\User Data"
profile_name = "Kamalpreet"  # Ensure this is the correct profile name
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument(f'--user-agent={random_user_agent}')
options.add_experimental_option("useAutomationExtension", False)

# Initialize ChromeDriver using webdriver-manager
driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True)

headers = {
    # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://gitlab.com/users/sign_in",
    "Connection": "keep-alive",
    "Accept-Encoding": "gzip, deflate, br"
}

# # Set the headers for all future requests
driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": headers})
driver.get("https://gitlab.com/users/sign_in")
driver.maximize_window()
cookies = [
    {
        'name': '_cfvid',
        'value': 'JRjSkYkAScypI28LcrI7w_zkYExCy5iWd17eqMWwOes-1727778592242-0.0.1.1-604800000',  # Use the actual value
        'domain': 'gitlab.com',
        'path': '/',
    },
    {
        'name': 'cf_clearance',
        'value': 'nlsVrKHimtoWu25TGmnF57Ls0rU3JOrZmta6oKVUMEI-1727783259-1.2.1.1-IwZNWd07Ax7.8adPV4A2v8sdbMV.pIaAuW9O4iufNmhhibfZBTVrq_MCdsJ12MGyCQs3WuGjjNI1ClGGCusbgiuhmv5muum290_2D4pNRst1OjHR_Im8jehh1c2UAlSnSzt38uXkLxLQ9IxsIknRHIN_88jEMs4u2kEH9F7TvYffKOnCFZPeDUem100FT_y2QQD23ILg6f0QTFSuc8B4RljPmymCoQVGWTfCwNe3EvwP6VuJDs51iO49CG3.mtrId4ZKTDJLPyqhJMauv8AFQgpCpxk0t.Uz9tObpuzkiXZGlHZ9h.iVKDpkcHz_sDEH0me2l64iOhQy_vFHOjdHjsmThXRCG4W44LOwPrXfc2hBHNG5OPId4wrwguB2Jzu8_FxNhcaoJtK.hFNTn6BCz16yA6x80NGTe.G7Z9izAIlgMIVB1at5b91lfv2e6uRm',  # Use the actual value
        'domain': 'gitlab.com',
        'path': '/',
    },
    {
        'name': 'cf_chl_rc_m',
        'value': '3',  # Use the actual value
        'domain': 'gitlab.com',
        'path': '/',
    },
    {
        'name': '_gitlab_session',
        'value': 'de1c39a5fcdabf87303864e2d1d1a779',  # Use the actual value
        'domain': 'gitlab.com',
        'path': '/',
    },
]



    
with open('cookies.json', 'r') as file:
    cookies = json.load(file)

# Add cookies to the current session
for cookie in cookies:
    driver.add_cookie(cookie)

# Optional: Verify that cookies have been added
print(driver.get_cookies())  # This should show the loaded cookies

# Now you can navigate to a page that requires those cookies
driver.get('https://gitlab.com/users/sign_in')
driver.maximize_window()
time.sleep(1200)

