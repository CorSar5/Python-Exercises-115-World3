base = list()
dado = list()
mai = men = 0
c = ''
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(base) == 0:
        mai = men = dado[1]
    else:
        if dado[1] < men:
            men = dado[1]
        if dado[1] > mai:
            mai = dado[1]
    base.append(dado[:])
    dado.clear()
    c = str(input('Deseja continuar? [S/N]')).strip().upper()
    if c not in 'NS':
        c = str(input('Deseja continuar? [S/N]')).strip().upper()
    if c in 'N':
        break
print('='*45)
print(f'Ao todo, foram registradas {len(base)} pessoas.')
print(f'O maior peso0 foi de {mai}KG. Peso de ', end='')
for p in base:
    if p[1]== mai:
        print(f'{p[0]} ', end='')
print(f'\nO menor peso foi de {men}KG. Peso de ', end='')
for r in base:
    if r == men:
        print(f'{p[0]} ', end='')