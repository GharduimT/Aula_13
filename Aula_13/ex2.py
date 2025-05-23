#>>>>>>> DATA SET | DATAFRAME<<<<<<<<<<<<<<<<<<<<<<
#SÃO COISAS DISTINTAS

import pandas as pd

df = pd.read_excel('./Aula_13/vendas_eletronicos.xlsx')  # é utilizado DF para identificar com maior facilidade que se trata de DATAFRAME #é necessário apresentar/informar o caminho para onde está p BD #nesse caso a raiz é a pasta CODE e dentro dela está a pasta informada e o arquivo
print(df.head(11))#caso não imforme um número específico de linhas irá imprimir 5 linhas
print(df)#vai imprimir "tudo" mas deve ser ter muito cuidado por conta do tamanho dos arquivos que serão analisados.