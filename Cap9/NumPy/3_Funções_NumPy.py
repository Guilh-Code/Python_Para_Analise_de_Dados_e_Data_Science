import numpy as dsa

# A função array() cria um array NumPy
arr2 = dsa.array([1, 2, 3, 4, 5])
print(arr2)

# Verificando o tipo do objeto
print(type(arr2))

# Digite . e pressione a tecla Tab no seu teclado para visualizar os métodos disponíveis em objetos Numpy
# arr2.

# Usando métodos do array numpy
print(arr2.cumsum())
print(arr2.cumprod())

print('-' * 20)

# Digite . e pressione a tecla Tab no seu teclado para visualizar as funções para manipular objetos em objetos Numpy
# dsa.

# A função arange cria um array NumPy contendo uma progessão aritmética a partir de um intervalo - start, stop, step
arr3 = dsa.arange(0, 50, 5)
print(arr3)

# Verificando o tipo do objeto
print(type(arr3))

# Formato do array
print(dsa.shape(arr3))
print(arr3.dtype)

print("-"*20)

# Cria um array preenchido com zeros
arr4 = dsa.zeros(10)
print(arr4)

print("-"*20)

# Retorna 1 nas posições em diagonal e 0 no restante
arr5 = dsa.eye(3)
print(arr5)

print("-"*20)

# Os valores passados como parâmetro, formam uma diagonal
arr6 = dsa.diag(dsa.array([1, 2, 3, 4]))
print(arr6)

print("-"*20)

# Array de valores booleanos
arr7 = dsa.array([True, False, False, True])
print(arr7)

print("-"*20)

# Array de strings
arr8 = dsa.array(["Linguagem Python", "Linguagem R", "Linguagem Julia"])
print(arr8)

print("-"*20)

# A função linspace() do NumPy gera uma sequência de números igualmente espaçados dentro de um intervalo definido. Ela permite especificar o número de pontos desejados, incluindo por padrão o valor inicial e o final do intervalo. É útil para criar distribuições uniformes de valores.
print("Função linspace()\n")
print(dsa.linspace(0, 10))
print(dsa.linspace(0, 10, 15))
print()

# A função logspace() do NumPy gera uma sequência de números espaçados logaritmicamente, ou seja, distribui os valores de forma que os logaritmos (geralmente na base 10) estejam igualmente espaçados. Ela é usada para criar escalas logarítmicas, definindo os limites do expoente inicial e final e a quantidade de pontos desejada.
print("Função logspace()\n")
print(dsa.logspace(0, 5, 10))