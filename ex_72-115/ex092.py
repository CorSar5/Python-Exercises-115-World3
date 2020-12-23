from datetime import datetime
dados = dict()
dados['Nome'] = str(input('Digite o seu Nome: '))
a = int(input('Ano de Nascimento: '))
dados['Idade'] = datetime.now().year - a
dados['CTPS'] = float(input('Carteira de Trabalho (0 não tem): '))

if dados['CTPS'] != 0:
    c = int(input('Ano de Contratação: '))
    dados['Contratação'] = c
    dados['Salário'] = float(input('Salário: € '))
    r = 35 - (datetime.now().year - c) + dados['Idade']
    dados['Reforma'] = r
print('=-'*30)