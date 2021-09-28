import time
import requests
import pandas as pd 
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json

# 1. Pegar conteúdo HTML a partir da URL
url = "https://www.nba.com/stats/players/traditional/?sort=W&dir=-1" 
 
driver = webdriver.Chrome(executable_path=r"D:\GoogleDrive\Documentos\PESSOAL\PYTHON\BaterPonto\chromedriver.exe") 

driver.get(url)
time.sleep(10)

driver.find_element_by_xpath("//div[@class='nba-stat-table']//table//thead//tr//th[@data-field='PTS']").click()

element = driver.find_element_by_xpath("//div[@class='nba-stat-table']//table")
html_content = element.get_attribute('outerHTML')

# 2. Parsear o conteúdo HTML - BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find(name='table')

# 3. Estruturar conteúdo em um Data Frame - Pandas
df_full = pd.read_html(str(table))[0].head(10)
df = df_full[['Unnamed: 0', 'PLAYER', 'TEAM', 'PTS']]
df.columns = ['pos', 'player', 'team', 'total']
 
# 4. Transformar os Dados em um Dicionário de dados próprio
top10ranking ={}
top10ranking['points'] = df.to_dict('records')

print(top10ranking['points'])

driver.quit()
# 5. Converter e salvar em um arquivo JSON
js = json.dumps(top10ranking)
fp = open('ranking.json', 'w')
fp.write(js)
fp.close()


