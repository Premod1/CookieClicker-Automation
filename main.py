from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service)
driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(20)
lang_select_button = driver.find_element("id", "langSelect-EN")
lang_select_button.click()
time.sleep(2)
cookie = driver.find_element("id", "bigCookie")

start_time = time.time()

while time.time() - start_time < 300:
    cookie.click()
    time.sleep(0.1)


print("Done")
