import requests
from bs4 import BeautifulSoup
from selenium import webdriver
list_url = []
list_title = []
driver = webdriver.Chrome(r"chromedriver.exe")
driver.get("https://www.fonfood.com/")#以瀏覽器去搜尋網址
driver.find_element_by_id("keyword").send_keys("北科大")#去輸入欄位自動輸入Selenium
driver.find_element_by_xpath('//*[@title="搜尋"]').click()#查看搜尋結果
now_url = driver.current_url
html = requests.get(now_url)
soup = BeautifulSoup(html.text,'html.parser')
article = soup.findAll('div','titleBlock')
for articles in article :
    meta = articles.find('a')
    list_title.append(meta['title'])
    list_url.append(meta['href'])
driver.quit()#關閉瀏覽器

print(list_title)
