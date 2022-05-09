from internet_speed_twitter_bot import InternetSpeedTwitterBot
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import *
from selenium.webdriver.common.keys import Keys
from time import sleep
import time



bot = InternetSpeedTwitterBot()


get_speed = bot.get_internet_speed()
# tweet = bot.tweet_at_provider()
