import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

lista_produtos = []

nome_produto = input('Digite o nome do produto: ').replace(' ','-')

uri = 'https://lista.mercadolivre.com.br/'
  
requisição = requests.get(uri+nome_produto)

site = BeautifulSoup(requisição.text, 'html.parser')
 
produtos = site.findAll('div', attrs={'class':'andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default'})

for produto in produtos:
    nome = produto.find('h2', attrs={'class':'ui-search-item__title'})
    
    link = produto.find('a', attrs={'class': 'ui-search-item__group__element ui-search-link'})

    Preco_inteiro = produto.find('span', attrs={'class':'price-tag-fraction'})

    Preco_centavos = produto.find('span', attrs={'class':'price-tag-cents'})
    
    if(Preco_inteiro):
        if(Preco_centavos):
            lista_produtos.append([nome.text, Preco_inteiro.text + ',' + Preco_centavos.text ,link['href']])
        else:
            lista_produtos.append([nome.text, Preco_inteiro.text + ',00' ,link['href']])
    else:        
        lista_produtos.append([nome.text, '' ,link['href']])
 
resultado = pd.DataFrame(lista_produtos, columns=['Nome do Produto','Preço do Produto', 'Link'])

diretorio = os.getcwd()
resultado.to_excel(nome_produto +'.xlsx', index=False)

print(resultado)

     