import sys
import time
import telepot
import random
from pprint import pprint
from telepot.loop import MessageLoop
import requests
from bs4 import BeautifulSoup

TOKEN = "619435504:AAHK1B8KlY8ef-bsuvy8_35c9EBQnEP_Ijw"
games = []

class AABB:
    def __init__(self):
        self.name = 'AABB'
        self.answer = self.random_answer()
        self.guessList = []

    def random_answer(self):
        items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        return random.sample(items, 4)

    def get_answer(self):
        return self.answer

    def check_input(self, inputStr):
        for i in range(4):
            for j in range(i+1, 4):
                if inputStr[i] == inputStr[j]:
                    return False
        return True

    def check(self, inputStr):
        guess = []
        for i in inputStr:
            guess.append(int(i))
        a = 0
        b = 0
        for i in range(4):
            for j in range(4):
                if self.answer[i] == guess[j]:
                    if i == j:
                        a += 1
                    else:
                        b += 1
                else:
                    pass
        if a == 4:
            return 'WIN'
        clue = str(a) + ' A ' + str(b) + ' B'
        self.guessList.append((inputStr,clue))
        return clue

def stock_crawl(stock):
    url = 'https://finance.yahoo.com/quote/'+ stock +'.TW/'
    res = requests.get(url)
    soap = BeautifulSoup(res.text,'html.parser')
    price = soap.find(class_='Trsdu(0.3s)').get_text()
    name = soap.select("h1[data-reactid='7']")[0].get_text()
    data = [name, price]
    return data

def handle(msg):
    pprint(msg)
    chat_id = msg['chat']['id']
    command = msg['text'].split(' ')
    username = '@' + msg['from']['username']

    print ('Got command: {}'.format(command))

    if command[0] == '/games':
        for i in games:
            bot.sendMessage(chat_id, i.getName())
    elif command[0] == '/AABB':
        if command[1] == 'new':
            if len(games) >= 1:
                bot.sendMessage(chat_id, '遊戲已經在進行了!')
            else:
                games.append(AABB())
                bot.sendMessage(chat_id, 'AABB新遊戲創立!')
        elif command[1] == 'guess':
            if games[0].check_input(command[2]):
                pass
            else:
                bot.sendMessage(chat_id, '不能輸入重複的')
                bot.sendMessage(chat_id, username)
                bot.sendMessage(chat_id, '87')
                return 0
            clue = games[0].check(command[2])
            if clue == 'WIN':
                info = username + ' WIN!!!'
                games.pop()
            else:
                info = clue
            bot.sendMessage(chat_id, info)
        elif command[1] == 'answer':
            bot.sendMessage(chat_id, '你想幹嘛????')
    elif command[0] == '/stock':
        stockData = stock_crawl(command[1])
        bot.sendMessage(chat_id, stockData[0])
        bot.sendMessage(chat_id, '價格: ' + stockData[1])

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('I am listening ...')

while 1:
    time.sleep(10)
    
    bot.getMe()
