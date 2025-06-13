# Loop em lista em listas (matrizes) para encontrar o mair número

matriz = [[42, 23, 34], [100, 215, 114], [10.1, 98.7, 12.3]]
maior_numero = 0

# Loop externo
for linha in matriz:

    # Loop interno
    for num in linha:

        # Condicional
        if num > maior_numero:
            maior_numero = num

print(f'O maior número: {maior_numero}')