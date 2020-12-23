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

def leiaFloat(mg):
    while True:
        try:
            r = float(input(mg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUsuário preferiu não digitar esse número. \033[m')
            return 0
        else:
            return r


num = leiaInt('Digite um número inteiro: ')
r = leiaFloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {num} e o real foi {r}.')