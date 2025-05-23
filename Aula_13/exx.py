'''Você foi designado pelo setor de inteligência comercial para gerar um relatório rápido de desempenho de vendas com base na planilha vendas_eletronicos.xlsx, que contém dados sobre produtos vendidos.
Sua tarefa é:

1. Visualizar as primeiras linhas para validar, se os dados foram importados corretamente.

2. Identificar o maior e o menor valor de faturamento total, para destacar extremos de desempenho.
3. Calcular o total de unidades vendidas, a fim de medir o volume geral de vendas.
4. Calcular a média de preço por unidade, para analisar o posicionamento médio de valor dos produtos.
Essas informações serão utilizadas em uma reunião de tomada de decisão comercial, portanto organize a saída no terminal de forma clara, objetiva e profissional.'''

# MAIOR E MENOR MAX MIN
import pandas as pd

df = pd.read_excel('./Aula_13/vendas_eletronicos.xlsx')
print("\n Maior valor de faturamento total: ")
print(df['Faturamento Total (R$)'].max())

print("\n Menor valor de faturamento total: ")
print(df['Faturamento Total (R$)'].min())

# Somatorio das uniades vendidas
print("\n Somatorio das uniades vendidas: ")
print(df['Unidades Vendidas'].sum())

# Media dos preços por unidade
print("\n Media dos preços por unidade: ")
print(df['Preço por Unidade (R$)'].mean())