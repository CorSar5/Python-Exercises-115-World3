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

def aumentar(p=0, x=0,sit=False):
    p = p + p * (x / 100)
    if sit == True:
        return (moeda(p))
    else:
        return p


def diminuir(p=0, x=0, sit=False):
    p = p - p*(x/100)
    return p if sit is False else moeda(p)