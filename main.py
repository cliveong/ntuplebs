from telegram.ext import Updater

updater = Updater(token='5207140517:AAGgW7Ct8NGrjL9oUpdiRNssmVqPKP1KaV4', use_context=True)

dispatcher = updater.dispatcher

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

from telegram import Update
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="fuck u!")


from telegram.ext import CommandHandler

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()


##Add command
def add(update: Update, context: CallbackContext):
    textToReturn = "Added " + update.message.text[5:]
    json_adder(update.message.text[5:])
    context.bot.send_message(chat_id=update.effective_chat.id, text=textToReturn)


add_handler = CommandHandler('add', add, pass_args=True)
dispatcher.add_handler(add_handler)

import json

def json_adder(string):
    splitBySpace = string.split()
    with open("storage.json", "r+") as file:
        content = json.load(file)
        new_object = {"day": splitBySpace[0], "time":splitBySpace[1], "link":splitBySpace[2]}
        print(new_object)
        content["reminder"].insert(0, new_object)
        file.seek(0)
        json.dump(content, file)
        file.truncate()
