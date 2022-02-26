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
    textToReturn = "Added: "
    try:
        textToReturn = textToReturn + update.message.text[5:]


        textSplitBySpace = update.message.text[5:].split()
        if len(textSplitBySpace) > 3:
            raise Exception("Too many parameters")
        if not textSplitBySpace[1].isdigit():
            raise Exception("Not a time")
        if textSplitBySpace[0].lower() not in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',
                                               'sunday']:
            raise Exception("Not day")

        json_adder(update.message.text[5:])
    except Exception as e:
        textToReturn = "Use the format of [Day] [Time] [Link], for example: Monday 1600 google.com"

    context.bot.send_message(chat_id=update.effective_chat.id, text=textToReturn)


add_handler = CommandHandler('add', add, pass_args=True)
dispatcher.add_handler(add_handler)

import json


def json_adder(string):
    splitBySpace = string.split()
    with open("storage.json", "r+") as file:
        content = json.load(file)
        new_object = {"day": splitBySpace[0], "time": splitBySpace[1], "link": splitBySpace[2]}
        print(new_object)
        content["reminder"].insert(0, new_object)
        file.seek(0)
        json.dump(content, file)
        file.truncate()


def listing(update: Update, context: CallbackContext):
    textToReturn = ""

    try:
        with open("storage.json") as file:
            content = json.load(file)

        index = 1
        for item in content["reminder"]:
            tempString = str(index) + ". "
            tempString = tempString + item['day'] + " "
            tempString = tempString + item['time'] + " "
            tempString = tempString + item['link']
            textToReturn = textToReturn + tempString + "\n"
            index+=1
    except Exception as e:
        textToReturn = "Use the format of [Day] [Time] [Link], for example: Monday 1600 google.com"

    context.bot.send_message(chat_id=update.effective_chat.id, text=textToReturn)



list_handler = CommandHandler('list', listing)
dispatcher.add_handler(list_handler)

##json deletor
def json_deletor(ind):

    with open("storage.json", "r+") as file:
        print('fuck')
        content = json.load(file)
        tempList = content["reminder"]
        tempItem = tempList.pop(ind-1);
        tempString = tempItem['day'] + " "
        tempString = tempString + tempItem['time'] + " "
        tempString = tempString + tempItem['link']
        content["reminder"] = tempList
        file.seek(0)
        json.dump(content, file)
        file.truncate()
        print(tempString)
        return tempString




##Delete command
def delete(update: Update, context: CallbackContext):
    textToReturn = "Deleted: "
    try:
        textSplitBySpace = update.message.text.split()
        if len(textSplitBySpace) > 2:
            raise Exception("Too many parameters")
        if not textSplitBySpace[1].isdigit():
            raise Exception("Not an Index")

        textToReturn = textToReturn + json_deletor(int(textSplitBySpace[1]))

    except Exception as e:
        print(e)
        textToReturn = "The format is [Index] using the correct index, for example: 1"

    context.bot.send_message(chat_id=update.effective_chat.id, text=textToReturn)


delete_handler = CommandHandler('delete', delete, pass_args=True)
dispatcher.add_handler(delete_handler)

