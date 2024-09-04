# Switch to different window using selenium and python

import time
from selenium.webdriver.chrome.options import Options

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

# driver = webdriver.Chrome()
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.letskodeit.com/practice")
driver.maximize_window()
print(driver.title)
print(driver.current_url)

# Find the parent window handle

parent_handle = driver.current_window_handle
print(parent_handle)  # 2631D1330608C57C6A408B5CF39369B7

# Find open window button and click it .
driver.find_element(By.ID, "openwindow").click()
time.sleep(4)

# Find all the handles after clicking open window button
handles = driver.window_handles

# print all handles and switch to new handle and search for the course

for handle in handles:
    print(handle)  # 2631D1330608C57C6A408B5CF39369B7, # 0E07B25227B361536CF49871632EE9A3
    if handle not in parent_handle:
        driver.switch_to.window(handle)
        print("Switched to new window")
        driver.maximize_window()
        driver.find_element(By.NAME, "course").send_keys("python")
        time.sleep(3)
        driver.close()  # this will close only the window that has the focus not all the windows
        break

# switch back to main page
driver.switch_to.window(parent_handle)
driver.find_element(By.ID, 'name').send_keys("Test Successful")

time.sleep(5)

driver.quit()
