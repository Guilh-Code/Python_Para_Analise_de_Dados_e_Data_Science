# Exercício 4 - Crie duas funções, uma para elevar um número ao quadrado e outra para elevar ao cubo. Aplique as duas funções aos elementos da lista abaixo.
# Obs: as duas funções devem ser aplicadas simultaneamente.

def quadrado(x):
    return x ** 2

def cubo(x):
    return x ** 3

lista = [0, 1, 2, 3, 4]

print(list(map(lambda x: (quadrado(x), cubo(x)), lista)))