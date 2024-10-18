
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import undetected_chromedriver as uc
# from fake_useragent import UserAgent
import requests
from selenium_stealth import stealth
import pickle
from itertools import cycle
import random
# proxy =  160.86.242.23:8080
# proxies = ['154.236.177.100']
# proxy_pool = cycle(proxies)
num_requests = 5

# ua = UserAgent()

# for i in range(num_requests):
proxy = '160.86.242.23:8080'

# Create new Chrome options 
# for each request
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
]
random_user_agent = random.choice(user_agents)

profile_path = r"C:\Users\VIS\AppData\Local\Google\Chrome\User Data\Profile 2"

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
driver.get("https://in.linkedin.com/")
driver.maximize_window()
# driver.maximize_window()

# After initializing the driver

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

try:
    submit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-content"]/section[1]/div/div/div[2]/a')))
    submit.click()

    email = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="username"]'))
    )
    email.send_keys("kamalpreetvinni@gmail.com")

    password = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]'))
    )
    password.send_keys("Kamal@123")
    # Wait for and click the submit button
    submit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')))

    submit.click()
except:
    print(">>>>>>>>>>>>>>>>>>>>>>>>already")
cookies = driver.get_cookies()
with open('cookies.pkl', 'wb') as f:
    pickle.dump(cookies, f)

submit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="global-nav"]/div/nav/ul/li[3]/a')))
submit.click()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(6)

submit = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[6]/div[3]/div/div[3]/div/div/main/div/div[1]/div[3]/div/div/div/section/div[2]/a')))
submit.click()
l=[]
for j in range(1,10):
    for i in range(1,26):
        try:
            submit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div[1]/div/ul/li[{i}]/div/div/div[1]/div/div[2]/div[1]/a')))

            time.sleep(1)
            driver.execute_script("arguments[0].scrollIntoView(true);", submit)
            actions = ActionChains(driver)
            actions.move_to_element(submit).click().perform()
            l.append(submit.text)
        except Exception as e:
            print(e,"eeeee")
    try:
        submit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div[1]/div/div[4]/ul/li[{j}]/button')))        

        actions = ActionChains(driver)
        actions.move_to_element(submit).click().perform()
    except Exception as e:
        print(e,"eee>>>>>>>>>>>>>ee") 
 
 
 
print(l)















