def moeda(p=0.0, moeda='€'):
    return f'{moeda}{p:>6.2f}'.replace('.', ',')


def metade(p=0, sit=False):
    p /=2
    if sit==True:
        return(moeda(p))
    else:
        return p


def dobro(p=0, sit=False):
    p *= 2
    return p if not sit else moeda(p)


def aumentar(p=0, x=0, sit=False):
    p = p + p * (x / 100)
    if sit == True:
        return (moeda(p))
    else:
        return p


def diminuir(p=0, x=0, sit=False):
    p = p - p*(x/100)
    return p if sit is False else moeda(p)


def resumo(p=0, a=10, d=5):
        print('-'*30)
        print('RESUMO DO VALOR'.center(30))
        print('-' * 30)
        print(f'Preço Analisado: \t{moeda(p):>12}')
        print(f'Dobro do preço:   \t{dobro(p,True):>12}')
        print(f'Metade do preço: \t{metade(p,True):>12}')
        print(f'{a}% de aumento:  \t{aumentar(p, a, True):>12}')
        print(f'{d}% de aumento:  \t{diminuir(p, d,True):>12}')
        print('-'*30)