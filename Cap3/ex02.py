numeros = [7, 5, 10, 2, 27, 19, 4, 1]

def bubble_sort(lista):  # Define a função que recebe uma lista como parâmetro
    n = len(lista)  # Armazena o tamanho da lista

    for i in range(n):  # Laço externo que controla o número de passagens
        trocou = False  # Flag para verificar se houve alguma troca nesta passagem

        for j in range(0, n - i - 1):  # Laço interno que percorre a lista até a parte não ordenada

            if lista[j] > lista[j + 1]:  # Compara elementos adjacentes
                # Troca os elementos de lugar se estiverem fora de ordem

                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True  # Marca que houve uma troca

        if not trocou:  # Se nenhuma troca foi feita, a lista já está ordenada
            break  # Sai do laço externo antes do final para otimizar

    return lista  # Retorna a lista ordenada

print(bubble_sort(numeros))