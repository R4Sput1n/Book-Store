# Messing around with selenium

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Edge()
driver.get('http://localhost:8000/')
dict = {}

authors_elements = driver.find_elements(By.CLASS_NAME, "text-author-home")
authors = [author.text for author in authors_elements if author.text != '']
print(authors)