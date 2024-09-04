import time

from selenium import webdriver # webdriver is class
# Chrome Driver service
driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.maximize_window()
print(driver.title) # property title
print(driver.current_url) # property current_url
time.sleep(6)
