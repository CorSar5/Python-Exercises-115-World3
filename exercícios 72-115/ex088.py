from time import sleep
from random import randint
jogos = list()
lista = list()
print('=-'* 30 )
print('     JOGA NA MEGA SENA     ')
print('=-'* 30 )
n = int(input('Quantos jogos você quer sortear? '))
tot = 1
while tot <= n:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in jogos:
            jogos.append(num)
            cont += 1
        if cont>= 6:
            break
    jogos.sort()
    lista.append(jogos[:])
    jogos.clear()
    tot += 1
print('=-'* 3, f'SORTEANDO {n} JOGOS', '-=' * 3)
for i, l in enumerate(lista):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-='*5, '<BOA SORTE>','-='*5)