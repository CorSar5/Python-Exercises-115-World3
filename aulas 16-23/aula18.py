'''teste = list()
teste.append('César')
teste.append(14)
pessoal = list()
pessoal.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
pessoal.append(teste[:])
print(pessoal)'''

'''galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade.')'''

galera = list()
dado = list()
totmai = totmen = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Existem {totmai} maiores de idade e {totmen} menores')