# A função zip() combina elementos de dois (ou mais) iteráveis, empacotando-os em tuplas, um de cada por posição.

# Criando duas listas
x = [1,2,3]
y = [4,5,6]

# Unindo as listas. Em Pyhton3 retorna um iterator
print(zip(x, y))

# Perceba que zip retorna tuplas. Neste caso, uma lista de tuplas
print(list(zip(x, y)))

print('-'*25)

# Atenção quando as sequências tiverem número diferente de elementos
print(list(zip('ABCD', 'xy')))

# Criando duas listas
a = [1,2,3]
b = [4,5,6,7,8]
print(list(zip(a, b)))

print('-'*25)

# Criando 2 dicionários
d1 = {'a': 1, 'b': 2}
d2 = {'c': 4, 'd': 5}

# Zip vai unir as chaves
print(list(zip(d1, d2)))

# Zip pode unir os valores (itens)
print(list(zip(d1, d2.values())))

# Criando uma função para trocar valores entre 2 dicionários
def trocaValores(d1, d2):

    dicTemp = {}

    for d1key, d2val in zip(d1, d2.values()):
        dicTemp[d1key] = d2val

    return dicTemp

print(trocaValores(d1, d2))