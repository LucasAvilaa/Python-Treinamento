#Link: https://www.youtube.com/watch?v=eDWc2xv_t_M&list=PLsMpSZTgkF5ANrrp31dmQoG0-hPoI-NoX&index=3
from collections import Counter

frase = "A função irá contar a quantidade de vezes que cada caracter aparece"

def tentativa_1(frase):
    chars = []
    quantity = []
    for x in frase:
        if not x in chars:
            chars.append(x)
            quantity.append(1)
        else:
            index = chars.index(x)
            quantity[index] +=1
    d = {}
    for i in range(len(chars)):
        d[chars[i]] = quantity[i]
    return d
print("Tentativa 1: ", tentativa_1(frase))

def tentativa_2(frase):
    chars = set()
    for x in frase:
        chars.add(x)
    chars = list(chars)
    quantity = [ frase.count(x) for x in chars]

    d = {}
    for i in range(len(chars)):
        d[chars[i]] = quantity[i]
    return d
print("Tentativa 2: ", tentativa_2(frase))

def tentativa_3(frase):
    chars = list({ x for x in frase})
    quantity = [ frase.count(x) for x in chars]
    
    d = {}
    for i in range(len(chars)):
        d[chars[i]] = quantity[i]
    return d

print("Tentativa 3: ", tentativa_3(frase))

def tentativa_4(frase):
    chars = list({ x for x in frase})
    quantity = [ (x, frase.count(x)) for x in chars]
    return dict(quantity)

print("Tentativa 4: ", tentativa_4(frase))

def tentativa_5(frase):
    return dict([(x, frase.count(x)) for x in set(frase)])

print("Tentativa 5: ", tentativa_5(frase))

def tentativa_6(frase):
    return { x: frase.count(x) for x in set(frase) }

print("Tentativa 6: ", tentativa_6(frase))

def tentativa_7(frase):
    return Counter(frase)
print("Tentativa 7: ", tentativa_7(frase))
