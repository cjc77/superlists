import time
from selenium import webdriver

browser = webdriver.Chrome('/Users/carsoncook/Downloads/chromedriver')
browser.get('http://localhost:8000')

assert 'Django' in browser.title
