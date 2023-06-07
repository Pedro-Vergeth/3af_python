import sqlite3
conn = sqlite3.connect('3af')
c = conn.cursor()

def lercadas(conn):
    cursor = conn.cursor()
    sql = 'select * from trabalhadores'
    cursor.execute(sql)
    return cursor.fetchall()


nomes = lercadas(conn)

n = 0

for i in nomes:
    print(nomes[n])
    n = n + 1


