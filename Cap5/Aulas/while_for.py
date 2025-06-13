# Encontrando números primos entre 2 e 30 usando loop for e while

primos = []

# Loop for para percorrer de 2 a 30
for num in range(2, 31):

    # Variável de controle
    eh_primo = True

    # Loop while para verificar se o número é primo
    i = 2
    while i <= num // 2:
        if num % i == 0:
            eh_primo = False
            break
        i += 1

    # Adicionando o número primo na lista
    if eh_primo:
        primos.append(num)

print(primos)