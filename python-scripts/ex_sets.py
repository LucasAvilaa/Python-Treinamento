# Link: https://algoritmosempython.com.br/cursos/programacao-python/conjuntos/

#Conjuntos (sets) em Python
#Um set em Python é uma coleção de itens únicos (distintos).

# Exemplo de criação de sets.
numeros = [1, 2, 2, 3, 3, 3]
numeros_distintos = set(numeros)
print("Números: ", numeros)
print("Números distintos: ", numeros_distintos)

# Exemplo de criação de sets.
numeros = [1, 2, 2, 3, 3, 3]
numeros_distintos = set() 
for num in numeros:
    numeros_distintos.add(num) 
print("Números: ", numeros)
print("Números distintos: ", numeros_distintos)
 
# adicionando elemento no set()
x = set()
x.add(10)

# Criando uma variaval set vazia
x = set()

# Criando uma variaval set já populada
numeros = [1, 2, 2, 3, 3, 3]
x = set(numeros)

# Como remover elementos de um conjunto,
nums = set([1, 2, 2, 3, 3, 3])
nums.remove(2)
print("Números: ", nums)

""" A função remove deve ser usada somente se tivermos certeza
que o elemento está presente no conjunto, pois se o elemento
não estiver presente, a função remove causa uma exceção """


""" Uma alternativa à função remove é a função discard, que remove um elemento do conjunto se o elemento estiver presente mas não faz nada caso contrário. """

nums = set([1, 2, 2, 3, 3, 3])
nums.discard(4) 
nums.discard(2)
print(nums)
""" 
 Apesar de 4 não estar presente no conjunto, nenhum erro é retornado ao tentarmos removê-lo.
"""

""" 
remover todos os elementos de um conjunto de uma vez. Para isso precisamos usar a função clear
"""
nums = set([1, 2, 2, 3, 3, 3])
print("Números: ", nums)
nums.clear()
print("Números: ", nums)


