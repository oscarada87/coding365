import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from random import choice
import json
import random
import time
import pprint

#自行更新  #自行更新   #自行更新
TOKEN =""             #自行更新#自行更新
#自行更新  #自行更新   #自行更新

bot = telepot.Bot(TOKEN)

def print_msg(msg):
    print(json.dumps(msg, indent=4))

# 接收chat後執行：
def on_chat(msg):
    header = telepot.glance(msg, flavor="chat")
    print_msg(msg)
    #data=""
    if header[0] == "text":
        text = msg["text"]
        username = msg["from"]["username"]
    if text.startswith("/"):
        command = text.lstrip("/")
        print(command)
        if command == "Hello" or command == "您好" or command == "你好" or command == "Hi":
            print(1)
            text = "Hi！需要甚麼服務呢?!"
            bot.sendMessage(header[2], text.format(msg["from"]["first_name"]))
        elif command == 'weather' or command ==  '天氣' or command == '氣象':
            print(2)
            text = ' https://www.cwb.gov.tw/V7/forecast/ '
            bot.sendMessage(header[2], text.format(msg["from"]["first_name"]))
        elif command == "mv":
            print(3)
            text = ' @youtube '
            bot.sendMessage(header[2], text)
    else :
        text = "海豹還聽不懂你在說什麼QQ"
        bot.sendMessage(header[2], text.format(msg["from"]["first_name"]))

MessageLoop(bot, on_chat).run_as_thread()
print('Listening ...')

while True:
    time.sleep(10)
