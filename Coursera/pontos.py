import math

x1 = int(input('Digite o primeiro número (x1): '))
y1 = int(input('Digite o primeiro número (y1): '))
x2 = int(input('Digite o segundo número (x2): '))
y2 = int(input('Digite o segundo número (x2): '))

distancia = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 ) 

if(distancia >= 10):
    print('longe')
else:
    print('perto')

