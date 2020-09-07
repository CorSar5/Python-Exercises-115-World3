lista = []
p = ''
while True:
    lista.append(int(input('Digite um número: ')))
    p = str(input('Quer continuar? [S/N] ')).strip().upper()
    while p not in 'SN':
        print('Resposta Inválida. ', end='')
        p = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if p == 'N':
        break
print('='*30)
lista.sort(reverse=True)
print(f'A lista em ordem decrescente é {lista}')
print(f'Foram digitado {len(lista)} números.')
if 5 in lista:
    print('O número 5 foi digitado na lista.')
else:
    print('O número 5 não foi digitado.')