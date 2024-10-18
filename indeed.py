
from seleniumbase import Driver
import time

driver = Driver(uc=True)
print(driver)
driver.get("https://in.indeed.com/")

driver.maximize_window()
driver.click('a.css-ixhkq1')

driver.click('#login-google-button')
driver.switch_to_window(1) 
driver.type('#identifierId', 'kamalpreetvinni@gmail.com')
# driver.wait_for_element_visible("div.VfPpkd-RLmnJb[aria-label='Sign in']")
driver.click('//*[@id="identifierNext"]/div/button')
driver.type('//*[@id="password"]/div[1]/div/div[1]/input', 'Kamal@123')
driver.click('//*[@id="passwordNext"]/div/button')

time.sleep(35)
driver.quit()

