import pandas as pd
from twilio.rest import Client 
# passo a passo de solução
account_sid = '**' 
auth_token = '**' 
client = Client(account_sid, auth_token) 
 
# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(mes+'.xlsx')
    if(tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000,'Vendas'].values[0]

        message = client.messages.create(  
                messaging_service_sid='**', 
                body=f'No mês de {mes} o vendedor {vendedor} vendeu R$l {vendas}',      
                to='**' 
            ) 
        
        print(message.sid)
# Para cada arquivo:

# Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55.000

# Se for maior do que 55.000 -> envia um SMS com o Nome, o mês e as vendas do vendedor


