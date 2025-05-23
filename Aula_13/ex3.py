# média - soma de todos os valores dividido pela quantidade de 'valores'
#a media nem sempre será a melhor medida pra mostrar a variação dos dados

#>>>>>>Biblioteca Numpy<<<<<<<<<<<
import numpy as np
data_salary = [2000, 2500, 3000, 3500, 4000, 30000]

media = np.mean(data_salary)
print('Média: ', media)
# No caso acima o valor mais alto de salário (Outlier)puxa a média pra cima distorcendo o que seria um valor mais próximo de uma média real.

#MEDIANA 

#pega o dado que REALMENTE está no centro. 
# ''' 1000, 2000, 2500, 3000, 3500, 4000, 30000''' pela ORDEM CRESCENTE vai pegar o valor do meio dos sete numeros
# ''' 2000, 2500, 3000, 3500, 4000, 30000''' pela ORDEM CRESCENTE vai pegar OS VALORES do MEIO SOMA E DIVIDE

mediana = np.median(data_salary)
print('Mediana: ', mediana)# a função MEDIANA organiza os itens em ordem crescente sempre

#  se a MEDIA é maior que a MEDIANA significa que tem dados puxando pra cima e o inverso a mesma coisa.
#  se a MEDIA estiver muito maior que a mediana pode ser identificada uma assimetria o inverso a mesma coisa.

