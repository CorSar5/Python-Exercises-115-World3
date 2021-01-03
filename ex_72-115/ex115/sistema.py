from ex115.lib.arquivo import *
from time import sleep


arq = 'cursoemvideo.txt'
if not arqExiste(arq):
    criarArquivo(arq)


op=0
while True:
    resposta = menu(['Visualizar Pessoas Registadas', 'Registar Nova Pessoa', 'Retirar Utilizador', 'Sair do Sistema'])
    # a resposta vai se tornar o return opc
    if resposta == 1:
        #opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resposta == 2:
        #opção de registrar uma pessoa
        cabecalho('NOVO CADASTRO')
        nome = leiaString('Nome: ')
        nome2 = leiaString('Sobrenome: ')
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, nome2, idade)
    elif resposta == 3:
        lerArquivo(arq)
        eliminar('Processo que deseja eliminar: ', arq)
    elif resposta == 4:
        cabecalho('Saindo do Sistema... Até mais!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida\033[m')
    sleep(1.5)