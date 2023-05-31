def cadastro(pessoa, lista):
    pessoa['nome'] = str(input("digite seu nome: "))
    pessoa['sobrenome'] = str(input("digite seu sobrenome: "))
    pessoa['idade'] = int(input("digite sua idade: "))
    pessoa['profissão'] = str(input("digite sua profissão: "))
    pessoa['CPF'] = int(input("digite seu CPF: "))
    pessoa['email'] = str(input("Crie um Email: "))
    pessoa['senha'] = str(input("Crie uma senha: "))
    lista.append(pessoa.copy())
    return(lista)
    

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