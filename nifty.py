import smtplib
import time
import requests
from bs4 import BeautifulSoup


url = "https://www.moneycontrol.com/"

headers = {
    "user-agent": 'enter your user agent(you can get it from google)'


}


def check():
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = "MARKET ACTION NIFTY 50"
    price = soup.find(id="cp").get_text()

    cp = price.replace(",", "")
    print(title.strip())
    print(cp)
    if float(cp) > 9000:
        send_mail(cp)


def send_mail(cp):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('sender mail id', 'sender login essential')

    subject = "Nifty 50 Price Updated"
    body = f"check the link https://www.moneycontrol.com/ \nCurrent Price:{cp}"
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'sender mail id',
        'reciver mail id',
        msg
    )
    print("mail sent!!")
    server.quit()


while True:
    check()
    time.sleep(100)
