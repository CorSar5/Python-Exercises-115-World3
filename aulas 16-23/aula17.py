#LISTAS SÃO MUTÁVEIS
lista = ['hambúrguer', 'pizza', 'sumo', 'pudim']

'''lista.append('cookie') #para adicionar elemnetos no fim da lista
lista.insert(0, 'cachorro quente')#para adicionar elementos em qualquer posição'''

'''if 'pizza' in lista:
    del lista[3] #para deletar pela posição
    lista.pop(3) #para deletar pela posição
    lista.remove('pizza') #para deletar pelo nome'''

'''valores = list(range(4,11)) #ficam todos em ordem

val =[8, 2, 5, 4, 9, 3, 0]
val.sort() #ordena todos os valores
val.sort(reverse=True) #ordena do maior para menor
len(val)'''

'''num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 5 in num:
    num.remove(5) #elimina apenas o 1º
else:
    print('Não achei o número 5')
print(num)
print(f'Essa lista tem {len(num)} elementos.')'''

'''v = list()'''
'''v.append(5)
v.append(9)
v.append(4)'''
'''for cont in range(0,5):
    v.append(int(input('Digite um valor: ')))
print(v)
for c, f in enumerate(v):
    print(f'Na posição {c} encontrei o valor {f}!')
print('Cheguei ao final da lista!')'''

a = [2, 3, 4, 7]
b = a[:] #recece uma cópia e não uma ligação !MUITO IMPORTANTE! a=b.copy()
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')