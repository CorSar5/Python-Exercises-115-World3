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
        a = open(nome, 'wt+')  #cria write text +
        a.close()
    except:
        print('\033[31m.Houve um ERRO na criação do arquivo!\033[m')
    else:
        print(f'Arquivo {nome} criado com sucesso')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabecalho('\033[36mPESSOAS REGISTRADAS\033[m')
        for linha in a:
            dado = linha.split(';')
            dado[2] = dado[2].replace('\n','')
            dado[0] = dado[0].replace('ï¿½','é')
            print(f'{dado[0]:<10} {dado[1]:<15}{dado[2]:>4} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', nome2 = 'desconhecido', idade=0):
    try:
        a = open(arq, 'at') #adicionar a de append
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{nome2};{idade}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} {nome2} adicionado')
            a.close()


'''def eliminar(arq, nome='desconhecido, idade = 0'):
    try'''
