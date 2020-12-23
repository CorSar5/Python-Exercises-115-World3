ficha = list()
while True:
    nome = str(input('Nome: ')).strip()
    nota1 = float(input('1ª Nota: '))
    nota2 = float(input('2ª Nota: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
    while resp != 'S' and resp != 'N':
        print('Você digitou um número invalido, repita! ', end='')
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print('=-' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*35)
    p = int(input('Quer aceder às notas de qual aluno? (999 encerra): '))
    if p == 999:
        print('ENCERRANDO...')
        break
    if p <= len(ficha) - 1:
        print(f'Notas de {ficha[p] [0]} são {ficha[p][1]}')
print('<<< VOLTE SEMPRE >>>')
