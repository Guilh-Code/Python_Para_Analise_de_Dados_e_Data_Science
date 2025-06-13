# Exercício 9 - Crie uma list comprehension que imprima as palavras com a letra a no nome\n",


palavras = ["maça", "coiote", "banana", "terreno", "Python"]

lista_nova = [x for x in palavras if 'a' in x]
print(lista_nova)