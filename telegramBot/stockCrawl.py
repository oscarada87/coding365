import requests
from bs4 import BeautifulSoup

while True:
    stock = input()
    url = 'https://finance.yahoo.com/quote/'+ stock +'.TW/'
    res = requests.get(url)
    soap = BeautifulSoup(res.text,'html.parser')
    price = soap.find(class_='Trsdu(0.3s)')
    name = soap.select("h1[data-reactid='7']")[0].get_text()
    print(price)
    print(name)
    print(price.get_text())
