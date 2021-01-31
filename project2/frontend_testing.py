from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\\Users\\Itay Zrihan\\Desktop\\ChromeDriver.exe")
driver.get("http://127.0.0.1:5001/users/get_user_data/1")
x = driver.find_element_by_id("user")
print(x)


