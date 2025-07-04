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

# Visualiza as 5 primeiras linhas
print(df.head())

print(type(df))

# Reorganizando as colunas
print(DataFrame(dados, columns = ['Estado', 'Taxa Desemprego', 'Ano']))

print('-='*32)

# Criando outro dataframe com os mesmo dados anteriores mas adicionando uma coluna
df2 = DataFrame(dados, columns = ['Estado', 'Taxa Desemprego', 'Taxa Crescimento', 'Ano'],
                        index = ['estado1', 'estado2', 'estado3', 'estado4', 'estado5'])

print(df2)

print('-'*15)

# Imprimindo apenas uma coluna do DataFrame
print(df2['Estado'])

print('-'*15)

# Imprimindo apenas duas colunas do DataFrame
print(df2[['Taxa Desemprego', 'Ano']])

print('-'*15)
print(df2.values)
print('-'*15)
print(df2.dtypes)
print('-'*15)
print(df2.columns)
print('-'*15)
print(df2.index)
print('-'*15)
print(df2.filter(items = ['estado3'], axis = 0))
