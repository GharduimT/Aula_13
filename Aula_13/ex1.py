# >>>>>>>>>>>>>>>>>>>>>>>>DATA FRAME - DADOS TABLARES <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#
#  É UMA ESTRUTURA DO PANDAS
# BIDIMENSIONAL
# UTLIZADA PRA TRABALHAR COM DADOS TABULARES (TABELAS)
# CADA COLUNA EM UM DATA FRAME É UMA SERIE

# pip install pandas >> para instalar um biblioteca

# um dicionário normal
# import pandas as pd

# data = {
#     'Nome': ['Ana', 'João', 'Maria'], #  lista
#     'Idade': [23, 25, 29],
#     'Gênero': ['F', 'W', 'F'],
#     'Altura': [1.70, 1.80, 1.75]
# }
# print (data)

'''Transformando o que era um dicionário numa estrutura DATA FRAME'''
import pandas as pd

data = {
    'Nome': ['Ana', 'João', 'Maria'], #  lista
    'Idade': [23, 25, 29],
    'Gênero': ['F', 'W', 'F'],
    'Altura': [1.70, 1.80, 1.75]
}
df_data = pd.DataFrame(data) #  pf_dados recebe 
print(df_data)

#Já tenho uma estrutura pronta e preciso imprimir uma coluna
#PRINT VAR QUANTT
print('\nVars Quatitativas')
print(20*'=')

#idade
print('\nExibindo Idade: ')
print(df_data['Idade'])

#Altura
print('\nExibindo Altura: ')
print(df_data['Altura'])

#Variaveis Qualitativas
#Gênero
print('\nExibindo Gênero: ')
print(df_data['Gênero'])

#Nome
print('\nExibindo Nome: ')
print(df_data['Nome'])

#>>>>>>> DATA SET | DATAFRAME<<<<<<<<<<<<<<<<<<<<<<

#SÃO COISAS DISTINTAS