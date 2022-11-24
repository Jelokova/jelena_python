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
########
# width=driver.get_window_size().get('width')
# height=driver.get_window_size().get('height')
# print(width,height)
# print(driver.get_window_size())
# driver.set_window_size(800,600)
####################
# pos_x = driver.get_window_position().get('x')
# pos_y = driver.get_window_position().get('y')
# print(pos_x,pos_y)
# print(driver.get_window_position())
# driver.set_window_position(0,0)

###########
#print(driver.get_window_rect())

#######
# driver.fullscreen_window()
# time.sleep(5)
# driver.minimize_window()
# time.sleep(5)
# driver.maximize_window()

########
#driver.get_screenshot_as_file('screenshot.png')

####
div=driver.find_element('xpath', '//*[@id="hp"]/div[1]/div[3]/div[1]')
div.screenshot('screenshot.png')
driver.refresh()

