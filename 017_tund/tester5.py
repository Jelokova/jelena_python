import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
url='http://www.gammatest.net'
driver.get(url)

gamma=driver.current_window_handle
print(driver.window_handles)
driver.switch_to.new_window('tab')
driver.get('http://www.github.com')
#driver.switch_to.window(gamma)
driver.switch_to.new_window('tab')
driver.get('http://www.google.com')

