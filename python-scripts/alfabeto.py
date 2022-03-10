PRIMEIRO, ULTIMO = "A", "Z"

def alfabeto_fn(primeiro=PRIMEIRO, ultimo=ULTIMO, passo=1):
    
    primeiro = primeiro.upper()
    ultimo = ultimo.upper()
 

    caractere = ord(primeiro if primeiro > PRIMEIRO else PRIMEIRO)
    ultimo_caractere = ord(ultimo if ultimo < ULTIMO else ULTIMO)

    if caractere >= ultimo_caractere:
        while caractere >= ultimo_caractere:
            yield chr(caractere)
            caractere += passo

    elif caractere < ultimo_caractere:
        while caractere <= ultimo_caractere:
            yield chr(caractere)
            caractere += passo
 

a = alfabeto_fn()
print(a)

for letra in a:
    print(letra, end=' ')