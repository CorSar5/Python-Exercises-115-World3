from ex115.lib.interface import *


def arqExiste(nome):
    try:
        a = open(nome, 'rt') #le
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')  #cria write text +
        a.close()
    except:
        print('\033[31m.Houve um ERRO na criação do arquivo!\033[m')
    else:
        print(f'File {nome} successfully created')


def lerArquivo(nome):
    c=0
    try:
        a = open(nome, 'rt')
    except:
        print('Error reading the file')
    else:
        cabecalho('\033[36mREGISTERED PEOPLE\033[m')
        for linha in a:
            dado = linha.split(';')
            dado[2] = dado[2].replace('\n', '')
            dado[2] = dado[2].replace(':','')
            dado[0] = dado[0].replace('ï¿½','é')
            c += 1
            print(f' {dado[0]:<10} {dado[1]:<15}{dado[2]:>4} years  n:{c}')


    finally:
        a.close()




def cadastrar(arq, nome='desconhecido', nome2 = 'desconhecido', idade=0):
    try:
        a = open(arq, 'at') #adicionar a de append
    except:
        print('There was an ERROR opening the file!')
    else:
        try:
            a.write(f'{nome};{nome2};{idade}:\n')
        except:
            print('There was an ERROR when writing the data!')
        else:
            print(f'New {nome} {nome2} record added')
            a.close()


def eliminar(op, arq):
    try:
        a = open(arq, 'rt')
    except:
        print('There was an error removing your Data')
    else:
        while True:
            try:
                option = int(input(op))
                if option < 0:
                    print('\033[31mERROR: please enter an existing process\033[m')
                    continue
                elif option > 115:
                    print('\033[31mERROR: please enter an existing process\033[m')
                    continue
