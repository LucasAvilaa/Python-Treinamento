#LINK - https://www.youtube.com/watch?v=FjlDonbRjpI&list=PLsMpSZTgkF5ANrrp31dmQoG0-hPoI-NoX&index=6

def loop(vezes):
    if vezes > 0:
        print("Rodando")
        loop(vezes -1)

loop(10)

def Fibonacci(n):
    if n >= 1:
        penultimo = 0
        print(penultimo)
    if n >= 2:
        ultimo = 1
        print(ultimo)
    if n >= 3:
        for i in range(n-2):
            proximo = ultimo + penultimo
            penultimo = ultimo
            ultimo = proximo
            print(proximo)
    
#Fibonacci(5)

def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

print(fib(5))
 
import json

html = """
    <div>
        <div>
            <p> Conteudo com p <a> Link </a> </p>        
        </div>
    </div>    
"""

def parser(html):
    comeco = html.index('<')
    fim = html.index('>')
    nome = html[comeco + 1:fim]
    fimTag = html.rfind(f'</{nome}>')
    conteudo = html[fim + 1:fimTag].strip()
    if '<' in conteudo:
        conteudo = parser(conteudo)
    return {'Tag': nome, "Conteúdo": conteudo}

print(json.dumps(parser(html), indent=2, ensure_ascii=False).encode('utf8').decode())
