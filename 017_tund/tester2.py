from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)
driver.get('http:www.github.com')

def wait_for_element_located(timeout, selector, select_value):
    try:
        element=WebDriverWait(driver,timeout).until(
            EC.presence_of_element_located((selector,select_value))
        )
        print(element.text)
    except:
        print('Error')
        driver.quit()
wait_for_element_located(10, By.XPATH,'/html/body/div[4]/main/div[1]/div[2]/div/div/div[2]/h1')


