import requests
from bs4 import BeautifulSoup
import re


def crawl(keyWord):
    input_list = []
    regex = re.compile(r'[\r\n\t]')
    for i in range(1, 11):
        url = "https://www.fonfood.com/s/" + keyWord + "/" + str(i)
        response = requests.get(url)
        soup = BeautifulSoup(response.text , 'html.parser')
        articles = soup.findAll('div' , {'class':'storeListItem '})
        for article in articles:
            meta = article.find('a')
            address = article.find('p').get_text()
            address = regex.sub('', address)
            input_list.append((meta['title'], address))
    return input_list

while True:
	inputStr = input()
	data = crawl(inputStr)
	print(data)
	#title = meta.get_text().strip()
