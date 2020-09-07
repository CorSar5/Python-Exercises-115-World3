def funcao(jog='<desconhecido>', gol = 0):
        print(f'O jogador {jog} fez {gol} golo(s) no campeonato.')


n = str(input('Nome do Jogador(a): '))
golos = str(input('Número de Golos: '))
if golos.isnumeric():
    golos= int(golos)
else:
    golos = 0
if n.strip()== '':
    funcao(gol=golos)
else:
    funcao(n, golos)