import numpy as dsa

# Array criado a partir de uma lista Python
arrl = dsa.array([10, 21, 32, 43, 48, 15, 76, 57, 89])
print(arrl)

# Imprimindo um elemento epecífico no array
print(arrl[4])

# Indexeção
print(arrl[1:4])

# Indexação
print(arrl[1:4+1])

# Cria uma lista de índices
indices = [1, 2, 5, 6]

# Imprimindo os elementos dos índices
print(arrl[indices])

# Cria uma máscara booleana para os elementos pares
mask = (arrl % 2 == 0)
print(arrl[mask])

# Alterando um elemento do array
arrl[0] == 100
print(arrl)

# Não é possível incluir elemento do outro tipo
try:
    arrl[0] = "Novo elemento"
except:
    print("Operação não permitida!")