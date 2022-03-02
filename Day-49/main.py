from selenium import webdriver
from selenium.webdriver.common.by import *
from selenium.webdriver.common.keys import Keys
from time import sleep
import time
SIGN_IN_XPATH = "/html/body/div[1]/header/nav/div/a[2]"
URL="https://www.linkedin.com/jobs/search/?f_AL=true&f_E=1%2C2&f_JT=F%2CC%2CT%2CI&geoId=103644278&keywords=python%20developer&location=united%20states"
LINK_IN_EMAIL = "100daysofangela@gmail.com"
LINK_IN_PASS = "Wildwest12345!"


driver = webdriver.Firefox()
driver.get(URL)
sleep(3)

search = driver.find_element(by=By.XPATH, value=SIGN_IN_XPATH)
search.click()

email_input = driver.find_element(by=By.ID, value="username")
email_input.send_keys(LINK_IN_EMAIL)
email_input.send_keys(Keys.ENTER)

pwd = driver.find_element(by=By.ID, value="password")
pwd.send_keys(LINK_IN_PASS)
pwd.send_keys(Keys.ENTER)

sign_in_button = driver.find_element(by=By.XPATH, value="/html/body/div/main/div[2]/div[1]/form/div[3]/button")
sign_in_button.click()





