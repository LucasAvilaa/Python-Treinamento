import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_noticias = []

resposta = requests.get('https://g1.globo.com')

conteudo = resposta.content

conversao = BeautifulSoup(conteudo, 'html.parser')

noticias = conversao.findAll('div', attrs={'class': 'feed-post-body'})

for noticia in noticias:
    # Título
    titulo = noticia.find('a', attrs={'class': 'feed-post-link'})
    
    # SubTitulo
    subtitulo = noticia.find('div', attrs={'class': 'feed-post-body-resumo'})
    
    if(subtitulo):
        #print('\nTítulo: ', titulo.text, '\nSubtitulo: ', subtitulo.text, '\n')
        lista_noticias.append([titulo.text, subtitulo.text, titulo['href']])    
    else:
         #print('\nTítulo: ', titulo.text)
        lista_noticias.append([titulo.text, '' , titulo['href']])    
  
news = pd.DataFrame(lista_noticias, columns=['Titúlo','Subtítulo','Link'])

news.to_excel('Noticias G1.xlsx', index=False)

#print(news)
