import pandas as pd

# Primeiro importamos um dataset
dsa_df = pd.read_csv("C:/Users/Guilh/OneDrive/Documentos/Atividades Curso/Python_Para_Analise_de_Dados_e_Data_Science/Cap10/Pandas/Manipulando Arquivo em CSV/dataset.csv")
print()

# O Pandas oferece diversas funções para a manipulação de strings. Começaremos com o filtros de strings nas letras iniciais e finais.

print(dsa_df.head())
print('-='*23)

# Filtramos o dataframe pela coluna Segmento com valores que iniciam com as letras 'Con'
print(dsa_df[dsa_df.Segmento.str.startswith('Con')].head())
print('-='*23)
print(dsa_df.Segmento.value_counts())
print('-='*23)

# Filtramos o dataframe pela coluna Segmento com valores que terminam com as letras 'mer'
print(dsa_df[dsa_df.Segmento.str.endswith('mer')].head())

# As funções startswith() e endswith() são muito úteis quando for necessário filtrar strings por caracteres que apareçam no começo e/ou final.