
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import undetected_chromedriver as uc
from fake_useragent import UserAgent
import requests
from selenium_stealth import stealth
import pickle
from itertools import cycle
import random

num_requests = 5

ua = UserAgent()

# for i in range(num_requests):
proxy = '160.86.242.23:8080'

# Create new Chrome options 
# for each request
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.2 Mobile/15E148 Safari/604.1',
]
random_user_agent = random.choice(user_agents)


# Create Chrome options
options = uc.ChromeOptions()
# options.add_argument(f"user-data-dir={profile_path.rsplit('\\', 1)[0]}")  # User data directory
# options.add_argument(f"profile-directory={profile_path.split('\\')[-1]}")

options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument(f'--user-agent={random_user_agent}')
options.add_experimental_option("useAutomationExtension", False)

# Initialize ChromeDriver using webdriver-manager
driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
print(driver)
driver.get("https://www.instagram.com/")
driver.maximize_window()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))



try:
    email = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input'))
    )
    email.send_keys("kamalpreetvinni7")

    password = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input'))
    )
    password.send_keys("Kamal@1234")
    # Wait for and click the submit button
    submit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')))

    submit.click()
    # time.sleep(1000)
except:
    print(">>>>>>>>>>>>>>>>>>>>>>>>already")
submit = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/section/div/button')))
submit.click()
submit = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')))
submit.click()

submit = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[4]/span/div/a/div/div[2]/div/div/span')))
submit.click()
# time.sleep(1200)
for i in range(1,10000,2):
    print(i)
    try:
        a = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div[{i}]/div/div[2]/div[2]/div/div/div/div/span/span')))
        driver.execute_script("arguments[0].scrollIntoView(true);", a)
        print(a.text)

        ss = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[role='button'] svg[aria-label='Save']")))
        print(">>>>>>>>>>>>>>",ss)
        actions = ActionChains(driver)
        actions.move_to_element(ss).click().perform()
    except:
        print(">>>>>>>>>>>>>>>>aaaaaaa")
    try:
        b = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div[{i}]/div/div[2]/div[1]/div/div/div/span/span')))
        print(b.text)    
    except:
        print(">>>>>>>>>>>>>>bbbbbbbbbbbbbbbbbbbbb")
    try:
        c = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div[{i}]/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[1]/div[2]/div/div[1]/a')))
        print(c.text)
    except:
        print(">>>>>>>>>>>>>>cccccc")
