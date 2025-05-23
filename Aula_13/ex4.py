#O NUMPY POSSUI UM PODER COMPUTACIONAL MAIOR E MELHOR

import numpy as np

idade = np.array([35, 25, 38, 31, 45, 22, 36, 29, 40, 32])

q1 = np.quantile(idade, 0.25)
q2 = np.quantile(idade, 0.50)
q3 = np.quantile(idade, 0.75)
media = np.mean(idade)
mediana = np.median(idade)

print('Q1: ', q1)
print('Q2: ', q2)
print('Q3: ', q3)
print('Media: ', media)
print('Mediana: ', mediana)

