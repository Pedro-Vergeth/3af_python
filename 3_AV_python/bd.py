import sqlite3

conn = sqlite3.connect('3af')
c = conn.cursor()

c.execute('''
create table Trabalhadores(
Trabalhador_id integer primary key autoincrement,
Nome varchar(150) not null,
Sobrenome varchar(150) not null,
Idade varchar(3) not null,
CPF varchar(12) not null,
Profissão varchar(150) not null,
Email varchar(150) not null,
senha varchar(150) not null
)
  ''')

conn.commit()