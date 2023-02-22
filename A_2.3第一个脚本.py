import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://web-dev.gemoo.com/')
driver.maximize_window()
time.sleep(3)
driver.quit()
