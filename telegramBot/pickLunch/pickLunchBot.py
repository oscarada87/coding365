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
HELP ='''/eat --- 隨機北科大附近的一家餐廳'''
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

data = crawl('北科大')

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
        bot.sendMessage(chat_id, data[randNum][0])
        bot.sendMessage(chat_id, data[randNum][1])
    elif command[0] == '/crawl':
        try:
            bot.sendMessage(chat_id, '關鍵字: {}...爬蟲中...'.format(command[1]))
            data = crawl(command[1])
        except BaseException:
            bot.sendMessage(chat_id, '關鍵字: 北科大...爬蟲中...')
            data = crawl('北科大')
        finally:
            bot.sendMessage(chat_id, '資料更新完成!!')

    elif command[0] == '/help@pickLunch_bot':
        bot.sendMessage(chat_id, HELP)

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('I am listening ...')

while 1:
    time.sleep(10)
    bot.getMe()
