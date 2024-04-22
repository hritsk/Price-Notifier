import requests
from bs4 import BeautifulSoup
import smtplib
import time
while True:
    re = requests.get ('https://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html')
    res = re.content
    soup = BeautifulSoup(res,'html.parser')
    print(soup.prettify())
    price= float(soup.find('p',class_='price_color').text[1:5])

    if price<60:
       smt = smtplib.SMTP('smtp.gmail.com',587)
       smt.ehlo()
       smt.starttls()
       smt.login('hritiksingh2902@gmail.com','eqpnrptxireinnhq')
       smt.sendmail('hritiksingh2902@gmail.com','hritiksingh.23k@gmail.com',f"Subject:Headphone Price Notifier\n\n Hii, Price has droped to {price}.Buy it!")
       smt.quit()
    time.sleep(24*60*60)