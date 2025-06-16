# Exercício 3 - Calcule a matriz transposta da matriz abaixo.

matrix = [
    [1,2],
    [3,4],
    [5,6],
    [7,8]
    ]

transposta = [list(coluna) for coluna in zip(*matrix)]

print(transposta)