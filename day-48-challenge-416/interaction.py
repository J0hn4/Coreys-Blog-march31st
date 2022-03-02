from selenium import webdriver
from selenium.webdriver.common.by import *
from selenium.webdriver.common.keys import Keys
from time import sleep
WIKI_XPATH = "/html/body/div[3]/div[3]/div[5]/div[1]/div[1]/div/div[3]/a[1]"


driver = webdriver.Firefox()
driver.get("https://en.wikipedia.org/wiki/Main_Page")
# sleep(3)
#
# # articles = driver.find_element(by=By.XPATH, value=WIKI_XPATH)
# # articles.click()
#
# # num_article = articles.text
# #
# # print(num_article)
#
# sleep(3)

# all_portals = driver.find_element(by=By.LINK_TEXT, value="All portals")
# all_portals.click()

search = driver.find_element(by=By.ID, value="searchInput")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

# search_button = driver.find_element(by=By.ID, value="searchButton")
# search_button.click()


sleep(3)

driver.quit()
