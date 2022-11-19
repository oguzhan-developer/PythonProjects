# -*- coding:utf-8 -*-
import requests
import smtplib
from bs4 import BeautifulSoup
header = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }


def send_mail(body):
    sender = "sender-mail-here"
    receiver = "receiver-mail-here"
    try:
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.ehlo()
        server.starttls()
        server.login(sender,'qyjpwoumupsequix')
        subject = "DOVIZ KURLARI"
        mailContent = f"To:{receiver}\nFrom:{sender}\nSubject:{subject}\n\n{body}"
        server.sendmail(sender, receiver, mailContent)
    except smtplib.SMTPException as e:
        print(e)
    finally:
        server.quit()

r = requests.get("https://www.doviz.com/", headers=header)
content = r.content
soup = BeautifulSoup(content,"html.parser")
currencies = soup.find_all("span",{"class":"name"},limit=5)
rates = soup.find_all("span",{"class":"value"},limit=5)
currencyList = []
rateList = []
y=0
for i in currencies:
    currencyList.append(i.text.replace("İ","I"))
    rateList.append(round(float(rates[y].text.strip().replace(".","").replace(",",".")),2))
    y+=1
body = f"""{currencyList[0]} {rateList[0]} TL
{currencyList[1]} {rateList[1]} TL
{currencyList[2]} {rateList[2]} TL
{currencyList[3]} {rateList[3]} TL
"""

send_mail(body)
    

