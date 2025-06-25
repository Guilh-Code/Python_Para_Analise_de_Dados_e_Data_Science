import pandas as pd

# Primeiro importamos um dataset
dsa_df = pd.read_csv("C:/Users/Guilh/OneDrive/Documentos/Atividades Curso/Python_Para_Analise_de_Dados_e_Data_Science/Cap10/Pandas/Preenchendo Valores Ausentes e Query de Dados no DataFrame/dataset.csv")
print()

# Primeiro usaremos o operador lógico AND para checar duas condições. Serão retornados os registros quando as duas condições forem verdadeiras.

# Filtrando as vendas que ocorreram para o segmento de Home Office e na região South
print(dsa_df[ (dsa_df.Segmento == 'Home Office') & (dsa_df.Regiao == 'South') ].head())
print('-='*32)

# Mas pode ser necessário checar duas condições e retornar os registros se pelo menos uma for verdadeira. Nesse caso usamos o operador OR, conforme abaixo.

# Filtrando as vendas que ocorreram para o segmento de Home Office e na região South
print(dsa_df[ (dsa_df.Segmento == 'Home Office') | (dsa_df.Regiao == 'South') ].tail())
print('-='*32)

# O operador de negação é o contrário do primeiro exemplo.

# Filtrando as vendas que não ocorreram para o segmento de Home Office e nem na região South
print(dsa_df[ (dsa_df.Segmento != 'Home Office') & (dsa_df.Regiao != 'South') ].sample(5))
