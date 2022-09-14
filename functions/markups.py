from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# ---Main menu ----
Sinf11A = KeyboardButton('11-A Sinf')
Sinf11B = KeyboardButton('11-B Sinf')
Sinf10A = KeyboardButton("10-A Sinf")
Sinf10B = KeyboardButton("10-B Sinf")
Sinf9A = KeyboardButton("9-A Sinf")
Sinf9B = KeyboardButton("9-B Sinf")
Sinf8A = KeyboardButton('8-A Sinf')
Sinf8B = KeyboardButton('8-B Sinf')
Sinf7A = KeyboardButton("7-A Sinf")
Sinf7B = KeyboardButton("7-B Sinf")
Sinf6A = KeyboardButton('6-A Sinf')
Sinf6B = KeyboardButton("6-B Sinf")
Sinf5A = KeyboardButton('5-A Sinf')
Sinf5B = KeyboardButton('5-B Sinf')
Sinf4A = KeyboardButton("4-A Sinf")
Sinf4B = KeyboardButton("4-B Sinf")
Sinf3A = KeyboardButton("3-A Sinf")
Sinf3B = KeyboardButton('3-B Sinf')
Sinf2A = KeyboardButton("2-A Sinf")
Sinf2B = KeyboardButton('2-B Sinf')
Sinf1A = KeyboardButton('1-A Sinf')
Sinf1B = KeyboardButton("1-B Sinf")

MainMarkup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(
    Sinf11A,Sinf11B,Sinf10A, Sinf10B,
    Sinf9A,Sinf9B, Sinf8A,Sinf8B,
    Sinf7A, Sinf7B,Sinf6A,Sinf6B,
    Sinf5A,Sinf5B,Sinf4A,Sinf4B,
    Sinf3A,Sinf3B,Sinf2A,Sinf2B,
    Sinf1A,Sinf1B,
)

# ---End main menu  ----



#---Kunlar ------

Dushanba = KeyboardButton("Dushanba")
Seshanba = KeyboardButton("Seshanba")
Chorshanba = KeyboardButton("Chorshanba")
Payshanba = KeyboardButton("Payshanba")
Juma = KeyboardButton("Juma")
Shanba = KeyboardButton("Shanba")
Orqaga = KeyboardButton("Orqaga")

HaftaKunlari = ReplyKeyboardMarkup(resize_keyboard=True).add(
    Dushanba,Seshanba,Chorshanba,
    Payshanba,Juma,Shanba,
    Orqaga,
    row_width=2
)


#----- Admin panel ---- 

AllUser = KeyboardButton("All User")
ChooseUser = KeyboardButton("Choose User")

Admin = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add(
    AllUser,
    ChooseUser
)