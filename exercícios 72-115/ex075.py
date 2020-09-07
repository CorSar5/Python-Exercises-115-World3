cont= 0
conta = 0
d = k= 0
lista= ( int(input('Escreva um número: ')),
     int(input('Escreva outro número: ')),
     int(input('Escreva outro número: ')),
    int(input('Escreva um último número: ')))
print(f'Os números digitados foram: {lista}')
print(f'O número 9 apareceu {lista.count(9)} vezes.')
if 3 in lista:
    print(f'O valor 3 apareceu na {lista.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado.')
print('Os valores pares digitados foram ', end=' ')
for n in lista:
    if n % 2 == 0:
        print(f'{n} ', end=' ')