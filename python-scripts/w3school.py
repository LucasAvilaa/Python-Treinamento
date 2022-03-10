# LINK - https://www.w3schools.com/python/

texto = " Lucas, Avila "

print(texto.upper()) # ' LUCAS, AVILA ' -> Coloca em letra maiúscula
print(texto.lower()) # ' lucas, avila ' -> Coloca em letra minúscula
print(texto.strip()) # 'Lucas, Avila' -> Remove espaços antes e depois
print(texto.replace("Lucas", "Alterado")) #' Alterado, Avila ' -> Altera o texto 'Lucas' para 'Alterado'
print(texto.split(",")) # [' Lucas', ' Avila '] -> Quebra o texto em lista onde o caractere é o especificado

texto_min = "a primeira letra vai ficar maiúscula"
print(texto_min.capitalize()) # 'A primeira letra vai ficar maiúscula' -> Coloca a primeira letra em maiúscula

firstname = "Lucas"
lastname = "Avila"
full_name = firstname + " " +lastname
print(full_name)

# Duas maneiras de usar o format

# 1°
age = 19
txt = "My name is {1}, and I am {0}".format(age, firstname)
print(txt)

# 2°
age = 19
txt = "My name is {}, and I am {}".format(firstname, age)
print(txt)

# Caracteres de escape
print("Aspas duplas dentro de outra \"como essa\", por exemplo")
print("\nQuebra de linha")
print("\ barra invertida")
print("\\ barra invertida")
print("Não\r entendi")
print("\tTab")
print("Apaga \bespaço \bentre \btexto")
print("\f Form Feed")
print("\110\145\154\154\157") # Octal Value
print("\x48\x65\x6c\x6c\x6f") # Hex Value
