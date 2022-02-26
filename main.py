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

##notify command
def notify(update: Update, context: CallbackContext):
    textToReturn = "Your links for today: \n"
    try:
        textToReturn = textToReturn + json_loader()

    except Exception as e:
        print(e)
        textToReturn = "wrong format lah chee bye"

    context.bot.send_message(chat_id=update.effective_chat.id, text=textToReturn)


notify_handler = CommandHandler('notify', notify)
dispatcher.add_handler(notify_handler)

import random
insults = ["4r5e", "5h1t", "5hit", "a55", "anal", "anus", "ar5e", "arrse", "arse", "ass", "ass-fucker", "asses", "assfucker", "assfukka", "asshole", "assholes", "asswhole", "a_s_s", "b!tch", "b00bs", "b17ch", "b1tch", "ballbag", "balls", "ballsack", "bastard", "beastial", "beastiality", "bellend", "bestial", "bestiality", "bi+ch", "biatch", "bitch", "bitcher", "bitchers", "bitches", "bitchin", "bitching", "bloody", "blow job", "blowjob", "blowjobs", "boiolas", "bollock", "bollok", "boner", "boob", "boobs", "booobs", "boooobs", "booooobs", "booooooobs", "breasts", "buceta", "bugger", "bum", "bunny fucker", "butt", "butthole", "buttmuch", "buttplug", "c0ck", "c0cksucker", "carpet muncher", "cawk", "chink", "cipa", "cl1t", "clit", "clitoris", "clits", "cnut", "cock", "cock-sucker", "cockface", "cockhead", "cockmunch", "cockmuncher", "cocks", "cocksuck", "cocksucked", "cocksucker", "cocksucking", "cocksucks", "cocksuka", "cocksukka", "cok", "cokmuncher", "coksucka", "coon", "cox", "crap", "cum", "cummer", "cumming", "cums", "cumshot", "cunilingus", "cunillingus", "cunnilingus", "cunt", "cuntlick", "cuntlicker", "cuntlicking", "cunts", "cyalis", "cyberfuc", "cyberfuck", "cyberfucked", "cyberfucker", "cyberfuckers", "cyberfucking", "d1ck", "damn", "dick", "dickhead", "dildo", "dildos", "dink", "dinks", "dirsa", "dlck", "dog-fucker", "doggin", "dogging", "donkeyribber", "doosh", "duche", "dyke", "ejaculate", "ejaculated", "ejaculates", "ejaculating", "ejaculatings", "ejaculation", "ejakulate", "f u c k", "f u c k e r", "f4nny", "fag", "fagging", "faggitt", "faggot", "faggs", "fagot", "fagots", "fags", "fanny", "fannyflaps", "fannyfucker", "fanyy", "fatass", "fcuk", "fcuker", "fcuking", "feck", "fecker", "felching", "fellate", "fellatio", "fingerfuck", "fingerfucked", "fingerfucker", "fingerfuckers", "fingerfucking", "fingerfucks", "fistfuck", "fistfucked", "fistfucker", "fistfuckers", "fistfucking", "fistfuckings", "fistfucks", "flange", "fook", "fooker", "fuck", "fucka", "fucked", "fucker", "fuckers", "fuckhead", "fuckheads", "fuckin", "fucking", "fuckings", "fuckingshitmotherfucker", "fuckme", "fucks", "fuckwhit", "fuckwit", "fudge packer", "fudgepacker", "fuk", "fuker", "fukker", "fukkin", "fuks", "fukwhit", "fukwit", "fux", "fux0r", "f_u_c_k", "gangbang", "gangbanged", "gangbangs", "gaylord", "gaysex", "goatse", "God", "god-dam", "god-damned", "goddamn", "goddamned", "hardcoresex", "hell", "heshe", "hoar", "hoare", "hoer", "homo", "hore", "horniest", "horny", "hotsex", "jack-off", "jackoff", "jap", "jerk-off", "jism", "jiz", "jizm", "jizz", "kawk", "knob", "knobead", "knobed", "knobend", "knobhead", "knobjocky", "knobjokey", "kock", "kondum", "kondums", "kum", "kummer", "kumming", "kums", "kunilingus", "l3i+ch", "l3itch", "labia", "lust", "lusting", "m0f0", "m0fo", "m45terbate", "ma5terb8", "ma5terbate", "masochist", "master-bate", "masterb8", "masterbat*", "masterbat3", "masterbate", "masterbation", "masterbations", "masturbate", "mo-fo", "mof0", "mofo", "mothafuck", "mothafucka", "mothafuckas", "mothafuckaz", "mothafucked", "mothafucker", "mothafuckers", "mothafuckin", "mothafucking", "mothafuckings", "mothafucks", "mother fucker", "motherfuck", "motherfucked", "motherfucker", "motherfuckers", "motherfuckin", "motherfucking", "motherfuckings", "motherfuckka", "motherfucks", "muff", "mutha", "muthafecker", "muthafuckker", "muther", "mutherfucker", "n1gga", "n1gger", "nazi", "nigg3r", "nigg4h", "nigga", "niggah", "niggas", "niggaz", "nigger", "niggers", "nob", "nob jokey", "nobhead", "nobjocky", "nobjokey", "numbnuts", "nutsack", "orgasim", "orgasims", "orgasm", "orgasms", "p0rn", "pawn", "pecker", "penis", "penisfucker", "phonesex", "phuck", "phuk", "phuked", "phuking", "phukked", "phukking", "phuks", "phuq", "pigfucker", "pimpis", "piss", "pissed", "pisser", "pissers", "pisses", "pissflaps", "pissin", "pissing", "pissoff", "poop", "porn", "porno", "pornography", "pornos", "prick", "pricks", "pron", "pube", "pusse", "pussi", "pussies", "pussy", "pussys", "rectum", "retard", "rimjaw", "rimming", "s hit", "s.o.b.", "sadist", "schlong", "screwing", "scroat", "scrote", "scrotum", "semen", "sex", "sh!+", "sh!t", "sh1t", "shag", "shagger", "shaggin", "shagging", "shemale", "shi+", "shit", "shitdick", "shite", "shited", "shitey", "shitfuck", "shitfull", "shithead", "shiting", "shitings", "shits", "shitted", "shitter", "shitters", "shitting", "shittings", "shitty", "skank", "slut", "sluts", "smegma", "smut", "snatch", "son-of-a-bitch", "spac", "spunk", "s_h_i_t", "t1tt1e5", "t1tties", "teets", "teez", "testical", "testicle", "tit", "titfuck", "tits", "titt", "tittie5", "tittiefucker", "titties", "tittyfuck", "tittywank", "titwank", "tosser", "turd", "tw4t", "twat", "twathead", "twatty", "twunt", "twunter", "v14gra", "v1gra", "vagina", "viagra", "vulva", "w00se", "wang", "wank", "wanker", "wanky", "whoar", "whore", "willies", "willy", "xrated", "xxx"]
##notify command
def insult(update: Update, context: CallbackContext):
    textToReturn = update.message.text[8:] + " is a fucking " + insults[random.randint(0, 300)]

    context.bot.send_message(chat_id=update.effective_chat.id, text=textToReturn)


insult_handler = CommandHandler('insult', insult, pass_args=True)
dispatcher.add_handler(insult_handler)

updater.start_polling()