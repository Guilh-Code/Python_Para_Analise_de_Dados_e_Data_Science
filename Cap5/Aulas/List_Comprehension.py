# Lista de Frutas
lista_frutas = ['banana', 'abacate', 'melancia', 'cereja', 'manga']

# Nova lista
nova_lista = []


# Loop tradicional para buscar as palavras com letra 'm'
for x in lista_frutas:
    if 'm' in x:
        nova_lista.append(x)

print(nova_lista)



# Mesmo resultado anterior mas com List Comprehension
nova_lista = [x for x in lista_frutas if 'm' in x]
print(nova_lista)