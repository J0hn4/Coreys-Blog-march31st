from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
PY_XPATH = "/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul"


driver = webdriver.Firefox()
driver.get("https://www.python.org/")
sleep(3)


upcoming_events = driver.find_element(by=By.XPATH, value=PY_XPATH)
upcoming_hr = upcoming_events.text

# print(upcoming_hr)

chunks = upcoming_hr.split('\n')

# print(chunks)

dates = chunks[::2]
name = chunks[1::2]

events = {}

# print(dates)
# print(name)

# upcoming_dictionary = {'dates':dates[i],'name':name[i] for i in range(len(dates))}
for n in range(len(dates)):
    events[n] = {
        "dates": dates[n],
        "name": name[n]
    }

print(events[3])

driver.quit()





