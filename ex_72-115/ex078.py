valores = list()
mai = men = 0
for c in range(0,5):
    valores.append(int(input(f'Escreva um número para a posição {c}: ')))
    if c == 0:
        mai = men = valores[c]
    else:
        if valores[c] > mai:
            mai = valores[c]
        if valores[c] < men:
            men = valores[c]
print('=-'*30)
print(f'A sua lista de valores é : ', end='')
for c in valores:
  print(f'{c} ', end='')
print(f'\nO maior valor digitado foi {mai} nas posições ', end='')
for i, v in enumerate(valores):
    if v == mai:
        print(f'{i}... ', end='')
print(f'\nO menor valor digitado foi {men} nas posições ',end='')
for i, v in enumerate(valores):
    if v == men:
        print(f'{i}...', end='')