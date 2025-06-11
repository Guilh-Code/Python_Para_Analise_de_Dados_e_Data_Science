# Exercício 2 - Crie uma lista de 5 objetos e imprima na tela

lista = []

for i in range(1, 6):
    obj = input(f'Adiciona o {i}º objeto na lista: ')
    lista.append(obj)

print(lista)