
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

# proxy =  160.86.242.23:8080
# proxies = ['154.236.177.100']
# proxy_pool = cycle(proxies)
num_requests = 5

ua = UserAgent()

# for i in range(num_requests):
proxy = '160.86.242.23:8080'

# Create new Chrome options 
# for each request
options = uc.ChromeOptions()

# options.add_argument("--headless")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
# options.add_argument(f'user-agent={ua.random}')
# options.add_argument("--start-maximized")

# options.add_argument(f'--proxy-server={proxy}')

# Initialize the driver with the current proxy
# driver = uc.Chrome(options=options, service=Service(ChromeDriverManager().install()))
driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
print(driver)
stealth(driver,
       user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.105 Safari/537.36',
       languages=["en-US", "en"],
       vendor="Google Inc.",
       platform="Win32",
       webgl_vendor="Intel Inc.",
       renderer="Intel Iris OpenGL Engine",
       fix_hairline=True,
       )
driver.get("https://in.linkedin.com/")
driver.maximize_window()
# driver.maximize_window()



# After initializing the driver

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
print("LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL")


submit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-content"]/section[1]/div/div/div[2]/a')))
submit.click()

# time.sleep(6000)
# time.sleep(10)
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
print("ttttttttttttttttttttttttttttt",submit)
submit.click()
cookies = driver.get_cookies()
print(">>>>>>>>>>>>>>>>sssssssssssss>>>>>>>>>>>>>cookieeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",cookies)
with open('cookies.pkl', 'wb') as f:
    pickle.dump(cookies, f)
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>cookieeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",cookies)
# time.sleep(6000)
# time.slee(10)
submit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="global-nav"]/div/nav/ul/li[3]/a')))
submit.click()
# time.sleep(6000)
submit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div[3]/div/div[3]/div/div/main/div/div[1]/div[4]/div/div/div/section/ul/div/div/a')))
submit.click()
# time.sleep(6000)
l=[]
for j in range(1,10):
    for i in range(1,26):
        try:
            submit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div[1]/div/ul/li[{i}]/div/div/div[1]/div/div[2]/div[1]/a')))
            # print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh",submit)
            time.sleep(1)
            driver.execute_script("arguments[0].scrollIntoView(true);", submit)
            actions = ActionChains(driver)
            actions.move_to_element(submit).click().perform()
            l.append(submit.text)
        except Exception as e:
            print(e,"eeeee")
    try:
        submit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div[1]/div/div[4]/ul/li[{j}]/button')))        
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>ggggg",submit)
        actions = ActionChains(driver)
        actions.move_to_element(submit).click().perform()
    except Exception as e:
        print(e,"eee>>>>>>>>>>>>>ee") 
        # time.sleep(6000)
           
    # time.sleep(6000)
print(l)




# # iframe = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/section[1]/div/div/div[1]/div/div/div/iframe')))
    
# #     # Switch to the iframe
# # driver.switch_to.frame(iframe)
# print("Switched to iframe successfully.")

# # Wait for the button inside the iframe to be clickable
# button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div/div[2]')))
# button.click()
# print("Button clicked.")
# actions = ActionChains(driver)
# actions.move_to_element(button).click().perform()
























# //*[@id="identifierId"]
# button = WebDriverWait(driver, 25).until(
#         EC.presence_of_element_located((By.XPATH, '/html/body/nav/ul/li[4]/a')))
# button.click()
# button = WebDriverWait(driver, 25).until(
#         EC.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/section/ul/li[4]/div/a')))
# button.click()
# # time.sleep(20)
# button = WebDriverWait(driver, 40).until(
#         EC.presence_of_element_located((By.XPATH,'//*[@id="main-content"]/section[2]/section[3]/div/section/a')))
# driver.execute_script("arguments[0].scrollIntoView(true);", button)
# time.sleep(7)
# button.click()
# button = WebDriverWait(driver, 25).until(
#         EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/div/div[2]')))
# button.click()

# # Set up the WebDriver (Chrome in this case)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get("https://www.airbnb.co.in/")
# driver.maximize_window()
# time.sleep(6)

# # elements = driver.find_elements(By.XPATH,"//div[contains(@class, 'a1djnv4w') and contains(@class, 'atm_mk_stnw88') and contains(@class, 'atm_c8_o7aogt') and contains(@class, 'atm_g3_8jkm7i') and contains(@class, 'atm_cs_10d11i2') and contains(@class, 'atm_e2_8jkm7i') and contains(@class, 'c1irrjfm') and contains(@class, 'atm_k4_kb7nvz') and contains(@class, 'dir') and contains(@class, 'dir-ltr')]")
# # 
# # print(elements)
# for i in range(0,500):
#     elements = driver.find_elements(By.XPATH,"//div[contains(@class, 'a1djnv4w') and contains(@class, 'atm_mk_stnw88') and contains(@class, 'atm_c8_o7aogt') and contains(@class, 'atm_g3_8jkm7i') and contains(@class, 'atm_cs_10d11i2') and contains(@class, 'atm_e2_8jkm7i') and contains(@class, 'c1irrjfm') and contains(@class, 'atm_k4_kb7nvz') and contains(@class, 'dir') and contains(@class, 'dir-ltr')]")
#     for e in elements:
#         print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",e.text)
        
# # element =driver.find_element(By.XPATH, '//*[@id="site-content"]/div[2]/div[1]/div/div/div/div[1]/div/div[2]/div/div/div/div/a')
# # time.sleep(3)
# # print(element)
# # # driver.execute_script("arguments[0].scrollIntoView(true);", element)
# # element.click()
# # actions = ActionChains(driver)
# # actions.move_to_element(element).click().perform()
# time.sleep(2)
# print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
# # element.click()
# driver.quit()

