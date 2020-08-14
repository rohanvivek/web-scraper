import requests
from bs4 import BeautifulSoup
import smtplib
import time

url = "https://www.moneycontrol.com/"


def lambda_handler(event, context):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = "MARKET ACTION NIFTY 50"
    price = soup.find(id="cp").get_text()

    cp = price.replace(",", "")
    print(title.strip())
    print(cp)
    if float(cp) < 12000:
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('netflixfreekahai@gmail.com', 'ulyxjyxzosmdtmsi')

    subject = "Nifty 50 Price Updated"
    body = 'check the link https://www.moneycontrol.com/'
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'netflixfreekahai@gmail.com',
        'rohanvivek.singh@gmail.com',
        msg
    )
    print("mail sent!!")
    server.quit()



