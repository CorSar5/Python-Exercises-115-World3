from time import sleep


def linha():
    print('-='*25)


def contador(inicio, fim, passo):
    linha()
    sleep(1.5)
    if passo != 0:
        print(f'Contagem de {i} até {f} de {p} em {p}')
        if inicio < fim:
            for c in range(inicio, fim+1, passo):
                print(c, end=' ')
                sleep(1/4)

        elif fim < inicio and passo >= 1:
            for c in range(inicio, fim-1, -passo):
                print(c, end=' ')
                sleep(1 / 4)
        elif fim < inicio and passo <= -1:
            for c in range(inicio, fim-1, passo):
                print(c, end=' ')
                sleep(1/4)
    if passo == 0:
        print(f'Contagem de {i} até {f} de {p+1} em {p+1}')
        if inicio < fim:
            for c in range(inicio, fim + 1, 1):
                print(c, end=' ')
                sleep(1 / 4)
        else:
            for c in range(inicio, fim - 1, -1):
                print(c, end=' ')
                sleep(1 / 4)
    print('FIM!')
    linha()


linha()
print('Contagem de 1 até 10 de 1 em 1')
for c in range(1,11,1):
    print(c, end=' ')
    sleep(1/5)
print('FIM!')
sleep(1/5)
linha()
print('Contagem de 10 até 0 de 2 em 2')
for c in range(10, -1, -2):
    print(c, end=' ')
    sleep(1/5)
print('FIM!')
sleep(1/5)
linha()
print('Agora é a sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))
contador(i, f, p)


# Solução AULA
from time import sleep


def contador(i, f, p):
    if p <0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f}de {p} em {p}')
    sleep(2.5)
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True) # este flush é usado para evitar bugs de espera de tempo aquando uso do float no sleep
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = 0
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(1 / 2)
            cont -= p
        print('FIM!')


#Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-='*20)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)