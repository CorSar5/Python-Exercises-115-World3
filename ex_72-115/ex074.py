from random import randint
lista = randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10)
print('Os valores sorteados são: ', end='')
'''c = 0
maior = 0
menor = 10'''
for c in lista:
    print(f'{c} ', end='')
print(f'\nO maior número foi {max(lista)} ')
print(f'O menor número foi {min(lista)}')
