from selenium import webdriver
from selenium.webdriver.common.by import *
from selenium.webdriver.common.keys import Keys
from time import sleep
import time

URL="https://tinder.com/app/recs"
DISLIKE_XPATH = '//*[@id="s1502865376"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[2]/button/span/span'
LOGIN_XPATH = "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a"
PH_LOGIN_XPATH = "/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[3]/button/span[2]"
COUNTRY_XPATH = "/html/body/div[2]/div/div/div[1]/div[2]/div/div[1]/span[2]"
C_INPUT_XPATH = "/html/body/div[2]/div/div/div[1]/div[2]/div[1]/div/input"

driver = webdriver.Firefox()
driver.get(URL)
sleep(3)

login = driver.find_element(by=By.XPATH, value=LOGIN_XPATH)
login.click()

sleep(2)

phone_login = driver.find_element(by=By.XPATH, value=PH_LOGIN_XPATH)
phone_login.click()

sleep(10)

country = driver.find_element(by=By.XPATH, value= COUNTRY_XPATH)
country.click()

c_input = driver.find_element(by=By.XPATH, value= C_INPUT_XPATH)
c_input.send_keys("Thailand")

sleep(2)
c_select = driver.find_element(by=By.XPATH, value= "/html/body/div[2]/div/div/div[1]/div[2]/div[2]/div/div")
c_select.click()

ph_input = driver.find_element(by=By.XPATH, value= "/html/body/div[2]/div/div/div[1]/div[2]/div/input")
c_input.send_keys("0987909189")


# /html/body/div[2]/div/div/div[1]/div[2]/div/input

# email_input = driver.find_element(by=By.ID, value="username")
# email_input.send_keys(LINK_IN_EMAIL)
# email_input.send_keys(Keys.ENTER)
#
# pwd = driver.find_element(by=By.ID, value="password")
# pwd.send_keys(LINK_IN_PASS)
# pwd.send_keys(Keys.ENTER)
#
#





