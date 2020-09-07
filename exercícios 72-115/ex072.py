n = ('zero', 'um', 'dois', 'três', 'quatro',
     'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
     'treze', 'catorze', 'quinze', 'dezasseis ', 'dezassete', 'dezoito',
     'dezanove', 'vinte')
while True:
    d = int(input('Escreva um número de 0 a 20: '))
    if 0 <= d <= 20:
        break
    print('Tente Novamente. ', end='')
print(f'Você digitou {n[d]}')