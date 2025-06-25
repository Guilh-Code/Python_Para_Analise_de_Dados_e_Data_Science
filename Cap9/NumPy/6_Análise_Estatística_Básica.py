import numpy as dsa

# Criando um array
arr14 = dsa.array([15, 23, 63, 94, 75])

# Média
print(dsa.mean(arr14))

'''
O NumPy oferece diversas funções estatísticas para análise de dados, como:

- mean() para média
- median() para mediana
- std() para desvio padrão
- var() para variância
- min() e max() para valores mínimo e máximo
- sum() para soma total
- percentile() e quantile() para percentis e quantis

Essas funções permitem calcular medidas descritivas de forma rápida e eficiente sobre arrays NumPy.
'''

# Desvio Padrão (Standard Deviation)
print(dsa.std(arr14))

# Variância
print(dsa.var(arr14))