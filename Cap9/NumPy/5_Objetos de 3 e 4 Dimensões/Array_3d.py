import numpy as dsa

# Cria um array numpy de 3 dimensões
arr_3d = dsa.array([
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ],
    [
        [13, 14, 15, 16],
        [17, 18, 19, 20],
        [21, 22, 23, 24]
    ]
])

print(arr_3d)
print()

print(arr_3d.ndim)
print(arr_3d.shape)
print(arr_3d[0, 2, 1])
