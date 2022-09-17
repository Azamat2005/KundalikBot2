from math import sin
import sqlite3

def getCurrentSinf(id):
    conn = sqlite3.connect('Kundalik.db')
    c = conn.cursor()

    try:
        c.execute(f"SELECT Sinf FROM CurrentSinf WHERE id={id}")
        sinf = c.fetchone()
    except:
        pass

    

    conn.commit()
    conn.close()

    try:
        if sinf:
            return sinf[0]
    except:
        pass
