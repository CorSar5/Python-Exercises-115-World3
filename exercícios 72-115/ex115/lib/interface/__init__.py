def leiaString(mens):
    while True:
        k = ('caralho','pila','penis','pica','piça','foda-se','fodase','pénis','fodasse','puta','cona','cabrao','vaca', 'aceite', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
        try:
            m = str(input(mens)).lower()
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar o seu nome. \033[m')
            return 0
        except (TypeError, ValueError):
            print('\n\033[31mUsuário deve digitar o seu nome corretamente. \033[m')
            continue
        m = m.replace(' ', '')
        if m.isnumeric():
            print('\033[31mERRO: por favor, digite um nome válido\033[m')
            continue
        if m in k:
            print('\033[31mERRO: por favor, digite um nome válido\033[m')
            continue
        for n in k:
            if n in m:
                print('\033[31mERRO: por favor, digite um nome válido\033[m')
                break
            continue
        else:
            m = m.capitalize()
            return m


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
        except (-1 < msg < 115):
            print('\033[31mERRO: por favor, digite um número inteiro válido\033[m')
            continue
        else:
            return n


def linha(tam=42):
    return '-' * tam


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
