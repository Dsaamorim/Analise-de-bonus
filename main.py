#pandas
#openpyxl
#twilio

import pandas as pd
from twilio.rest import Client
account_sid = "AC2073fce44698665db7451f3c6cad53ec"
# Your Auth Token from twilio.com/console
auth_token  = "267037c26aceebbee873021508a9e160"
client = Client(account_sid, auth_token)

#Passo a Passo de solução

#Abrir os 6 arquivos em Excel
lista_meses = ['janeiro','fevereiro','março','abril','maio','junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx');
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} o vendedor {vendedor} bateu a meta, vendas: {vendas}');
        message = client.messages.create(
            to="+5521972875309",
            from_="+18646066182",
            body=f'No mês {mes} o vendedor {vendedor} bateu a meta, vendas: {vendas}')
        print(message.sid)

#Para cada arquivo:

#Verificar se o algum valor na coluna Vendas daquele arquivo é maior que 55.000

#Se for maior do que 55.000 -> Envia um SMS com o Nome, o mês, e as vendas do vendedor

#Caso não seja maior do que 55.000 não vai fazer nada

