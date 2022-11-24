from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
# driver.get('http:www.github.com')
# print(driver.title)
# print(driver.page_source)

driver.get('http:www.gammatest.net')
#link=driver.find_element('link text', 'Rohkem infot')
# link=driver.find_elements('partial link text', 'Rohkem')
# link.click()
link=driver.find_elements('partial link text', 'Rohkem')
for x in link:
    print(x.get_attribute('href'))