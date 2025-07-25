# Importando o Pandas
import pandas as pd

# Cria um Dicionário
dados = {
    'Estado': ['Santa Catarina', 'Rio de Janeiro', 'Tocantins', 'Bahia', 'Minas Gerais'],
    'Ano': [2004, 2005, 2006, 2007, 2008],
    'Taxa Desemprego': [1.5, 1.7, 1.6, 2.4, 2.7]
}

# Importa a função DataFrame do Pandas
from pandas import DataFrame

# Converte o dicionário em um dataframe
df = DataFrame(dados)

# Reorganizando as colunas
DataFrame(dados, columns = ['Estado', 'Taxa Desemprego', 'Ano'])

print('-='*32)

# Criando outro dataframe com os mesmo dados anteriores mas adicionando uma coluna
df2 = DataFrame(dados, columns = ['Estado', 'Taxa Desemprego', 'Taxa Crescimento', 'Ano'],
                        index = ['estado1', 'estado2', 'estado3', 'estado4', 'estado5'])

# _____________________________

print(df2.head())
print('-='*32)
# Resumo estatístico do DataFrame
print(df2.describe())
print('-'*15)

print(df2.isna())
print('-'*15)
print(df2['Taxa Crescimento'].isna())
print('-='*32)

# _____________________________

# Importando o NumPy
import numpy as np

# Usando o NumPy para alimentar uma das colunas do dataframe
df2['Taxa Crescimento'] = np.arange(5.)

print(df2)
print('-'*15)
print(df2.isna())
print('-'*15)
print(df2.describe())