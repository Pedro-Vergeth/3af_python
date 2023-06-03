def lercadas(conn):
    cursor = conn.cursor()
    sql = 'select * from trabalhadores'
    cursor.execute(sql)
    return cursor.fetchall()
    
    

def cadastro(conn):
    nomen = str(input("digite seu nome: "))
    sobrenomen = str(input("digite seu sobrenome: "))
    idaden= int(input("digite sua idade: "))
    profissaon= str(input("digite sua profissão: "))
    CPFN= int(input("digite seu CPF: "))
    emailn= str(input("Crie um Email: "))
    senhan = str(input("Crie uma senha: "))

    cursor = conn.cursor()
    sql = 'INSERT INTO trabalhadores(nome, sobrenome, idade, CPF, profissão, email, senha) VALUES (?, ?, ?, ?, ?, ?, ?)'
    cursor.execute(sql, [nomen, sobrenomen, idaden, CPFN, profissaon, emailn, senhan])
    conn.commit()
    print("Cadastro realizado")
    
    return

def loginn():
    for i in range(len(lista)):
        if(lista[i]['email'] == emailc and lista[i]['senha'] == senhac):
            loginre = 3
            n = i
        else:
            i = i + 1


def Exibir(lista, n):
    
    print(lista[n])

def Editar(lista, n):
    
    print("Nome | Sobrenome | Idade | Profissão | CPF | Email | Senha")
    opca = str(input("O que você quer editar:"))
    if opca == 'Nome':
        Nomen = str(input("Digite o novo nome:"))
        lista[n]['Nome'] = Nomen
    elif opca == 'Sobrenome':
        sobrn = str(input("Digite seu novo sobrenome: "))
        lista[n]['sobrenome'] = sobrn
    elif opca == 'Idade':
        idaden = str(input("Digite a nova idade: "))
        lista[n]['idade'] = idaden
    elif opca == 'Profissão':
        profn = str(input("Digite sua nova profissão: "))
        lista[n]['profissão'] = profn
    elif opca == 'CPF':
        cpfn = str(input("Digite o novo CPF: "))
        lista[n]['CPF'] = cpfn
    elif opca == 'Email':
        Emailnv = str(input("Digite seu novo email: "))
        lista[n]['email'] = Emailnv
    elif opca == 'Senha':
        senhanv = str(input("Digite sua nova senha: "))
        lista[n]['senha'] = senhanv
    else:
        print("erro")
    return(lista)

def Excluir():
    
    print("Nome | Sobrenome | Idade | Profissão | CPF | Email | Senha")
    opco = str(input("O que você quer editar:"))
    if opco == 'Nome':
        lista[n]['Nome'] = ''
    elif opco == 'Sobrenome':
        lista[n]['sobrenome'] = ''
    elif opco == 'Idade':
        lista[n]['idade'] = ''
    elif opco == 'Profissão':
        lista[n]['profissão'] = ''
    elif opco == 'CPF':
        lista[n]['CPF'] = ''
    elif opco == 'Email':
        lista[n]['email'] = ''
    elif opco == 'Senha':
        lista[n]['senha'] = ''
    else:
        print("erro")
    return(lista)