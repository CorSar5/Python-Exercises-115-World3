def metade(p = 0):
    return p / 2


def dobro(p = 0):
    return p * 2


def aumentar(p = 0, x=0):
    return p + p * (x / 100)


def diminuir(p= 0, x=0):
    return p - p*(x/100)


def moeda(p = 0, moeda='€'):
    return f'{moeda}{p:>8.2f}'.replace('.',',')