import telepot
from telepot.namedtuple import ReplyKeyboardMarkup, ReplyKeyboardRemove

class BotOutput:
    @staticmethod
    def send_text(bot, user, text):
        bot.sendMessage(user.chat_id, text)
