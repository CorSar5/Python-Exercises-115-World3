matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
p = d = m =0
for l in range(0,3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            p += matriz[l][c]
        '''if c == 2:
            d += matriz[l][c]'''
print('=-' * 40)
for l in range(0, 3):
    for c in range(0, 3):
        print(f' [ {matriz[l] [c]:^5} ]', end='')
    print()
print('=-' * 40)
print(f'A soma dos valores pares é {p}')
for l in range(0,3):
    d += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {d}')
for c in range(0, 3):
    if c == 0:
        m = matriz[1][c]
    elif matriz[1][c] > m:
        m = matriz[1][c]
print(f'O maior valor da 2ª linha é {m}')