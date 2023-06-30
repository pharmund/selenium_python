from selenium import webdriver

def launchBrowser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = "C:\\Users\\Redmi\\Desktop\\Selenium2\\yandexdriver.exe"
    chrome_options.add_argument("disable-infobars");
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com")
    while True:
        pass


launchBrowser()
