numero = int(input('Digite um número inteiro: '))

tamanho_numero = len(str(numero))
# print('tamanho',tamanho_numero)
multiplicador = 10
soma = 0
i = 1

while tamanho_numero >= i:  
    temp = str(numero % multiplicador)
    # print(numero % multiplicador)
    soma += int(str(temp)[0])
    # print(soma)
    multiplicador *= 10   
    i += 1
print(soma)