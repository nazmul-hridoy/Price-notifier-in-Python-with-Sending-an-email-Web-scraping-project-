import requests
from bs4 import BeautifulSoup
import smtplib
import time

# Using a While loop to make sure that Our code runs all the time (once a day)

while True:
    re = requests.get('https://books.toscrape.com/catalogue/sharp-objects_997/index.html')
    res = re.content

    soup = BeautifulSoup(res, 'html.parser')
    price = float(soup.find('p', class_='price_color').text[1:])

    # Checking if the price is less than 40
    # Use your email and the password (you can generate a password for the app from your Yahoo account)

    if price < 60:
        smt = smtplib.SMTP('smtp.gmail.com', 587)
        # address & port number.Port 587 is often used to encrypt SMTP messages using STARTTLS

        smt.ehlo()
        # greet the server

        smt.starttls()
        # Use your credentials
        smt.login('nazmul.hridoy007@gmail.com', 'tctmwokcpsxmjlrd')
        # First email is the sender's email, the second is the receiver's email
        smt.sendmail('nazmul.hridoy007@gmail.com',
                     'nazmul3224@diu.edu.bd',
                     f"Subject: Books Price Notifier\n\nHi, price has dropped to {price}. Buy it!")
        smt.quit()
    time.sleep(24 * 60 * 60)
