lista = ('PROGRAMAR', 'APRENDER', 'JOGAR', 'OUVIR', 'LER', 'CONHECER',
         'EMPREENDEDORISMO', 'VER', 'PALAVRA', 'COMPUTADOR',
         'TRABALHO', 'CONSTRUIR')
for pos in lista:
    print(f'\n A palavra {pos} temos ', end='')
    if 'A' in pos:
        print(f'{"a"} ', end=' ')
    if 'E' in pos:
        print(f'{"e"} ', end=' ')
    if 'I' in pos:
        print(f'{"i"} ', end=' ')
    if 'O' in pos:
        print(f'{"o"} ', end=' ')
    if 'U' in pos:
        print(f'{"u"} ', end=' ')


#solução aula


lista = ('PROGRAMAR', 'APRENDER', 'JOGAR', 'OUVIR', 'LER', 'CONHECER',
         'EMPREENDEDORISMO', 'VER', 'PALAVRA', 'COMPUTADOR',
         'TRABALHO', 'CONSTRUIR')
for pos in lista:
    print(f'\n A palavra {pos} temos ', end='')
    for letra in pos:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end= ' ')