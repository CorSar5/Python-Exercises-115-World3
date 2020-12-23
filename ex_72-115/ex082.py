num = list()
b = list()
c = list()
r = ''
while True:
    num.append(int(input('Digite um número: ')))
    r = str(input('Quer continuar? [S/N] ')).strip().upper()
    while r not in 'NS':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()
    if r == 'N':
        break
for d in num:
    if d % 2 == 0:
        b.append(d)
    elif d % 2 == 1:
        c.append(d)
print('='*45)
print(f'A lista completa é {num}')
print(f'A lista de pares é {b}')
print(f'A lista de ímpares é {c}')