import abc
import sys
import time
import telepot
import random
from pprint import pprint
from telepot.loop import MessageLoop

TOKEN = "695612325:AAGMtTb2_3LBB2Gr8JlJwwp3QHT1erjkyPY"
HELP = ""
games = []

#
class Player:
    def __init__(self, username):
        self.data = ()
        self.username = username
    def getUsername(self):
        return self.username
    def getData(self):
        return self.data
    def setData(self, data):
        self.data = data

class Game:
    def __init__(self):
        self.member = []
        self.nowPlayer = 0
        self.time = 0

    def nextPlayer(self):
        self.nowPlayer += 1
        length = len(self.member) - 1
        if self.nowPlayer > length:
            self.nowPlayer = 0

    def getMember(self):
        return self.member

    def Join(self,player):
        self.member.append(player)

    @abc.abstractmethod
    def StartGame():
        return Notimplemented

class DiceGame(Game):
    def __init__(self):
        self.nowGuessDice = []  #點數,個數
        super(DiceGame, self).__init__()
    def getNowGuessDice(self):
        return self.nowGuessDice
    def setNowGuessDice(self, dice):
        self.nowGuessDice = dice
    def Start(self):
        for x in self.member:
            data_temp=[]
            for _ in range(6):
                data_temp.append(random.randint(1, 6))
            data_temp.sort()
            x.setData(tuple(data_temp))

    def check_valid_input(self, dice, chat_id, message_id):
        nowDice = self.nowGuessDice
        if dice[0] > 6 or dice[1] > 6 or dice[0] < 1 or dice[1] < 1:
            bot.sendMessage(chat_id, '骰子點數或個數不合法', reply_to_message_id = message_id)
            return 2    #Error code 2: 骰子點數或個數不合法
        elif dice[0] == nowDice[0] and dice[1] == nowDice[1]:
            bot.sendMessage(chat_id, '喊的點數個數與上一人相同', reply_to_message_id = message_id)
            return 3    #Error code 3: 喊的點數個數與上一人相同
        elif dice[0] < nowDice[0]:
            bot.sendMessage(chat_id, '喊的骰子點數比上一人小', reply_to_message_id = message_id)
            return 4    #Error code 4: 喊的骰子點數比上一人小
        elif dice[1] < nowDice[1]:
            bot.sendMessage(chat_id, '喊的骰子個數比上一人小', reply_to_message_id = message_id)
            return 5    #Error code 5: 喊的骰子個數比上一人小
        else:
            return 1

    def check_win(self, message_id, chat_id):
        player = self.member[self.nowPlayer]
        username = player.getUsername()
        count = player.getData().count(self.nowGuessDice[0])
        if count < self.nowGuessDice[1]:
            bot.sendMessage(chat_id, '獲勝!!', reply_to_message_id = message_id)
            bot.sendMessage(chat_id, username + '被抓到!')
            return 2    #抓到 Player win
        else:
            bot.sendMessage(chat_id, '抓錯!!', reply_to_message_id = message_id)
            bot.sendMessage(chat_id, username + '很誠實!')
            return 1    #抓錯 Player lose


#

def handle(msg):
    global games
    pprint(msg)
    try:
        chat_id = msg['chat']['id']
        flag =  msg['text'].split('@')[1]
        command = msg['text'].split('@')[0]
        command = command.split(' ')
        message_id = msg['message_id']
        username = '@' + msg['from']['username']
    except BaseException:
        command = msg['query']
        query_id = msg['id']
        username = '@' + msg['from']['username']

    print ('Got command: {}'.format(command))

    # Inline query
    if command == 'mydice':
        print('test')
        for i in games[0].getMember():
            print(i.getUsername())
            if username == i.getUsername():
                dice = i.getData()
                print('test')
                article = [{'type':'article','id':'1','title':str(dice),'input_message_content':{'message_text':'TOP SECRET!!'}}]
                print(article)
                bot.answerInlineQuery(query_id, article)
                break

    # if flag != 'NTUTgames_bot':
    #     return 0

    if command[0] == '/new':
        games.append(DiceGame())
        bot.sendMessage(chat_id, '新的吹牛遊戲建立!!')
    elif command[0] == '/join':
        tempPlayer = Player(username)
        games[0].Join(tempPlayer)
        bot.sendMessage(chat_id, username + '成功加入遊戲!', reply_to_message_id = message_id)
    elif command[0] == '/start':
        games[0].Start()
        bot.sendMessage(chat_id, '開始吹牛遊戲!')
    elif command[0] == '/喊':
        dice = [int(command[1][0]), int(command[1][1])]
        if games[0].check_valid_input(dice, chat_id, message_id) == 1:
            games[0].setNowGuessDice(dice)
    elif command[0] == '/抓':
        games[0].check_win(self, message_id, chat_id)
        games.pop()


bot = telepot.Bot(TOKEN)
MessageLoop(bot, handle).run_as_thread()
print ('I am listening ...')

while 1:
    time.sleep(10)
    bot.getMe()
