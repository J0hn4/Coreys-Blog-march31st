from selenium import webdriver
from selenium.webdriver.common.by import *
from selenium.webdriver.common.keys import Keys
from time import sleep
import time
COOKIE_XPATH = '//*[@id="cookie"]'
URL = "http://orteil.dashnet.org/experiments/cookie/"

driver = webdriver.Firefox()
driver.get(URL)

sleep(3)

def click_cookie():
    end = time.time() + 5
    cookie = driver.find_element(by=By.XPATH, value=COOKIE_XPATH)
    while time.time() < end:
        cookie.click()

def check_purchase():
    try:
        driver.find_element(by=By.CSS_SELECTOR, value='#buyPortal.grayed')
    except NoSuchElementException:
        element = driver.find_element(by=By.ID, value='buyPortal')
        element.click()
        return

    # We have to use XPATH here because of the space in 'buyAlchemy lab'
    # We cannot use driver.find_element(by=By.CSS_SELECTOR, value='#buyAlchemy lab.grayed')
    try:
        driver.find_element(by=By.XPATH, value='//div[@id="buyAlchemy lab" and @class="grayed"]')
    except NoSuchElementException:
        element = driver.find_element(by=By.ID, value='buyAlchemy lab')
        try:
            amount = element.find_element(by=By.CLASS_NAME, value="amount").text
        except NoSuchElementException:
            amount = "0"
        if int(amount) < 5:
            element.click()
        return

    def find_element(tag_id):
        try:
            driver.find_element(by=By.CSS_SELECTOR, value=f'#{tag_id}.grayed')
            return False
        except:
            element = driver.find_element(by=By.ID, value=f'{tag_id}')
            try:
                amount = element.find_element(by=By.CLASS_NAME, value="amount").text
            except:
                amount = "0"
            if int(amount) < 5:
                element.click()
            return True

    if find_element('buyShipment'):
        return
    if find_element('buyMine'):
        return
    if find_element('buyFactory'):
        return
    if find_element('buyGrandma'):
        return
    if find_element('buyCursor'):
        return

countdown = 5 * 60
start = time.time()

sleep(2)
time_passed = int(time.time() - start)
print(time_passed)

while time_passed < countdown:
    check_purchase()
    click_cookie()
    time_passed = int(time.time() - start)
    print(time_passed)


cps = driver.find_element(by=By.XPATH, value='//*[@id="cps"]')
final_cps = cps.text
print(final_cps)

sleep(5)
driver.quit()




#     if driver.find_element(by=By.ID, value='//div[@id=="buyPortal" and @class!=="grayed"]'):
#         buy_portal = driver.find_element(by=By.ID, value="buyPortal")
#         buy_portal.click()
#     elif driver.find_element(by=By.XPATH, value='//div[@id="buyAlchemy lab" and @class!="grayed"]'):
#         buy_portal = driver.find_element(by=By.ID, value="buyAlchemy lab")
#         buy_portal.click()
#     elif driver.find_element(by=By.XPATH, value='//div[@id="buyShipment" and @class!="grayed"]'):
#         buy_portal = driver.find_element(by=By.ID, value="buyShipment")
#         buy_portal.click()
#     elif driver.find_element(by=By.XPATH, value='//div[@id="buyMine" and @class!="grayed"]'):
#         buy_portal = driver.find_element(by=By.ID, value="buyMine")
#         buy_portal.click()
#     elif driver.find_element(by=By.XPATH, value='//div[@id="buyFarm" and @class!="grayed"]'):
#         buy_portal = driver.find_element(by=By.ID, value="buyFarm")
#         buy_portal.click()
#     elif driver.find_element(by=By.XPATH, value='//div[@id="buyGrandma" and @class!="grayed"]'):
#         buy_portal = driver.find_element(by=By.ID, value="buyGrandma")
#         buy_portal.click()
#     elif driver.find_element(by=By.XPATH, value='//div[@id="buyCursor" and @class!="grayed"]'):
#         buy_portal = driver.find_element(by=By.ID, value="buyCursor")
#         buy_portal.click()
#
# while time_passed < countdown:
#     if time_passed % 5 == 0:
#         # print("Check purchase")
#         check_purchase()
#         time_passed = int(time.time() - start)
#     else:
#         click_cookie()
#         # print(time_passed)
#         time_passed = int(time.time() - start)
# # final_cookie_speed = cookie = driver.find_element(by=By.XPATH, value=)






# def check_purchase():
#     def find_element(tag_id):
#         try:
#             driver.find_element(by=By.CSS_SELECTOR, value=f'#{tag_id}.grayed')
#             return False
#         except NoSuchElementException:
#             element = driver.find_element(by=By.ID, value=f'{tag_id}')
#             try:
#                 amount = element.find_element(by=By.CLASS_NAME, value="amount").text
#             except NoSuchElementException:
#                 amount = "0"
#             if int(amount) < 5:
#                 element.click()
#             return True
#
#     if find_element('buyShipment'):
#         return
#
#     if find_element('buyMine'):
#         return
#
# #     if find_element('buyFactory'):
# #         return
# #
# #     if find_element('buyGrandma'):
# #         return
#
#     if find_element('buyCursor'):
#         return
