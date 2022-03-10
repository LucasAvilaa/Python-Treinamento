# f-string
a = 65
b = "Lucas"
# Mostra o nome e o valor da variável
print(f'Variavel {a=} Nome: {b=}')
# Outros métodos de colocar variaveis no texto
print(f'Variavel {a} Nome: {b}')
print('Variavel', a, 'Nome:', b)
print('Variavel ' + str(a), 'Nome:', b)
print('Variavel %s Nome: %s' %(a,b))