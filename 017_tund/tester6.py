import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options=webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.maximize_window()
url='https://www.youtube.com/c/visitestoniaofficial/videos'
driver.get(url)
agree_btn=driver.find_element('xpath', '//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[2]/div/div/button')
agree_btn.click()
video = driver.find_elements('class name','style-scope ytd-rich-item-renderer')
for vid in video:
    title=vid.find_element('xpath','.//*[@id="video-title"]').text
    duration=vid.find_element('xpatch','//*[@id="text"]')
    print(title)
    print(duration)
print(len(video))