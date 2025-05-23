#imobiiliária

import numpy as np

sold_houses = np.array([150.000, 180.000, 200.000, 220.000, 250.000, 280.000, 300.000, 320.000, 400.000, 1.500000])

media = np.mean(sold_houses)
mediana = np.median(sold_houses)

print('O valor médio de casas vendidas é: ', media)
print('O valor Mediano de casas vendidas é: ', mediana)
print('O valor mediano é o que melhor se enquadra no que se entende por "Valor típico" das vendas pois representa ' )