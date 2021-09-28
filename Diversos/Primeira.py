
# A identacao faz diferença
if(5>2):
    print("5 maior que 2")
    print("Segunda mensagem")

x,y,z = "1","2","3"
print (x)
print (y)
print (z)

x=y=z = "1"
print (x)
print (y)
print (z)


#Criacao de uma funcao com variavel global
x = "Teste"

#def é usado pra criar uma funcao

def myFunc():
    print("Teste e: "+x)

myFunc()


#Gerar numero aleatorio
import random
print(random.randrange(1,20))

#Conversao de tipos
a = 1 
print(type(a))

a = float(a)
print(type(a))

a = str(a)
print(type(a))

#Strings sao matrizes
a= "primeiro","segundo","terceiro"
print(a[2])

#Fatiamento
a="Lucas"
print(a[1:3])
print(a[0:3])


# Comentario sao feitos com #

# Metodo print() escreve algo

# indexacao negativa
#     a='Lucas'
#     print(a[-5:-4])


# Comprimento de uma string
#     print(len(variavel))

# Remover espacos em branco do comeco ou do fim
#   print(variavel.strip())

# Deixar tudo minusculo
#   print(variavel.lower())

# Maiusculo
#    print(variavel.upper())

# # Replace (Substituir)
#     print(variavel.replace("old", "new"))   

# método split() divide a string em substrings se encontrar instâncias do separador:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
print(a)

# Verificar String se tiver um determinado texto
a= "Lucas Andrade de Avila"
x= "Luc" in a    
print(x)

# Verificar String se nao tiver um determinado texto
a= "Lucas Andrade de Avila"
x= "Pato" in a    
print(x)

# Concatenar variaveis
a='lucas'
b='avila'
c= a+b
d= a + "  " + b
print(c) #Resultado = lucasavila
print(d) #Resultado = lucas   avila

# Use o format()método para inserir números em seqüências de caracteres:
#     age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))    


quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# inserindo aspas dentro de uma str *usa se \ para isso
txt = "We are the so-called \"Vikings\" from the north."
# \n new line
# \t tab
# \b backspace 
# entre outros


a='lucas andeade de avila'
print(a.rfind("a"))
a = a.replace('andeade','andrade')
print(a)


this =['lucas','andrade','ávila']
if 'andrade' in this:
        print("Sim")
else:
        print("nao")


this =['lucas','andrade','ávila']
this.aenppd("Adicionar item no ultimo lugar da fila")
print(this)


this =['lucas','andrade','ávila']
this.insert(0,"o primeiro campor é a posicao que este texto vai entrar")
print(this)

# Metodos
#     remove() Remover
#     pop()  Remove pelo indice indicado caso na indique ele removera o ultimo
#     clear() Limpa a lista
#     copy() Copiar
#     list() Tambem copia
#     reverse() Reverte a lista
#     count()
#     append() insere um item no final da lista

# del tambem remove item da lista uma parte ou o todo

# Concatenando listas 
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


# outra maneira de concatenar
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

# outra maneira de concatenar
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

# Listas - ordenada e mutavel ex ['a','b','c']
# Tuplas - ordenada e imutavel ('a','b','c')
# Conjunto - nao ordenada e nao indexada {'a','b','c'}
# dicionario - desordenda, mutavel, indexada {"Carro": "Mustang",
                                            # "Marca":"Ford",
                                            #  "Ano": 2019}

dicionario=	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = dicionario["model"]
# ou
x = dicionario.get("model")

# adicionando valor
dicionario ["COR"] = "Vermelho"

# alterando valor
x = dicionario["ano"] = 2020
print(x)

for x in dicionario:
    print(x)

for x in dicionario:
    print(dicionario[x])

for x in dicionario.values():
    print(x)

for x,y in dicionario.items():
    print(x,y)



# Dicionario aninhado

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}


a='lucas'
print(len(a))
