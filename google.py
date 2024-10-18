import time
import random
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Function to randomly change user-agent
user_agents = [
   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.105 Safari/537.36',
    
]
random_user_agent = random.choice(user_agents)

options = uc.ChromeOptions()
options.add_argument("--log-level=3")  
options.add_argument("--disable-logging") 
# options.add_argument("--headless")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument(f'user-agent={random_user_agent}')

driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))

# Navigate to the website
driver.get("https://www.ebay.com/b/Cell-Phone-Accessories/9394/bn_320095")
driver.maximize_window()
# time.sleep(10000)
n=2
try:
    for u in range(5):
        for j in range(n,11):
            print("888888888888888888888888888888888888",n)
            for i in range(1,61):
                if j==2:
                    data = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div[3]/div[3]/div[3]/section[2]/ul/li[{i}]/div[1]/div[2]/a/h3')))
                    submit = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div[3]/div[3]/div[3]/section[2]/div[2]/nav/ol/li[{j}]/a')))
                    c = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div[3]/div[3]/div[3]/section[2]/ul/li[{i}]/div[1]/div[2]/a')))
                else:
                    data = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div[3]/div[3]/div[3]/section[1]/ul/li[{i}]/div[1]/div[2]/a/h3')))
                    submit = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div[3]/div[3]/div[3]/section[1]/div[2]/nav/ol/li[{j}]/a')))
                    c = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div[3]/div[3]/div[3]/section[1]/ul/li[{i}]/div[1]/div[2]/a')))
                driver.execute_script("arguments[0].scrollIntoView(true);", data)
                driver.implicitly_wait(3)
                url=driver.current_url
                print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh",data.text)
                print(">>>>>>>>>>>>>>",c,c.tag_name)
                driver.execute_script("arguments[0].click();", c)
                # actions = ActionChains(driver)
                # actions.move_to_element(c).click().perform()
                
                print(driver.current_url)
                window_handles = driver.window_handles
                print(len(window_handles))
                time.sleep(5)
                if len(window_handles) > 1:
                    driver.switch_to.window(window_handles[1])
                    # Close the current tab (second tab)
                    driver.close()
                    print("Closed the second tab.")
                    
                    # Update window handles after closing
                    window_handles = driver.window_handles
                    
                    # Switch back to the first tab
                    if len(window_handles) > 0:
                        driver.switch_to.window(window_handles[0])
                        print("Switched back to the first tab:", driver.current_url)
                    else:
                        print("No tabs are left to switch to.")
                else:
                    # If no new tab was opened, just navigate to the URL
                    driver.get(url)
            # submit = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f' /html/body/div[3]/div[3]/div[3]/section[2]/div[2]/nav/ol/li[{j}]/a')))
            actions = ActionChains(driver)
            actions.move_to_element(submit).click().perform()
            print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        next_submit = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div[3]/div[3]/div[3]/section[1]/div[2]/nav/a[2]')))
        actions = ActionChains(driver)
        actions.move_to_element(next_submit).click().perform()
        n=7
except Exception  as e:
    print("LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL",e)
    time.sleep(1000)