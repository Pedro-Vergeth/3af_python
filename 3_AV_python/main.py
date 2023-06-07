from funcoes import cadastro, Exibir, Editar, Excluir, loginn2, lercadas, buscarnome
import sqlite3
import os

loginre = 0
conn = sqlite3.connect('3af')
c = conn.cursor
opc = 0
lista = list()
pessoa = dict()
login = False
n = 0
num = int
nume = 3
i = 0
p = 0


while(num != 2):
    print("1 - Cadastro | 2 - Login")
    num = int(input("digite um número: "))
    if(num == 1):
        cadastro(conn)
        continue
        
    elif(num == 2):
        print("Ok!")
    else:
        print("erro")
        continue


while(loginre != 3):
    i = 0
    print (f'Você tem {nume} tentativas ')
    emailc = str(input("Digite seu Email: "))
    senhac= str(input("Digite sua senha: "))
    
    cadastrado = lercadas(conn)   
    usuario = loginn2(conn)
    print(usuario)
    
    
    p = 0
    for i in cadastrado:

        if usuario[p][0] == emailc and usuario[p][1] == senhac:
            n = p
            loginre = 3
            
        else:
            p = p + 1
    if (loginre == 3):
        print("login realizado com sucesso")
    elif(nume == 0):
        print("Bloqueado")
        break
    else:
        print ("erro")
        nume = nume - 1
        print(nume)
        




nomebc = buscarnome(conn, n)


print("olá {} {}".format(nomebc[n][0], nomebc[n][1]))


while (opc != 4):
    
    print("1 - Exibir | 2 - Editar | 3 - Excluir | 4 - Sair")
    opc = int(input("digite um numero: "))
    if opc == 1:
        exibirdados = Exibir(conn, n)
        print(exibirdados)
        os.system("pause")
    elif opc == 2:
        Editar(conn, n)
    elif opc == 3:
        Excluir(conn, n)
    elif opc == 4:
        print("Tenha um ótimo dia!")
        break