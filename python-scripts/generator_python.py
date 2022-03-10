# LINK: https://www.youtube.com/watch?v=bjebnCnwwJg&list=PLsMpSZTgkF5ANrrp31dmQoG0-hPoI-NoX&index=4

# FORMA SEM O GERADOR
from pyparsing import string_start


a = [i for i in range(600000)]

for i in a:
    #print(i, end='')
    break

# FORMA COM O GERADOR
# SÓ MUDA DE COLCHETE PARA PARENTESES
a = (i for i in range(600000))

for i in a:
    #print(i)
    break

# NOVO ELEMENTO 'YIELD'
# O YIELD DEVOLVE UM VALOR E NÃO TERMINA A FUNÇÃO, COMO O RETURN FARIA
def gerador_infinito():
    number = 0
    while True:
        number += 1
        yield number


for i in "Teste do end":
    print(i, end=' END ')