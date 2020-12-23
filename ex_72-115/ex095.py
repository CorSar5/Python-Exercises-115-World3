print('       ==ANÁLISE DE JOGADORES==')
print('='*40)
jogador = dict()
partidas = list()
pessoal = list()
while True:
    jogador.clear()
    partidas.clear()
    while True:
        sexo = str(input('Sexo: [M/F] ')).upper()[0]
        if sexo not in 'MF':
            print('Digite apenas M ou F!')
        elif sexo == 'M':
            jogador['Nome'] = str(input('Nome do Jogador: '))
            break
        elif sexo == 'F':
            jogador['Nome'] = str(input('Nome da Jogadora: '))
            break
    f = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
    for c in range(0, f):
        partidas.append(int(input(f'   Quantos golos marcou na {c+1}ª partida? ')))
        jogador['Golos'] = partidas[:]
        jogador['total'] = sum(partidas)
    resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
    pessoal.append(jogador.copy())
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()
        
    if resp == 'N':
        break
print('-='*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(pessoal):
    print(f'{k:>3}  ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    dados = int(input('Mostrar os dados de que jogador? '))
    if dados == 999:
        break
    if dados >= len(pessoal):
        print(f'ERRO! Não existe jogador com o código {dados}!')
    else:
        if sexo == 'M':
            print(f'--LEVANTAMENTO DO JOGADOR {pessoal[dados]["Nome"]}')
        elif sexo == 'F':
            print(f'--LEVANTAMENTO DA JOGADORA {pessoal[dados]["Nome"]}')
        for i, v in enumerate(pessoal[dados]['Golos']):
            print(f'      => No jogo {i + 1}, fez {v} golos.')
    print('-'*40)
print('<< VOLTE SEMPRE >>')
