# Exercício 3 - Crie uma função que receba como parâmetro uma lista de 4 elementos, adicione 2 elementos a lista e imprima a lista

frutas = ['Melância', 'Caju', 'Laranja', 'Goiaba']

def Adicionar_Elemento(lista):
    lista.append('Maça')
    lista.append('Banana')
    print(lista)

Adicionar_Elemento(frutas)