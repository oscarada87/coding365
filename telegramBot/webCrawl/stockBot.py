import sys
import time
import telepot
import random
import csv
from telepot.loop import MessageLoop
from bs4 import BeautifulSoup
import requests
from pprint import pprint


TOKEN = "608004759:AAFQmPaMT34Dp9KLjrJpXW_dcmJvR62qXUw"
HELP ='''/help@NTUTstock_bot --- 指令列表
/find [股價代碼 或 股價名字] @NTUTstock_bot --- 查詢股票資訊
'''

dataTrans=[]             #文字轉代碼列表
files=open(r'stocklist.csv','r',encoding='UTF-8')
for i in files :
    i = i.split(',')
    i.pop()
    dataTrans.append(i)
print('讀取完成!')

def NametransCode(dataTrans,inpu) :   #輸入中文轉代碼的函式
    for i in dataTrans :
        if inpu == i[1] :
            stock = i[0]
    return stock

def getName(data, stock):
    url = 'https://tw.stock.yahoo.com/q/q?s='+ stock
    res = requests.get(url)
    soup = BeautifulSoup(res.text,'html.parser')
    companyName = soup.find(href="/q/bc?s=" + stock)
    if companyName is None :
        print("None")
        return 2
    else :
        data.append("股票代碼: %s" % companyName.get_text())
        return 1

def getInfo(data, stock):
    url = 'https://tw.stock.yahoo.com/q/q?s='+ stock
    url2 = 'https://finance.yahoo.com/quote/'+ stock +'.TW' #取得當前時間
    res2 = requests.get(url2)
    soup2 = BeautifulSoup(res2.text,'html.parser')

    time = soup2.find(id="quote-market-notice")
    data.append(time.get_text())
    price = soup2.find(class_="Trsdu(0.3s)")                #取得股價
    data.append("當前股價: %s" % price.get_text())

    url3 = 'https://www.wantgoo.com/stock/' + stock         #取得漲跌幅
    response3 = requests.get(url3)
    soup3 = BeautifulSoup (response3.text, 'html.parser')
    change = soup3.find_all('span',{'class':'chg'})
    for i in change :
        data.append('漲跌幅: %s' %i.get_text())

    data.append('更多訊息: %s' % url)                        #給予參考連結

def mergeInfo(data):
    infoStr = ''
    for i in data :
        infoStr = infoStr + str(i) + '\n'
    return infoStr

def handle(msg):
    data = []
    pprint(msg)
    try:
        chat_id = msg['chat']['id']
        flag =  msg['text'].split('@')[1]
        command = msg['text'].split('@')[0]
        command = command.split(' ')
        message_id = msg['message_id']
        username = '@' + msg['from']['username']
    except BaseException:
        pass
    if flag != 'NTUTstock_bot':
        return 0
    if command[0] == '/find':
        inpu = command[1]
        if inpu.isdigit():   #輸入數字
            stock = inpu
        else :               #輸入文字
            stock = NametransCode(dataTrans,inpu)
        if getName(data, stock) == 1:
            getInfo(data, stock)
            bot.sendMessage(chat_id, mergeInfo(data), reply_to_message_id = message_id)
        else:
            bot.sendMessage(chat_id, '查無此股!', reply_to_message_id = message_id)
    elif command[0] =='/help':
        bot.sendMessage(chat_id, HELP)

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('I am listening ...')

while 1:
    time.sleep(10)
    bot.getMe()
