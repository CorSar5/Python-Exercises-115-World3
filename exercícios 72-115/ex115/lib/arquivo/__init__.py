from ex115.lib.interface import *


def arqExiste(nome):
    try:
        a = open(nome, 'rt') #le
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

##
def criarArquivo(nome):
    try:
        number = nome.length
        a = open(number, nome, 'wt+')  #cria write text +
        a.close()
    except:
        print('\033[31m.Houve um ERRO na criação do arquivo!\033[m')
    else:
        print(f'Arquivo {nome} criado com sucesso')