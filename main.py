from telegram.ext import *
import logging
from telegram import Update
import json
import random

updater = Updater(token='TOKEN', use_context=True)

dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello!")


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


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
            raise Exception("Not a day")

        json_adder(update.message.text[5:])
    except Exception as e:
        textToReturn = "Use the format of [Day] [Time] [Link], for example: monday 1600 google.com"

    context.bot.send_message(chat_id=update.effective_chat.id, text=textToReturn)


add_handler = CommandHandler('add', add, pass_args=True)
dispatcher.add_handler(add_handler)


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
            index += 1
    except Exception as e:
        textToReturn = "Use the format of [Day] [Time] [Link], for example: Monday 1600 google.com"

    context.bot.send_message(chat_id=update.effective_chat.id, text=textToReturn)


list_handler = CommandHandler('list', listing)
dispatcher.add_handler(list_handler)


##json deletor
def json_deletor(ind):
    with open("storage.json", "r+") as file:
        content = json.load(file)
        tempList = content["reminder"]
        tempItem = tempList.pop(ind - 1);
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

from datetime import datetime

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def json_loader():
    with open("storage.json", "r+") as file:
        content = json.load(file)
        curr_date = str(datetime.now().weekday()).lower()
        curr_day = days[int(curr_date)].lower()
        print(curr_date)
        index = 1
        textToReturn = ""
        for item in content["reminder"]:
            if curr_day == item['day']:
                print()
                tempString = str(index) + ". "
                tempString = tempString + item['time'] + " "
                tempString = tempString + item['link'] + "\n"
                index += 1
                textToReturn = textToReturn + tempString
        return textToReturn

compliments = ['Have a great day!', 'I like your style!', "You're a smart cookie!", 'I am so proud of you, and I hope you are too!', "On a scale from 1 to 10, you're an 11.", "You're one of a kind.", 'You deserve a hug right now', 'Everyone gets knocked down sometimes; only people like you get back up again and keep going', 'You were cool way before hipsters were cool', 'You light up the room']

##notify command
def notify(update: Update, context: CallbackContext):
    
    textToReturn = "Your links for today: \n"
    try:
        textToReturn = textToReturn + json_loader() + " \n"

    except Exception as e:
        print(e)
        textToReturn = "Wrong format!"

    context.bot.send_message(chat_id=update.effective_chat.id, text=textToReturn + compliments[random.randint(0,9)])


notify_handler = CommandHandler('notify', notify)
dispatcher.add_handler(notify_handler)

updater.start_polling()
