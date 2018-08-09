import requests
from bs4 import BeautifulSoup

while True:
    stock = input()
    url = 'https://finance.yahoo.com/quote/'+ stock +'.TW/'
    res = requests.get(url)
    soap = BeautifulSoup(res.text,'html.parser')
    price = soap.find(class_="Trsdu(0.3s)")
    print(price.get_text())
