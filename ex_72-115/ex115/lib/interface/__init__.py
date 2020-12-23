def calao(mens):
    while True:
        k = ['caralho','pila','penis','pica','piça','foda-se','fodase','pénis','fodasse','puta','cona','cabrao','vaca', 'foda']
        try:
            p = mens
        except (KeyboardInterrupt):
            print('\033[31mO Usuário não digitou o seu nome\033[m')
            continue
        if p in k:
            print('\033[31mERRO: por favor, digite um nome válido\033[m')
            continue
        for n in k:
            if n in p:
                print('\033[31mERRO: por favor, digite um nome válido\033[m')
                break
            continue
        else:
            p = p.capitalize()
            return p
        p = str(input(mens)).lower()


def numero(mens):
    while True:
        l = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        try:
            c = str(input(mens))
            c=c.replace(' ','')
            c=c.replace(',','')
        except (KeyboardInterrupt):
            print('\033[31mO Usuário não digitou o seu nome\033[m')
            continue
        if c in l:
            print('\033[31mERRO: por favor, digite um nome válido\033[m')
            continue
        for n in l:
            if n in c:
                print('\033[31mERRO: por favor, digite um nome válido\033[m')
                break
            continue
        else:
            c = c.capitalize()
            return c


def leiaString(m):
    while True:
        mens = str(input(m)).lower()
        m = m.replace(' ', '')
        m = m.replace(',', '')
        m = m.replace('-', '')
        m = m.replace('_', '')
        m = m.replace('.', '')
        m = m.replace(';', '')
        m = m.replace(':', '')
        m = m.replace('/', '')
        calao(mens)
        return mens


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