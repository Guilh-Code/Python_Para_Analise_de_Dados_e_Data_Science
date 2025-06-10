numeros = list(range(1, 101))

'''for numero in numeros:
    if numero % 2 == 0 and numero % 4 == 0:
        print(numero)'''

# List Comprehension
pares_div4 = [numero for numero in numeros if numero % 2 == 0 and numero % 4 == 0]

print(pares_div4)