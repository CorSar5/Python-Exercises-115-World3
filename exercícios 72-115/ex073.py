equipas = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR', 'São Paulo', 'Internacional', 'Corinthians',
           'Fortaleza', 'Goiás', 'Bahia', 'Vasco da Gama', 'Atlético', 'Fluminense', 'Botafogo', 'Ceará',
           'Cruzeiro', 'Csa', 'Chapecoense', 'Avaí')
print('='*30)
print(f'A lista das equipas do Brasileirão: {equipas}')
print('='*30)
print(f'Os primeiros 5 são:{equipas[0:6]}')
print('='*30)
print(f'As 4 equipas que estão na última classificação são {equipas[-4:]}')
print('='*30)
print(f'As equipas em ordem alfabética são:{sorted(equipas)}')
print('='*30)
print(f'O Chapecoense está na posição: {equipas.index("Chapecoense")+1}ª')