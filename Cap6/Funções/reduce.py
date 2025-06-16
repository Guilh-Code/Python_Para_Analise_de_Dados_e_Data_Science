# A função reduce() aplica uma função cumulativa aos itens de um iterável, reduzindo-os a um único valor.
# Ela está no módulo functools, então precisa ser importada primeiro.
from functools import reduce
from IPython.display import Image
print(Image('arquivos/reduce.png'))

# Criando uma lista
lista = [47, 11, 42, 13]
print(lista)

# Função
def soma(a, b):
    x = a + b
    return x

# Usando reduce com uma função e uma lista. A função vai retornar o valor máximo
print(reduce(soma, lista))

print('-'*25)

# Criando uma lista
lst = [47, 11, 42, 13]

# Usando a função reduce() com lambda
print(reduce(lambda x, y: x+y, lst))

# Podemos atribuir a expressão lambda a uma variável
max_find2 = lambda a,b: a if (a > b) else b

print(type(max_find2))

# Reduzindo a lista até o valor máximo, através de função criada com a expressão lambda
print(reduce(max_find2, lst))