# A função map() em Python é usada para aplicar uma função a cada item de um iterável (como uma lista), retornando um novo iterador com os resultados.

# Função Python que retorna um número ao quadrado
def potencia(x):
    return x ** 2

numeros = [1, 2, 3, 4, 5]

numeros_ao_quadrado = list(map(potencia, numeros))

print(numeros_ao_quadrado)

print('-' * 25)

# Criando duas funções

# Função 1 - Recebe uma temperatura como parâmetro e retorna a temperatura em Fahrenheit
def fahrenheit(T):
    return ((float(9)/5)*T + 32)

# Função 2 - recebe uma temperatura como parâmetro e retorna a temperatura em Celsius
def celsius(T):
    return ((float(5)/9)* (T-32))

# Criando uma lista
temperaturas = [0, 22.5, 40, 100]

# Aplicando a função a cada elemento da lista de temperaturas.
# Em python 3, a função map() retornar um iterator
print(map(fahrenheit, temperaturas))

# Função map() retornando a lista de temperaturas convertidas em Fahrenheit
print(list(map(fahrenheit, temperaturas)))

# Usando um loop for para imprimir o resultado da função map()
for temp in map(fahrenheit, temperaturas):
    print(temp)

print('-' * 25)

# Convertendo para Celsius
print(map(celsius, temperaturas))
print(list(map(celsius, temperaturas)))

print('-' * 25)

# Usando expressão lambda
print(map(lambda x: (5.0/9)*(x - 32), temperaturas))
print(list(map(lambda x: (5.0/9)*(x - 32), temperaturas)))

print('-' * 25)

#Somando os elementos de 2 listas
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

print(list(map(lambda x,y: x+y, a, b)))

# Somando os elementos de 3 listas
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
c = [9, 10, 11, 12]

print(list(map(lambda x, y, z: x + y + z,  a, b, c)))
