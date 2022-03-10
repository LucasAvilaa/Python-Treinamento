# LINK https://www.youtube.com/watch?v=xMDWX83cTF8&list=PLsMpSZTgkF5ANrrp31dmQoG0-hPoI-NoX&index=5

nomes = ['Will','Aline', 'Maria', 'Cesar']
idades = [10,20,30,40]

# 1° Jeito de juntar duas listas
for i in range(len(nomes)):
    print(f"{nomes[i]} tem {idades[i]} anos")

print("\n-----------------\n")

# 2° Jeito de juntar duas listas
# .zip() junta duas listas com a mesma quantidade de indices
for nome, idade in zip(nomes,idades):
    print(f"{nome} tem {idade} anos")


print("\n-----------------\n")


# Primeiro jeito de saber a linha de um iterável
with open("teste.txt") as text:
    count = 1
    for linha in text:
        print(str(count), linha.strip()) 
        count += 1

# Segundo jeito de saber a linha de um iterável
# enumerate()
with open("teste.txt") as text:
    for count, linha in enumerate(text, start=1):
        print(str(count), linha.strip()) 

print("\n-----------------\n")

# Manipulando Dicionários no for

dicionario = {'Will': 10, "Aline": 20, "Ivone": 30}

for key, value in dicionario.items():
    print(key, value)

for value in dicionario.values():
    print(value)

for keys in dicionario.keys():
    print(keys)

    

