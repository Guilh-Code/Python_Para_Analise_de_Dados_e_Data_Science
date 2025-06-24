# Importando o NumPy
import numpy as dsa

# __________

# Criando Arrays NumPy

# Array criado a partir de uma lista Python
arrl = dsa.array([10, 21, 32, 43, 48, 15, 76, 57, 89])
print(arrl)

# um objeto do tipo ndarray é um recipiente multidimensional de itens do mesmo tipo e tamanho
print(type(arrl))

# Verificando o formato do array
print(arrl.shape)

''' Uma array no NumPy é uma estrutura de dados eficiente e multidimensional usada para armazenar e manipular conjuntos de dados numéricos de forma rápida e otimizada.

O NumPy oferece:

- Arrays multidimensionais eficientes (ndarray)
- Operações matemáticas e estatísticas vetorizadas
- Funções para álgebra linear, transformadas de Fourier e números aleatórios
- Ferramentas para manipulação de formas e dados
- Alto desempenho com uso de implementações em C

É uma base fundamental para computação numérica em Python.
'''