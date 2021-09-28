import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time 

lista_hospedagem = []

option = Options()
# option.add_argument('--headless')
# option.add_argument('window-size=400,700') 

driver = webdriver.Chrome(executable_path="./chromedriver.exe", options=option)

driver.get('https://www.airbnb.com.br')
time.sleep(1)

destino = driver.find_element_by_class_name('_1xq16jy')
destino.send_keys('São Paulo')
destino.submit()
time.sleep(3)

conteudo = driver.page_source

site = BeautifulSoup(conteudo, 'html.parser')
hospedagens = site.findAll('div', attrs={'class': '_8ssblpx'})

for hospedagem in hospedagens:
    hospedagem_name = hospedagem.find('meta', attrs={'itemprop':'name'})
    hospedagem_url = hospedagem.find('meta', attrs={'itemprop':'url'})
    hospedagem_valor = hospedagem.find('span', attrs={'class':'_krjbj'})
    Lugares = hospedagem.find_all('span', attrs={'class':'_3hmsj'})
    hospedagem_lugares = ' '.join([detalhe.text for detalhe in Lugares])
     
    if (hospedagem_name != None): hospedagem_name = hospedagem_name['content'] 
    if (hospedagem_url != None): hospedagem_url= hospedagem_url['content'] 
    if (hospedagem_valor != None): hospedagem_valor = hospedagem_valor.text

    lista_hospedagem.append([hospedagem_name,hospedagem_lugares, hospedagem_url, hospedagem_valor])
    
    print('Nome da Hospedagem:',hospedagem_name, '\n',hospedagem_lugares,'\n', hospedagem_url,'\n', hospedagem_valor)

driver.quit() 