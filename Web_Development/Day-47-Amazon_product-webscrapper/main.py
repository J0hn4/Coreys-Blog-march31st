import requests
from bs4 import BeautifulSoup
from datetime import datetime
import smtplib
from time import time, sleep

USER_AGENT = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0"
ACCEPT_LANGUAGE = "en-US,en;q=0.5"
URL ="https://www.amazon.com/DEWALT-DCK1020D2-20V-Combo-Kit/dp/B0773CS85H/ref=sr_1_3?crid=US4YA6MMA23Y&keywords=tools&qid=1645962119&sprefix=to%2Caps%2C381&sr=8-3"

headers = {
    "User-Agent": USER_AGENT,
    "Accept-Language": ACCEPT_LANGUAGE,

}


def get_price_alert():
    response = requests.get(URL, headers=headers)
    amazon_pot_page = response.text
    soup = BeautifulSoup(amazon_pot_page, "html.parser")
    price_info = soup.find(name="span", class_="a-offscreen")
    price = price_info.string
    price_float = float(price[1:])
    if price_float < 700.00:
        port_number = 587
        goog_my_email = "100daysofangela@gmail.com"
        goog_password = "100Daysmoreofstudy#1"
        goog_smtp = "smtp.gmail.com"
        yahoo_my_email = "luangelu@yahoo.com"
        yahoo_password_original = "Angela100#4124"
        yahoo_password_new = "rzjjvorijmqbhedn"
        yahoo_smtp = "smtp.mail.yahoo.com"

        with smtplib.SMTP(yahoo_smtp, 587) as connection:
            connection.starttls()
            connection.login(user=yahoo_my_email, password=yahoo_password_new)
            connection.sendmail(
                from_addr=yahoo_my_email,
                to_addrs=goog_my_email,
                msg=f"Subject: Tool Price Alert \n\n The current price for the tool set is ${price_float}. Go to {URL} to view it. "
            )
        print("Email being sent. Price alert communicated.")

now = datetime.now()
hour = now.hour
minute = now.minute

if hour == 19 and minute == 00:
    get_price_alert()
    sleep(61)
