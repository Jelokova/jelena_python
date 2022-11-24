from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
url='https://www.saucedemo.com'
driver.get(url)
driver.maximize_window()

user_name=driver.find_element('id', 'user-name')
user_name.send_keys('standard_user')
user_name.send_keys(Keys.ENTER)
time.sleep(3)


user_password=driver.find_element('id', 'password')
user_password.send_keys('secret_sauce')
user_password.send_keys(Keys.ENTER)
time.sleep(3)

login_btn=driver.find_element('id', 'login-button')
login_btn.click()
time.sleep(3)

#Sort option
sort_itemes = driver.find_element ('xpath','//*[@id="header_container"]/div[2]/div[2]/span/select').click()
sort_itemes.set_attribute('value')

product1=driver.find_element('id','add-to-cart-sauce-labs-backpack')
product1.click()
time.sleep(3)
product2=driver.find_element('id','add-to-cart-test.allthethings()-t-shirt-(red)')
product2.click()
time.sleep(3)

basket_link=driver.find_element('id','shopping_cart_container')
basket_link.click()
time.sleep(3)

banner1= driver.find_element('xpath', '//*[@id="cart_contents_container"]/div/div[1]/div[3]')
banner1.screenshot('banner1.png')
banner2= driver.find_element('xpath', '//*[@id="cart_contents_container"]/div/div[1]/div[4]')
banner2.screenshot('banner2.png')
time.sleep(3)

checkout=driver.find_element('id','checkout')
checkout.click()
time.sleep(3)

first_n=driver.find_element('id','first-name')
first_n.send_keys('Jelena')
first_n.send_keys(Keys.TAB)
time.sleep(3)

last_n=driver.find_element('id','last-name')
last_n.send_keys('Jel')
last_n.send_keys(Keys.TAB)
time.sleep(3)

zip=driver.find_element('id','postal-code')
zip.send_keys('74001')
zip.send_keys(Keys.TAB)
time.sleep(3)

menu=driver.find_element('id','react-burger-menu-btn')
menu.click()
time.sleep(3)
log_out=driver.find_element('id','logout_sidebar_link')
log_out.click()

