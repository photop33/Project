from rest_app import user
from db_connector import select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

res = requests.post('http://127.0.0.1:5000/users/1', json={"user_name": "itay"})

res = requests.get('http://127.0.0.1:5000/users/1')

select()

driver = webdriver.Chrome(executable_path="C:\\Users\\Itay Zrihan\\Desktop\\ChromeDriver.exe")
driver.get("http://127.0.0.1:5001/users/2")