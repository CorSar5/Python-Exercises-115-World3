from utilidades.moeda import moeda
from utilidades.dado import dado

p = dado.leiaDinheiro('Digite o preço: € ')
moeda.resumo(p, 22, 15)