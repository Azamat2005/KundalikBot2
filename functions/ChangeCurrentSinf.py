import sqlite3
def ChangeSinf(Sinf, id):
    conn = sqlite3.connect('Kundalik.db')
    c = conn.cursor()
    
    try:
        c.execute(f"INSERT INTO CurrentSinf VALUES(?,?)", (Sinf, id))
       
    except:
         c.execute(f"UPDATE CurrentSinf SET Sinf='{Sinf}' WHERE id={id}")

    conn.commit()
    conn.close()