def area(c, l):
    print(f'A área de um terreno {c} x {l} é de {c*l}m²')

print('  Controle de Terrenos')
print('-'*30)
area(c=float(input('COMPRIMIENTO (m): ')), l=float(input('LARGURA (m): ')))


#SOLuÇÃO AULA



#def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg} x {comp} é de {a}m²')


print(' Controle de Terrenos')
print('-'* 25)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)