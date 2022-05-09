from selenium import webdriver
from selenium.webdriver.common.by import *
from selenium.webdriver.common.keys import Keys
from time import sleep
import time

FAST_URL = 'https://fast.com/'
SPEED_URL = "https://www.speedtest.net/"
BUTTON_XPATH = "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]"
DOWN_XPATH = "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span"
UP_XPATH = "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span"
TWITTER_URL = "https://twitter.com/i/flow/login"
PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "100daysofangela@gmail.com"
TWITTER_PASSWORD = "Wildwest12345!"
EMAIL_LOGIN_XPATH = "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input"
TWITTER_NAME = "Jizz Wayne"
T_NAME_XPATH = "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[2]/label/div/div[2]/div/input"
T_PASS_XPATH = "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input"
TWEET_XPATH = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div"
TWEET_MESSAGE = "Tweeting something for fun"
TWEET_ENTER_XPATH = "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span"

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Firefox()

        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(SPEED_URL)
        sleep(5)
        press = self.driver.find_element(by=By.XPATH, value=BUTTON_XPATH)
        press.click()
        sleep(60)
        self.up2 = float(self.driver.find_element(by=By.XPATH, value=UP_XPATH).text)
        print(self.up)
        self.down2 = float(self.driver.find_element(by=By.XPATH, value=DOWN_XPATH).text)
        print(self.down)
        if self.down2 > self.down or self.up2 < self.up:
            self.tweet_at_provider()

    def tweet_at_provider(self):
        self.driver.get(TWITTER_URL)
        sleep(5)
        email_login = self.driver.find_element(by=By.XPATH, value=EMAIL_LOGIN_XPATH)
        email_login.send_keys(TWITTER_EMAIL)
        email_login.send_keys(Keys.ENTER)

        sleep(2)

        pwd_login = self.driver.find_element(by=By.XPATH, value=T_PASS_XPATH)
        pwd_login.send_keys(TWITTER_PASSWORD)
        pwd_login.send_keys(Keys.ENTER)

        sleep(4)

        tweet_input = self.driver.find_element(by=By.XPATH, value=TWEET_XPATH)
        tweet_input.send_keys("HELLO")
        tweet_input.send_keys(Keys.ENTER)

        sleep(2)

        tweet_button = self.driver.find_element(by=By.XPATH, value=TWEET_ENTER_XPATH)
        tweet_button.click()

        sleep(2)