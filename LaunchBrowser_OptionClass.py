import time
from selenium.webdriver.chrome.options import Options

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

# driver = webdriver.Chrome()
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://rahulshettyacademy.com/client")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

driver.find_element(By.ID,"userEmail").send_keys("testabc@gmail.com")
driver.find_element(By.ID,"userPassword").send_keys("admin123")
time.sleep(6)
driver.find_element(By.XPATH,"//input[@name='login']").click()

time.sleep(6)

