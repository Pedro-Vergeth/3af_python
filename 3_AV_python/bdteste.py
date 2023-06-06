import sqlite3

conn = sqlite3.connect('3af')
c = conn.cursor()

sql = "UPDATE Trabalhadores SET Nome = 'iza' where Trabalhador_id = 2"
c.execute(sql)

c.fetchall()
