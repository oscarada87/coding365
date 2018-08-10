import requests
from bs4 import BeautifulSoup
import sys
import time
import telepot
import random
from pprint import pprint
from telepot.loop import MessageLoop
import re

TOKEN = "621337650:AAGKDefEVqbk0WMiIaWCfgJ4-GAO3iev4xA"
HELP ='''/eat @pickLunch_bot --- 隨機資料庫中一家餐廳
/crawl [關鍵字] @pickLunch_bot --- 關鍵字搜尋並更新資料庫
/top10 @pickLunch_bot --- 列出資料庫前10筆資料
/help @pickLunch_bot --- 指令列表
'''
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
            input_list.append((meta['title'], address ,meta['href']))
    return input_list

def top10(data, msg):
    chat_id = msg['chat']['id']
    for i in range(10):
        restaurant = data[i][0] + '\n' + data[i][1] + '\n' + data[i][2]
        bot.sendMessage(chat_id, restaurant)

data = []

def handle(msg):
    pprint(msg)
    global data
    try:
        chat_id = msg['chat']['id']
        flag =  msg['text'].split('@')[1]
        command = msg['text'].split('@')[0]
        command = command.split(' ')
        message_id = msg['message_id']
        username = '@' + msg['from']['username']
    except BaseException:
        pass
    if flag != 'pickLunch_bot':
        return 0
    else:
        pass
    if command[0] == '/eat':
        randNum = random.randint(0,len(data))
        restaurant = data[randNum][0] + '\n' + data[randNum][1] + '\n' + data[randNum][2]
        bot.sendMessage(chat_id, restaurant)
    elif command[0] == '/crawl':
        try:
            bot.sendMessage(chat_id, '關鍵字: {}...爬蟲中...'.format(command[1]))
            data = crawl(command[1])
            if len(data) == 0:
                bot.sendPhoto(chat_id,'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQGkV4N8ErJIFIrAac1IGcvagr5Du89GsZZwJg25J3js4THChjyjw',reply_to_message_id = message_id)
                bot.sendMessage(chat_id, '你確定{}是可以吃的嗎???'.format(command[1]), reply_to_message_id = message_id)
            else:
                bot.sendMessage(chat_id, '資料更新完成!!')
        except BaseException:
            bot.sendMessage(chat_id, '關鍵字: 北科大...爬蟲中...')
            data = crawl('北科大')
            bot.sendMessage(chat_id, '資料更新完成!!')

    elif command[0] == '/top10':
        top10(data, msg)

    elif command[0] == '/help':
        bot.sendMessage(chat_id, HELP)

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('I am listening ...')

while 1:
    time.sleep(10)
    bot.getMe()
