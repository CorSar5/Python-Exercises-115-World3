def escreva(msg):
    print('-' * 20)
    print(msg)
    print('-' * 20)


escreva(f'{"Olá, Mundo!":^20}')


#Solução da Aula


#def escreva(msg):
    tam = len(msg) + 4
    print('-'*tam)
    print(f'  {msg}')
    print('-'*tam)