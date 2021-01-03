def leiaString(mens):
    while True:
        k = ('pussy','dick','fuck','motherfucker','merda','caralho','pila','penis','pica','piça','foda-se','fodase','pénis','fodasse','puta','cona','cabrao','vaca', 'foda', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
        try:
            m = str(input(mens)).lower()
        except (KeyboardInterrupt):
            print('\n\033[31mUser preferred not to type his name. \033[m')
            return 0
        except (TypeError, ValueError):
            print('\n\033[31mUser must enter his name correctly. \033[m')
            continue
        m = m.replace(' ', '')
        if m.isnumeric():
            print('\033[31mERROR: please enter a valid name\033[m')
            continue
        if m in k:
            print('\033[31mERROR: please enter a valid name\033[m')
            continue
        for n in k:
            if n in m:
                print('\033[31mERROR: please enter a valid name\033[m')
                break
            continue
        else:
            m = m.capitalize()
            return m


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
            if n< 0:
                print('\033[31mERROR: please enter a real age\033[m')
                continue
            elif n>115:
                print('\033[31mERROR: please enter a real age\033[m')
                continue
        except (ValueError, TypeError):
            print('\033[31mERROR: please enter a valid integer\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUser preferred not to enter this number. \033[m')
            return 0

        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('\033[35mMAIN MENU\033[m')
    c=1
    for i in lista:
        print(f'\033[33m{c}\033[m - \033[m{i}\033[m')
        c+=1
    print(linha())
    opc = leiaInt('\033[32mYour Option: \033[m')
    return opc