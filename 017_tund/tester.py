from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
driver.get('http:www.github.com')
# time.sleep(3)
# driver.close()
# time.sleep(3)
# driver.quit()
user_email = driver.find_element('id', 'user_email')
user_email.send_keys('python@example.com')
user_email.send_keys(Keys.ENTER)

time.sleep(10)
continue_btn = driver.find_element('xpath','/html/body/div[4]/main/div[2]/text-suggester/div[1]/form/div[1]/div[2]/button')
continue_btn.click()
print(user_email)