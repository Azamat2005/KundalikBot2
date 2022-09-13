import sqlite3

def addUserDataBase(username, id):
    conn =sqlite3.connect('Kundalik.db')
    c = conn.cursor()
    try:
        c.execute(f"INSERT INTO Users VALUES (?,?)", (username,id))
    except:
        print("Oldin ro'xatdan o'tgan")
    conn.commit()
    conn.close()