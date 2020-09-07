dados = dict()
dados['Nome'] = str(input('Nome: '))
n = float(input(f'Média de {dados["nome"]}: '))
dados['Média'] = n
if n < 9.5:
    dados['Situação'] = 'Reprovado'
else:
    dados['Situação'] = 'Aprovado'
for k, v in dados.items():
    print(f'{k} é igual a {v}')