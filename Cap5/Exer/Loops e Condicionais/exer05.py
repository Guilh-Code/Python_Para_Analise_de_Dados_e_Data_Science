# Exercício 6 - Crie uma variável chamada contador = 0. Enquanto counter for menor que 100, imprima os valores na tela mas quando for encontrado o valor 23, interrompa a execução do programa"

contador = 0

while contador < 100:
    print(contador, end=' ')

    if contador == 23:
        break
    contador += 1