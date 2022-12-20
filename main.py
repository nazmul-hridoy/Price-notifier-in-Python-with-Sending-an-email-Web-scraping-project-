import requests
from bs4 import BeautifulSoup
import smtplib
import time

# Using a While loop to make sure that Our code runs all the time (once a day)

while True:
    re = requests.get('https://books.toscrape.com/catalogue/sharp-objects_997/index.html')
    res = re.content

    soup = BeautifulSoup(res, 'html.parser')
    price = float(soup.find('p', class_='price_color').text[1:])    # float is using here to set price value as a floating number.

    # Checking if the price is less than 60
    # Use your email and the password (you can generate a password for the app from your gmail account)

    if price < 60:
        smt = smtplib.SMTP('smtp.gmail.com', 587)
        # address & port number.Port 587 is often used to encrypt SMTP messages using STARTTLS

        smt.ehlo()
        # greet the server

        smt.starttls()
        # Use your credentials
        # STARTTLS notifies a mail server that the contents of an email need to be encrypted
        smt.login('YourEmail@gmail.com', 'YourPassword')
        
       
        smt.sendmail('SenderEmail@gmail.com',
                     'ReceiverEmail@gmail.com',
                     f"Subject: Books Price Notifier\n\nHi, price has dropped to {price}. Buy it!")
         # First email is the sender's email aka YourEmail@gmail.com, the second is the receiver's email
        smt.quit()
    time.sleep(24 * 60 * 60) # It'll check the price one time in each day
