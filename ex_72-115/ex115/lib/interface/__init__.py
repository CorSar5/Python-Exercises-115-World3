def calao(p):
    while True:
        k = ['caralho','pila','penis','pica','piça','foda-se','fodase','pénis','fodasse','puta','cona','cabrao','vaca', 'aceite']
        p = str(input(p)).lower()
        if p in k:
            print('\033[31mERRO: por favor, digite um nome válido\033[m')
            continue
        for n in k:
            if n in p:
                print('\033[31mERRO: por favor, digite um nome válido\033[m')
                continue
            if n == 'aceite':
                break
        else:
            p = p.capitalize()
            return p


def leiaString(mens):
    while True:
        l = ('1','2','3','4','5','6','7','8','9','0')
        try:
            m = str(input(mens)).lower()
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar o seu nome. \033[m')
            return 0
        if m.isnumeric():
            print('\033[31mERRO: por favor, digite um nome válido\033[m')
            continue
        calao(m)
        #não atribuir números a nomes
        '''for c in l:
            if c in m:
                print('\033[31mERRO: por favor, digite um nome válido\033[m')

        if m in k:
            print('\033[31mERRO: por favor, digite um nome válido\033[m')
            continue'''
        #impedir palavras calão escritas com mais 1 letra

        '''if m in k:
            print('\033[31mERRO: por favor, digite um nome válido\033[m')
            continue
        for n in k:
            if n in m:
                print('\033[31mERRO: por favor, digite um nome válido\033[m')
                continue
            if n == 'aceite':
                break
        else:
            return m'''


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número. \033[m')
            return 0
        else:
            return n


def linha(tam = 42):
    return '-' *tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('\033[35mMENU PRINCIPAL\033[m')
    c = 1
    for i in lista:
        print(f'\033[33m{c}\033[m - \033[m{i}\033[m')
        c += 1
    print(linha())
    opc = leiaInt('\033[32mSua opção: \033[m')
    return opc