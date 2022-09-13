import sqlite3

def Jadval(Sinf, Kun):
    conn = sqlite3.connect('Kundalik.db')
    c = conn.cursor()
    try:
        c.execute(f"SELECT * FROM '{Sinf}' WHERE kun='{Kun}' ")
        jadval = c.fetchone()

        msg = f"Sinf: {Sinf}\nKun: {Kun}\n"
        msg +=f"1: {jadval[1]}\n"
        msg +=f"2: {jadval[2]}\n"
        msg +=f"3: {jadval[3]}\n"
       
        if len(jadval[4]) > 0:
            msg +=f"4: {jadval[4]}\n" 

        if len(jadval[5])  > 0:
            msg+=f"5: {jadval[5]}\n"    
        if len(jadval[6]) > 0:
            msg+=f"6: {jadval[6]}\n"    

    except:
        pass

    conn.commit()
    conn.close()

    return msg