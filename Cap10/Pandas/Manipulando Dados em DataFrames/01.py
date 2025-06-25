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

