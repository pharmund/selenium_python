from selenium import webdriver
import time
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = "C:\\Users\\Redmi\\Desktop\\Selenium2\\yandexdriver.exe"
chrome_options.add_argument("disable-infobars");
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com")
user_name = driver.find_element(By.ID, "user-name")
user_name.send_keys("standard_user")
time.sleep(5)
# while True:
    # pass



