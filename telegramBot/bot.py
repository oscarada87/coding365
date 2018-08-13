import sys
import time
import telepot
import random
from pprint import pprint
from telepot.loop import MessageLoop
import requests
from bs4 import BeautifulSoup

TOKEN = ""
games = []
HELP ='''/AABB new --- 新增遊戲
/AABB guess [1234] --- 猜數字
/AABB history --- 歷史紀錄
/AABB answer --- 秘密
/stock [股票代碼] --- 查詢股票現在價格
/help --- 指令列表
備註: 需要設定username才能玩AABB的遊戲'''

class AABB:
    def __init__(self):
        self.name = 'AABB'
        self.answer = self.random_answer()
        self.guessList = []

    def random_answer(self):
        items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        return random.sample(items, 4)
    def get_name(self):
        return self.name
    def get_answer(self):
        answerstr = ''
        for i in self.answer:
            answerstr += str(i)
        return answerstr
    def get_guessList(self):
        return self.guessList
    def check_input(self, inputStr):
        if len(inputStr) == 4:
            for i in range(4):
                for j in range(i+1, 4):
                    if inputStr[i] == inputStr[j]:
                        return False
            return True
        else:
            return False

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
    try:
        chat_id = msg['chat']['id']
        command = msg['text'].split(' ')
        message_id = msg['message_id']
        username = '@' + msg['from']['username']
    except BaseException:
        command = msg['query']
        query_id = msg['id']

    print ('Got command: {}'.format(command))
    # 進行中的遊戲
    if command[0] == '/games':
        for i in games:
            bot.sendMessage(chat_id, i.get_name())
    # AABB訊息
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
                bot.sendMessage(chat_id, '輸入不合法!!!')
                bot.sendMessage(chat_id, username)
                bot.sendMessage(chat_id, '87')
                return 0
            clue = games[0].check(command[2])
            if clue == 'WIN':
                info = username + ' WIN!!!'
                count = len(games[0].get_guessList())
                games.pop()
                bot.sendMessage(chat_id, info)
                bot.sendMessage(chat_id, '大家總共猜了{}次'.format(count))
                if count < 3:
                    bot.sendMessage(chat_id, '媽的你作弊????')
                elif count < 10:
                    bot.sendMessage(chat_id, '勉強合格')
                    bot.sendPhoto(chat_id,'https://images.kocpc.com.tw/kocpc/2017/09/1505037254-e970979c4fe7bbbfcde39041cbf86f2f.png')
                elif count < 15:
                    bot.sendMessage(chat_id, '也太笨了吧')
                    bot.sendPhoto(chat_id, 'https://images.gamme.com.tw/news2/2017/62/28/pJeToKGak56Zqg.jpeg')
                else:
                    bot.sendMessage(chat_id, '經本BOT測定智商為-87')
                    bot.sendPhoto(chat_id, 'https://img.tw.observer/images/nj27AHS.jpg')

            else:
                info = clue
                bot.sendMessage(chat_id, info, reply_to_message_id = message_id)

        elif command[1] == 'answer':
            bot.sendPhoto(chat_id, 'https://i.imgur.com/Vedlve0.jpg')

        elif command[1] == 'history':
            for i in games[0].get_guessList():
                bot.sendMessage(chat_id, str(i[0]) + ' : ' + str(i[1]))
    # inline query
    elif command == 'answer':
        article = [{'type':'article','id':'1','title':games[0].get_answer(),'input_message_content':{'message_text':'TOP SECRET!!'}}]
        print(article)
        bot.answerInlineQuery(query_id, article)
    # 股票訊息
    elif command[0] == '/stock':
        stockData = stock_crawl(command[1])
        bot.sendMessage(chat_id, stockData[0])
        bot.sendMessage(chat_id, '價格: ' + stockData[1])
    # 幫助訊息
    elif command[0] == '/help':
        bot.sendMessage(chat_id, HELP)

bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('I am listening ...')

while 1:
    time.sleep(10)
    bot.getMe()
