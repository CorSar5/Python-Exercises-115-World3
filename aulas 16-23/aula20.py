'''#Do Def para o Pprincipal precisa de ter 2 linhas
def lin():
    print('-' * 30)


#Programa Principal
lin()
print('   CURSO EM VÍDEO   ')
lin()
lin()
print('   APRENDA PYTHON  ')
lin()'''

'''def mensagem(msg):
    print('-'*30)
    print(msg)
    print('-' * 30)


mensagem('SISTEMA DE ALUNOS')
mensagem('APRENDA PYTHON')'''


#^^^^^^
#|||||| TEORIA

#  Prática:
'''def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A({a}) + B({b}) = {s}')


#Programa Principal
soma(a=4, b=5)
soma(b=8, a=9)  #pode se mudar a ordem
soma(2, 1)'''

#* é o sinal de desempacotar
'''def contador(*num):
    for valor in num:
        print(f'{valor} ', end='')
    print()
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')


contador(2, 1, 7)
contador(8,0)
contador(4, 4, 7, 6, 2)'''
'''def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos]*= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)'''
def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)