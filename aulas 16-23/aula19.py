'''dados = dict()
dados = {'nome':'Pedro', 'idade':25}
print(dados['idade'])
dados['sexo']='M'''


'''print(dic.values()) #informação
print(dic.keys())  #nome do espaço
print(dic.items()) #tudo'''

'''for k, v in film.items():
    print(f'O {k} é {v}')'''

'''pessoas = {'nome':'César', 'sexo':'M', 'idade':14}
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"] } anos.')
print(pessoas.values())
print(pessoas.items())
pessoas['peso'] = '75'
for k, v in pessoas.items():
    print(f'{k} = {v}')'''
'''brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(estado2)
print(brasil[0]['uf'])
print(brasil)'''

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    print(e)

for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')

for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()