import time
import random
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Function to randomly change user-agent
user_agents = [
   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.105 Safari/537.36',
    
]
random_user_agent = random.choice(user_agents)

# for i in range(num_requests):
# proxy = '160.86.242.23:8080'

# Create new Chrome options 
# for each request
options = uc.ChromeOptions()
options.add_argument("--log-level=3")  # Suppresses most log messages
options.add_argument("--disable-logging") 
# options.add_argument("--headless")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument(f'user-agent={random_user_agent}')
# options.add_argument(f'user-agent={ua.random}')
# options.add_argument("--start-maximized")

# options.add_argument(f'--proxy-server={proxy}')

# Initialize the driver with the current proxy
# driver = uc.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))

# Navigate to the website
driver.get("https://x.com/")
driver.maximize_window()
# Wait for a random time between actions to mimic human behavior
# time.sleep(random.uniform(2, 5))

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
print("LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL...........................................LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL]PPPPPPPPPPPPPPPPPPPPPP")
result = driver.execute_script("return typeof window === 'object';")
print("JavaScript enabled;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;:", result)

submit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[4]/a')))
submit.click()
# time.sleep(1000)
email = WebDriverWait(driver, 35).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input'))
)
email.send_keys("@KaurKamalp68671")
submit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]')))
submit.click()
email = WebDriverWait(driver, 15).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'))
)
email.send_keys("Kamal@1234")
submit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button')))
submit.click()
print("LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]")
result = driver.execute_script("return typeof window === 'object';")
print("JavaScript enabled...................................................................:", result)
for i in range(1,1000):
    try:
        image_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, f'//div/div/div[{i}]/div/div/article/div/div/div[2]/div[2]/div[3]/div/div/div/div/div/div/a/div/div[2]/div/img'))
        )
        # Get the source of the image
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",image_element)
        driver.execute_script("arguments[0].scrollIntoView();", image_element)
        image_src = image_element.get_attribute("src")
        # Wait until the image is visible after scrolling
        # WebDriverWait(driver, 10).until(
        #     EC.visibility_of(image_element)
        # )

        # # Get the source of the image
        # image_src = image_element.get_attribute("src")

        print("Image Source:", image_src)
    except:
        print("Image Source:>>>>>>>>>>>>>>>>")
# time.sleep(1000)
# Clean up
driver.quit(
    
)
