from funcoes import cadastro, Exibir, Editar, Excluir, loginn, lercadas
import sqlite3

conn = sqlite3.connect('3af')
c = conn.cursor

opc = 0
loginre = 0
lista = list()
pessoa = dict()
login = False
n = 0
num = int
nume = 3
numcadas = 0


while(num != 2):
    cadastrados = lercadas(conn)   
    numcadas = len(cadastrados)
    print(numcadas)

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
    print (f'Você tem {nume} tentativas ')
    emailc = str(input("Digite seu Email: "))
    senhac= str(input("Digite sua senha: "))
    loginn()
    if (loginre == 3):
        print("login realizado com sucesso")
    elif(nume == 0):
        print("Bloqueado")
        break    
    else:
        print ("erro")
        nume = nume - 1
    



while (opc != 4):
    print("olá {} {}".format(lista[n]['nome'], lista[n]['sobrenome']))
    print("1 - Exibir | 2 - Editar | 3 - Excluir | 4 - Sair")
    opc = int(input("digite um numero"))
    if opc == 1:
        Exibir(lista, n)
    elif opc == 2:
        Editar(lista, n)
    elif opc == 3:
        Excluir(lista, n)
    elif opc == 4:
        print("Tenha um ótimo dia!")
        break