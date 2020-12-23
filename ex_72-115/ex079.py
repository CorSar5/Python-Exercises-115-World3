lista = list()
c = ' '
while True:
    n = (int(input('Digite um número: ')))
    if n not in lista:
        print('Valor adicionado com sucesso!')
        lista.append(n)
    else:
        print('Valor duplicado! Não vou adicionar.')
    c = str(input('Deseja Continuar?[S/N] ')).upper().strip()
    if c not in 'SN':
        print('Digitou Incorretamente a letra.', end='')
        c = str(input(' Quer continuar?[S/N] ')).upper().strip()
    if c == 'N':
        break
print('='*30)
lista.sort()
print(f'A lista é : {lista}')