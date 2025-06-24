import numpy as dsa

# Criando uma matriz
arr9 = dsa.array([[1,2,3], [4,5,6]])
print(type(arr9))
print(arr9)
print(arr9.shape)

print('-' * 20)

# Criando uma matriz 2x3 apenas com números "1"
arr10 = dsa.ones((2,3))
print(arr10)

print('-' * 20)

# Lista de listas
lista = [[13, 81, 22], [0, 34, 59], [21, 48, 94]]

# A função matrix cria uma matriz a partir de uma lista de listas
arr11 = dsa.matrix(lista)
print(type(lista))
print(arr11)

# Formato da matriz
print(dsa.shape(arr11))

# Tamanho da matriz
print(arr11.size)

print(arr11.dtype)

print('-' * 20)

print(arr11)

# Indexação da matriz
print(arr11[2,1])

# Indexação da matriz
print(arr11[0:2,2])

# Indexação da matriz
print(arr11[1,])

# Alterando um elemento da matriz
arr11[1,0] = 100
print(arr11)

print('-' * 20)

x = dsa.array([1, 2]) # NumPy decide o tipo dos dado
y = dsa.array([1.0, 2.0]) # NumPy decide o tipo dos dado
z = dsa.array([1, 2], dtype = dsa.float64) # Forçamos um tipo de dado em particular

print(x.dtype, y.dtype, z.dtype)

print('-' * 20)

arr12 = dsa.array([[24, 76, 92, 14], [47, 35, 89, 2]], dtype = float)
print(arr12)

# O itemsize é um atributo de arrays NumPy que retorna o tamanho, em bytes, de cada elemento da array. Ele mostra quanto de memória cada item ocupa, com base no tipo de dado (dtype) utilizado.

print(arr12.itemsize)
print(arr12.nbytes)
print(arr12.ndim)