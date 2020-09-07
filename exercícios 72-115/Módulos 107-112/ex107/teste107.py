import ex107

p = float(input('Escreva o preço: €'))
print(f'A metade de {p} é {ex107.metade(p)}')
print(f'O dobro de {p} é {ex107.dobro(p)}')
print(f'Aumentando 10%, temos {ex107.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {ex107.diminuir(p, 13)}')