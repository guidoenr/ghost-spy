from telegram import *
from telegram.ext import *
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

bot = Bot("1758554339:AAFl8JZ3x4Sd281OfWZbkg5qTN3YqDRP3D0")
updater = Updater("1758554339:AAFl8JZ3x4Sd281OfWZbkg5qTN3YqDRP3D0", use_context=True)
dispatcher = updater.dispatcher


def start(update:Update, context:CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome sir")

def login(update,context):
    pass



start_handler = CommandHandler('start', start)
login_handler = CommandHandler('login', login)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(login_handler)



if __name__ == '__main__':
    print(bot.get_me())
    updater.start_polling()