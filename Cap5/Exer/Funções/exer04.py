# Crie uma função que receba um argumento formal e uma possível lista de elementos. Faça duas chamadas à função, com apenas 1 elemento e na segunda chamada com 4 elementos

def mostrar_elementos(nome, *elementos):
    print(f'Nome: {nome}')
    print('Elementos recebidos: ')

    for item in elementos:
        print(f'- {item}')

mostrar_elementos('Guilherme', 'Banana')
print()
mostrar_elementos('Guilherme', 'Melão', 'Abacate', 'Geleia', 'Queijo')