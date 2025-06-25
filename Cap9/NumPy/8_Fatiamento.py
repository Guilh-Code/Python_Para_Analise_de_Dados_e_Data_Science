import numpy as dsa

# Cria uma array
arr22 = dsa.diag(dsa.arange(3))
print(arr22)

print(arr22[1, 1])
print(arr22[1])
print(arr22[:,2])

print("-"*20)

arr23 = dsa.arange(10)
print(arr23)

# [start:end:step]
print(arr23[2:9:3])

print("-"*20)

# Cria 2 arrays
a = dsa.array([1, 2, 3, 4])
b = dsa.array([4, 2, 2, 4])

# Comparação item a item
a == b

# Comparação Global
print(dsa.array_equal(arr22, arr23))

print(arr23.min())
print(arr23.max())

# Somando um valor a cada elemento do array
print(dsa.array([1, 2, 3]) + 1.5)

print("-"*20)

# Cria um array
arr24 = dsa.array([1.2, 1.5, 1.6, 2.5, 3.5, 4.5])
print(arr24)

# Usando o método around
arr25 = dsa.around(arr24)
print(arr25)

print("-"*20)

# Criando um array
arr26 = dsa.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr26)

# O método flatten() do NumPy retorna uma cópia unidimensional (1D) da array original, ou seja, transforma uma array de qualquer dimensão em uma única linha contínua de elementos.

# "Achatando" a matriz
arr27 = arr26.flatten()
print(arr27)

print("-"*20)

# Criando um array
arr28 = dsa.array([1, 2, 3])
print(arr28)

# Repetindo os elementos de um array
print(dsa.repeat(arr28, 3))

# Repetindo os elementos de um array
print(dsa.tile(arr28, 3))

print("-"*20)

# Criando um array 
arr29 = dsa.array([5, 6])
print(arr29)

# Criando cópia do array
arr30 = dsa.copy(arr29)
print(arr30)

