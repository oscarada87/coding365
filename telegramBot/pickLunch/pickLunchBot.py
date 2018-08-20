import requests
from bs4 import BeautifulSoup
import sys
import time
import telepot
import random
from pprint import pprint
from telepot.loop import MessageLoop
import re

TOKEN = ""
HELP ='''/eat [數字]@pickLunch_bot --- 隨機資料庫中指定數量(預設1家)餐廳
/crawl [關鍵字]@pickLunch_bot --- 關鍵字搜尋並更新資料庫
/help@pickLunch_bot --- 指令列表
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

def eat(data, msg, number = 1):
    chat_id = msg['chat']['id']
    try:
        if len(data[chat_id]) <= 0:
            bot.sendMessage(chat_id, '目前資料庫中沒有餐廳!!')
            return 0
    except BaseException:
        bot.sendMessage(chat_id, '目前資料庫中沒有餐廳!!')
    output = random.sample(data[chat_id], number)
    for i in output:
        restaurant = i[0] + '\n' + i[1] + '\n' + i[2]
        bot.sendMessage(chat_id, restaurant)

data = {}

def handle(msg):
    global data
    pprint(msg)
    typeOfMsg = telepot.flance(msg)[0]
    if typeOfMsg == 'chat':
        query = ''
        chat_id = msg['chat']['id']
        flag =  msg['text'].split('@')[1]
        command = msg['text'].split('@')[0]
        command = command.split(' ')
        message_id = msg['message_id']
        username = '@' + msg['from']['username']
        # print(command[0])
        # print(flag)

    elif typeOfMsg == 'inline_query':
        command = [None]
        flag = 'pickLunch_bot'
        query = msg['query']
        query_id = msg['id']
    else:
        pass

    if flag != 'pickLunch_bot':
        return 0
    else:
        pass

    if command[0] == '/eat':
        length = len(command)
        if length == 1:
            eat(data, msg)
        elif int(command[1]) > 10:
            bot.sendPhoto(chat_id,'https://i.ytimg.com/vi/AWgDNOxroB8/maxresdefault.jpg',reply_to_message_id = message_id)
        else:
            eat(data, msg, int(command[1]))

    elif command[0] == '/crawl':
        try:
            bot.sendMessage(chat_id, '關鍵字: {}...爬蟲中...'.format(command[1]))
            data[chat_id] = crawl(command[1])
            if len(data[chat_id]) == 0:
                bot.sendPhoto(chat_id,'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQGkV4N8ErJIFIrAac1IGcvagr5Du89GsZZwJg25J3js4THChjyjw',reply_to_message_id = message_id)
                bot.sendMessage(chat_id, '你確定{}是可以吃的嗎???'.format(command[1]), reply_to_message_id = message_id)
            else:
                bot.sendMessage(chat_id, '資料更新完成!!')
        except BaseException:
            bot.sendMessage(chat_id, '關鍵字: 北科大...爬蟲中...')
            data = crawl('北科大')
            bot.sendMessage(chat_id, '資料更新完成!!')

    elif command[0] == '/help':
        bot.sendMessage(chat_id, HELP)

    elif query == 'surprise':
        article = [{'type':'article','id':'1','title':'彩蛋','input_message_content':{'message_text':'你找到彩蛋了!'}}]
        print(article)
        bot.answerInlineQuery(query_id, article)

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('I am listening ...')

while 1:
    time.sleep(10)
    bot.getMe()
