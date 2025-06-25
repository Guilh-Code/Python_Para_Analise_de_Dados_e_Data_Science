import numpy as dsa

arr15 = dsa.arange(1, 10)
print(arr15)

# Soma dos elementos do array
print(dsa.sum(arr15))

# Retorna o produto dos elementos
print(dsa.prod(arr15))

# Soma acumulada dos elementos
print(dsa.cumsum(arr15))

print("-"*25)

# Cria 2 arrays 
arr16 = dsa.array([1, 2, 3])
arr17 = dsa.array([3, 2, 1])

# Soma dos arrays
arr18 = dsa.add(arr16, arr17)
print(arr18)

print("-"*25)

# Cria duas matrizes
arr19 = dsa.array([[1, 2], [3, 4]])
arr20 = dsa.array([[5, 6], [0, 7]])

print(arr19.shape)
print(arr20.shape)

print("-"*15)

print(arr19)
print(arr20)

print("-"*25)

# Multiplicar as duas matrizes
arr21 = dsa.dot(arr19, arr20)
print(arr21)

arr21 = arr19 @ arr20
print(arr21)
