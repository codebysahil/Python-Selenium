from selenium import webdriver

browserName = input("Enter Browser Name")
if browserName.lower() == "chrome":
    driver = webdriver.Chrome()
elif browserName.lower() == "firefox":
    driver = webdriver.Firefox()
elif browserName.lower() == "edge":
    driver= webdriver.Edge()
else:
    print("No such browser")
    print(browserName.islower())
