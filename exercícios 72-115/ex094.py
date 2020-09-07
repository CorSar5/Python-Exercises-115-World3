info = dict()
pes = list()
cp = 0
ti = 0
soma = 0
while True:
    info.clear()
    info['Nome'] = str(input('Nome: '))
    info['Sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
    while info['Sexo'] not in 'MF':
        info['Sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
    info['Idade'] = int(input('Idade: '))
    soma += info['Idade']
    pes.append(info.copy())
    op = str(input('Deseja continuar? [S/N] ')).strip().upper()
    while op not in 'SN':
        op = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if op == 'N':
        break
print('-='*25)
print(f'-Ao todo temos {len(pes)} pessoas.')
media = soma / len(pes)
print(f'-A média de idade é de {media:5.2f} anos.')
print('-As mulheres cadastradas foram', end='')
for p in pes:
    if info['Sexo'] == 'F':
        print(f'{p["nome"]} ',end='')
print('-Lista das pessoas que estão acima da média: ', end='')
for p in pes:
    if p['Idade'] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')