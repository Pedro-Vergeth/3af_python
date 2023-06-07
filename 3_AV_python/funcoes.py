

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

def loginn2(conn):
        cursor = conn.cursor()
        sql = 'select email, senha from trabalhadores'
        cursor.execute(sql)
        return cursor.fetchall()

def buscarnome(conn, p):
    p = p + 1
    print(p)
    cursor = conn.cursor()
    sql = 'select nome, sobrenome from trabalhadores where trabalhador_id = ?'
    cursor.execute(sql, [p])
    return cursor.fetchall()
    
    


def Exibir(conn, n):
    n = n + 1
    cursor = conn.cursor()
    sql ='select * from trabalhadores where trabalhador_id = ?'
    cursor.execute(sql, [n])
    return cursor.fetchall()
    
    print(lista[n])

def Editar(conn, n):
    n = n + 1
    cursor = conn.cursor()

    print("1 - Nome | 2 - Sobrenome | 3 - Idade | 4 - Profissão | 5 - CPF | 6 - Email | 7 - Senha")
    opca = int(input("O que você quer editar: "))
    if opca == 1:
        Nomen = str(input("Digite o novo nome: "))
        sql = 'UPDATE Trabalhadores SET Nome = ? WHERE Trabalhador_id = ?;'
        cursor.execute(sql, [Nomen, n])
        conn.commit()
        
    elif opca == 2:
        sobrn = str(input("Digite seu novo sobrenome: "))
        sql = 'UPDATE Trabalhadores SET Sobrenome = ? WHERE Trabalhador_id = ?;'
        cursor.execute(sql, [sobrn, n])
        conn.commit()
        
    elif opca == 3:
        idaden = str(input("Digite a nova idade: "))
        sql = 'UPDATE Trabalhadores SET Idade = ? WHERE Trabalhador_id = ?;'
        cursor.execute(sql, [idaden, n])
        conn.commit()
        
    elif opca == 4:
        profn = str(input("Digite sua nova profissão: "))
        sql = 'UPDATE Trabalhadores SET Profissão = ? WHERE Trabalhador_id = ?;'
        cursor.execute(sql, [profn, n])
        conn.commit()
        
    elif opca == 5:
        cpfn = str(input("Digite o novo CPF: "))
        sql = 'UPDATE Trabalhadores SET CPF = ? WHERE Trabalhador_id = ?;'
        cursor.execute(sql, [cpfn, n])
        conn.commit()
        
    elif opca == 6:
        Emailnv = str(input("Digite seu novo email: "))
        sql = 'UPDATE Trabalhadores SET Email = ? WHERE Trabalhador_id = ?;'
        cursor.execute(sql, [Emailnv, n])
        conn.commit()
        
    elif opca == 7:
        senhanv = str(input("Digite sua nova senha: "))
        sql = 'UPDATE Trabalhadores SET Senha = ? WHERE Trabalhador_id = ?;'
        cursor.execute(sql, [senhanv, n])
        conn.commit()
        
    else:
        print("erro")
    
    
    return 

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
    return