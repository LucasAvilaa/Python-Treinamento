quantidade = int(input('Digite o valor de n: '))

i = 1

while quantidade >= i:
    numeros = range(100)
    for x in numeros:
        if x % 2 != 0:  
            if(quantidade >= i):
                print(x) 
                i += 1 