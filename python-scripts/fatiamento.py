# Link - https://www.youtube.com/watch?v=kw88FTqG8Wo&list=PLsMpSZTgkF5ANrrp31dmQoG0-hPoI-NoX&index=9

a = [1,2,3,4,5,6,7,8,9]

print(a[0]) # Pega o primeiro item de uma lista
print(a[0:4]) # Pega o primeiro até o 4° item da lista
print(a[:4]) # Pega o primeiro até o 4° item da lista
print(a[4:]) # Pega do 4° até o final da lista
print(a[-1]) # Pega o ultimo elemento da lista
print(a[:]) # Pega a lista inteira
print(a) # Pega a lista inteira
print(a[::2]) # Pega o primeiro item e vai pulando de 2 em 2
print(a[::-1]) # Inverte a lista

palavra = "radar"

print(palavra, 'É palindromo' if palavra == palavra[::-1] else 'Não é palindromo')
