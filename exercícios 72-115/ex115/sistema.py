from lib.arquivo import *
from lib.interface import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arqExiste(arq):
    criarArquivo(arq)


while True:
    resposta = menu(['Visualizar Pessoas Registadas', 'Registar Nova Pessoa',  'Sair do Sistema'])
    # a resposta vai se tornar o return opc
    if resposta == 1:
        #opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        #opção de registrar uma pessoa
        cabecalho(' NOVO CADASTRO ')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do Sistema... Até mais!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida\033[m')
    sleep(1.5)