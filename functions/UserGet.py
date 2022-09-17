import sqlite3

def sendUser():
    conn = sqlite3.connect("Kundalik.db")

    c = conn.cursor()

    try:
        c.execute("""SELECT * FROM Users""")
        items = c.fetchall()

       
        ll =[]
        for item in items:
        
            ll.append({"id":item[1], "UserName":item[0]})


        return ll
    except:
        print("Xato Userda")
        
    conn.commit()
    conn.close()