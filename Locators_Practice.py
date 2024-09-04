import time
from selenium.webdriver.chrome.options import Options

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

# driver = webdriver.Chrome()
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.find_element(By.NAME,"email").send_keys("hell0@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("12345678")
driver.find_element(By.ID,"exampleCheck1").click()
# //XPATH tagname[@attribute = 'value'] //@input[type='submit']
# CSS Selector tagname[attribute = 'value']
driver.find_element(By.XPATH,"//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME,"alert-success").text
driver.find_element(By.CSS_SELECTOR,"input[name = 'name']").send_keys("testedname")
print(message)
assert "Success" in message

time.sleep(5)
