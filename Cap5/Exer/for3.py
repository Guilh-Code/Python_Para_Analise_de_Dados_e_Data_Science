# Soma os números pares da primeira lista com os números pares da segunda lista

lista1 = [10,16,24,39,47]
lista2 = [39, 89,47,76,12]
soma = 0

# Loop externo
for lista in [lista1, lista2]:

    # Loop interno
    for num in lista:

        # Condicional
        if num % 2 == 0:
            soma += num

print(f'A soma dos números pares das duas listas é igual a {soma}')