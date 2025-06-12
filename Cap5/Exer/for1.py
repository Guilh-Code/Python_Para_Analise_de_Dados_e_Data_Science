# Loops aninhados
lista1 = [0, 1, 2, 3, 4, 5]
lista2 = [1, 2, 3]

# Loop externo
for elementos_lista1 in lista1:

    # Loop interno
    for elemento_lista2 in lista2:

        print(f'\n{elementos_lista1 * elemento_lista2}')

    print('-----')
