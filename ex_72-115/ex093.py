print('       ==ANÁLISE DE JOGADORES==')
print('='*40)
jogador = dict()
partidas = list()
jogador['Nome'] = str(input('Nome do Jogador: '))
f = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for c in range(0, f):
    partidas.append(int(input(f'   Quantos golos marcou na {c+1}ª partida? ')))
    jogador['Golos'] = partidas[:]
jogador['total'] = sum(partidas)
print('='*40)
print(jogador)
print('='*40)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('='*40)
print(f'O jogador {jogador["Nome"]} jogou {f} partidas.')
for i, v in enumerate(jogador['Golos']):
    print(f'      => Na partida {i}, fez {v} golos.')
print(f'Foi um total de {jogador["total"]} golos.')