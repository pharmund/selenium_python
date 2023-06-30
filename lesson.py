from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = "C:\\Users\\Redmi\\Desktop\\Selenium2\\yandexdriver.exe"
chrome_options.add_argument("disable-infobars");
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com")
time.sleep(10)
user_name = driver.find_element_by_id('user-name')
user_name.send_keys("standard_user")

time.sleep(10)
# while True:
#     pass
driver.close()



