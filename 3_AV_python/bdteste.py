import sqlite3

conn = sqlite3.connect('3af')
c = conn.cursor()
def teste():
    global c
    sql = f'select * from trabalhadores'
    c.execute(sql)
    return c.fetchall()

teste1 = teste()
print(len(teste1))