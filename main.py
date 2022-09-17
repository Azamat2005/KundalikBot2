import sqlite3
import os
from dotenv import load_dotenv
import telebot 
import functions.markups as markups
import functions.getUser as getUser
import functions.KunList as KunList
import functions.SinfList as SinfList
import functions.ChangeCurrentSinf as ChangeCurrentSinf
import functions.GetCurrentSinf as GetCurrentSinf
import functions.GetTable as GetTable
import datetime
import functions.UserGet as UserGet

load_dotenv()
TOKENBOT = os.getenv("Token")

bot = telebot.TeleBot(TOKENBOT)

@bot.message_handler(commands=['start'])
def start(message):
    ism = message.from_user.first_name
    userId = message.from_user.id


    getUser.addUserDataBase(ism, userId)
    bot.send_message(chat_id=message.chat.id, text="Salom bot ga xush kelibsiz", reply_markup=markups.MainMarkup)
    
    
    

@bot.message_handler(content_types=['text'])
def Sinflar(message):
    
    try:
        now = datetime.datetime.now()
        nowDate = f"year:{now.year} month:{now.month}, day:{now.day} hour:{now.hour}, minute:{now.minute} "
        username = message.from_user.username
        id = message.from_user.id
        chats = message.text
    except:
        pass

    SinfLar = SinfList.Sinflar()
    for Sinf in SinfLar:
        if Sinf == message.text:
            bot.send_message(chat_id=message.chat.id, text="Hafta kunlarning birini tanlang", reply_markup=markups.HaftaKunlari)
            ChangeCurrentSinf.ChangeSinf(Sinf, message.chat.id)

    if message.text == 'Orqaga':
        bot.send_message(chat_id=message.chat.id, text="Ortga", reply_markup=markups.MainMarkup)


    days = KunList.Kunlar()
    for day in days:
        if day == message.text:
            CurSinf = GetCurrentSinf.getCurrentSinf(message.chat.id)
            msg = GetTable.Jadval(CurSinf, day)
            
            bot.send_message(chat_id=message.chat.id, text=msg)

    if message.text == "Update database":
        bot.send_message(chat_id=message.chat.id, text='Enter Password')
        bot.register_next_step_handler(message=message, callback=CheckPassword)

    if message.text == "Send database":
        bot.send_message(chat_id=message.chat.id,text="Enter Password")
        bot.register_next_step_handler(message=message, callback=CheckSendPassword)

    conn = sqlite3.connect('Kundalik.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO UsersChat VALUES (?,?,?, ?)", (username, id, chats, nowDate))
    except:
        pass

    conn.commit()
    conn.close()


    if message.text == "Send Chat":
        bot.send_message(chat_id=message.chat.id, text="Enter password")
        bot.register_next_step_handler(message=message, callback=pasww)

def pasww(message):
    if message.text == "Azamat20050308":
        bot.send_message(chat_id=message.chat.id, text="Correct", reply_markup=markups.Admin)
        bot.register_next_step_handler(message=message, callback=ChooseOptions)

def ChooseOptions(message):
    if message.text == "All User":
        bot.send_message(chat_id=message.chat.id, text="Chatni boshlang: ")
        bot.register_next_step_handler(message=message, callback=AllUserChat)
    if message.text == "Choose User":
        pass


def AllUserChat(message):
    users = UserGet.sendUser()

    for user in users:
        try:
            bot.send_message(chat_id = int(user['id']), text=message.text)
        except:
            print("Xato")
            
   

    
    bot.register_next_step_handler(message=message, callback=ChooseOptions) 

def CheckSendPassword(message):

    if message.text == "Azamat20050308":
        bot.send_message(chat_id=message.chat.id, text="Correct password")
        bot.register_next_step_handler(message=message, callback=SendDataFile)


def SendDataFile(message):




    with open("Kundalik.db",'rb') as file:
        bot.send_document(message.from_user.id, document=file)


  
def CheckPassword(message):

    if message.text == "Azamat20050308":
        bot.send_message(chat_id=message.chat.id, text="Correct Password")
        bot.send_message(chat_id=message.chat.id, text="Send new database file")
        bot.register_next_step_handler(message=message, callback=getData)
      
    else:
        bot.send_message(chat_id=message.chat.id, text="try again")
    
def getData(message):
    
    file_path = bot.get_file(message.document.file_id).file_path

    file = bot.download_file(file_path=file_path)
            
    

    bot.send_message(chat_id=message.chat.id, text="Complete")
    

   
    with open('Kundalik.db', 'wb') as data:
            data.write(file)



bot.enable_save_next_step_handlers(delay=5)
bot.load_next_step_handlers()

bot.polling(non_stop=True)