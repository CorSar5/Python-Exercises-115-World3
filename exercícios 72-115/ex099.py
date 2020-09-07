from time import sleep


def maior(*num):
    cont = maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for v in num:
        print(f'{v} ', end='')
        sleep(1/4)
        if cont == 0:
            maior = v
        else:
            if v > maior:
                maior = v
        cont += 1
    print(f'Foram informados ao todo {len(num)} números.')
    print(f'O maior valor informado foi {maior}.')


maior(7, 8, 9, 4, 2)
maior(2, 6, 3)
maior(5, 6)
maior(1)
maior()