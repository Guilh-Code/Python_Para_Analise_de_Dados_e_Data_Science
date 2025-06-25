# Importando o Pandas
import pandas as pd

dados = {
    'Estado': ['Santa Catarina', 'Rio de Janeiro', 'Tocantins', 'Bahia', 'Minas Gerais'],
    'Ano': [2004, 2005, 2006, 2007, 2008],
    'Taxa Desemprego': [1.5, 1.7, 1.6, 2.4, 2.7]
}
# ___________________________
from pandas import DataFrame

df = DataFrame(dados)

DataFrame(dados, columns = ['Estado', 'Taxa Desemprego', 'Ano'])

df2 = DataFrame(dados, columns = ['Estado', 'Taxa Desemprego', 'Taxa Crescimento', 'Ano'],
                        index = ['estado1', 'estado2', 'estado3', 'estado4', 'estado5'])
# ___________________________
import numpy as np

df2['Taxa Crescimento'] = np.arange(5.)
# ___________________________

print()
print(df2)
print('-='*32)

print(df2['estado2':'estado4'])
print('-'*15)
print(df2[ df2['Taxa Desemprego'] < 2 ])
print('-'*15)
print(df2[['Estado', 'Taxa Crescimento']])

