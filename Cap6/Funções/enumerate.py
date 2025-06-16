# A função enumerate() é usada para iterar sobre um iterável (como lista, tupla ou string) acessando ao mesmo tempo o índice e o valor de cada item.

# Criando uma lista
seq = ['a', 'b', 'c']

print(enumerate(seq))
print(list(enumerate(seq)))

# Imprimindo os valores de uma lista com a função enumerate() e seus respectivos índice
for indice, valor in enumerate(seq):
    print(indice, valor)

for indice, valor in enumerate(seq):
    if indice >= 2:
        break
    else:
        print(valor)

print('-'*20)

lista = ['Marketing', 'Tecnologia', 'Business']

for i, item in enumerate(lista, start=1):
    print(f'{i}º - {item}')
    
print('-'*20)

for i, item in enumerate('Data Science Academy', start=1):
    print(f'{i}º - {item}')

print('-'*20)

for i, item in enumerate(range(10), start=1):
    print(f'{i}º - {item}')