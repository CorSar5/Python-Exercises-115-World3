from ex115.lib.arquivo import *
from time import sleep


arq = 'cursoemvideo.txt'
if not arqExiste(arq):
    criarArquivo(arq)


op=0
while True:
    resposta = menu(['View Registered People', 'Log new Person', 'Delete User', 'End System'])
    # a resposta vai se tornar o return opc
    if resposta == 1:
        #opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        #opção de registrar uma pessoa
        cabecalho('NEW REGISTER ')
        nome = leiaString('Name: ')
        nome2 = leiaString('Surname: ')
        idade = leiaInt('Age: ')
        cadastrar(arq, nome, nome2, idade)
    elif resposta == 3:
        lerArquivo(arq)
        eliminar('Process that will be deleted: ', arq)
    elif resposta == 4:
        cabecalho('Ending System!')
        break
    else:
        print('\033[31mERROR! Chose an avaliable choice!\033[m')
    sleep(1.5)
