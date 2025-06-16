# Exercício 6 - Considerando o range de valores abaixo, use a função filter() para retornar apenas os valores negativos.

lista = [x for x in range(-5, 5)]

# Com função
def valoresNegativo(x):
    if x < 0:
        return True
    else:
        return False

print(list(filter(valoresNegativo, lista)))

# Função fantasma
print(list(filter(lambda x: x < 0, lista)))