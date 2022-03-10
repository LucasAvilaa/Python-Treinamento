# Lista tradicional
lista = []
for x in range(1,11):
    lista.append(x)
print(lista)

# List Comprehension
lista2 = [x for x in range(1,11)]
print(lista2)

# List Comprehension em uma str e invertendo a palavra com [::-1]
lista3 = [x for x in "Lucas"]
print(lista3[::-1])
