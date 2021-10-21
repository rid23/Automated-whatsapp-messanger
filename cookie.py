from selenium import webdriver
from time import sleep
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:/Users/riddhi/AppData/Local/Google/Chrome/for_rid')

driver = webdriver.Chrome('chromedriver.exe',options = options)

driver.get('https://web.whatsapp.com/')
