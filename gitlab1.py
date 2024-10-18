from seleniumbase import Driver

driver = Driver(uc=True)
url = "https://gitlab.com/users/sign_in"
driver.uc_open_with_reconnect(url, 4)
driver.maximize_window()
driver.uc_gui_click_captcha()
driver.sleep(100)
driver.quit()   