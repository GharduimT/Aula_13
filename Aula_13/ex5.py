import pandas as pd
import numpy as np

df = pd.read_excel('./Aula_13/vendas_roupas.xlsx')
#print(df.head(10))
print(df.describe())

categoria = df['Categoria']
quantidade_vendida = df['Unidades Vendidas']
#print(quantidade_vendida)

media =np.mean(quantidade_vendida)
mediana =np.median(quantidade_vendida)

print('Essa é a média:', media)
print('Essa é a médiana:', mediana)

#Organizar o DATAFRAME crescente por 'quatidade vendida'
quantidade_organizada = df.sort_values(by='Unidades Vendidas', ascending=False)

#print(quantidade_organizada)

print(quantidade_vendida.values)

satisfacao = df[df['Satisfação'] == 'Baixo']
print(satisfacao)