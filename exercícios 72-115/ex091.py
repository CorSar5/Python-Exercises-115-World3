from random import randint
from time import sleep
from operator import itemgetter
jogo = dict()
print('Valores Sorteados: ')
jogo['jogador_1'] = randint(1, 6)
jogo['jogador_2'] = randint(1, 6)
jogo['jogador_3'] = randint(1, 6)
jogo['jogador_4'] = randint(1, 6)
ranking = list()
for k, v in jogo.items():
    print(f'       O {k} tirou {v}')
    sleep(1)
print('Ranking dos Jogadores: ')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'       {i+1}º lugar: {v[0]} com {v[1]} ')
    sleep(1)
