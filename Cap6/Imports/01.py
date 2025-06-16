import random

print(random.choice(['Abacate', 'Banana', 'Laranja']))

print(random.sample(range(100), 10))

import statistics

dados = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]

print(statistics.mean(dados))
print(statistics.median(dados))

import os

print(os.getcwd())
print(dir(os))