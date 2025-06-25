# A função fillna() do Pandas serve para preencher valores ausentes (NaN) em um DataFrame ou Series. Ela permite substituir esses valores por um número, texto ou até por métodos como o valor anterior ou seguinte. É muito usada na limpeza de dados para evitar erros em análises.

import pandas as pd

# Primeiro importamos um dataset
dsa_df = pd.read_csv("C:/Users/Guilh/OneDrive/Documentos/Atividades Curso/Python_Para_Analise_de_Dados_e_Data_Science/Cap10/Pandas/NumPy e Pandas para Manipulação de Dados/dataset.csv")

print(dsa_df.head(5))
print('-='*32)

print(dsa_df.isna().sum())
print('-='*12)

# Extraímos a moda da coluna Quantity
moda = dsa_df['Quantidade'].value_counts().index[0]

# A Moda, em estatística, é o valor que mais se repete em um conjunto de dados. Ela indica a frequência dominante e pode ser usada tanto com dados numéricos quanto categóricos. Diferente da média e da mediana, a moda pode ter mais de um valor (multimodal) ou nenhum, se não houver repetições. É especialmente útil para identificar padrões comuns em uma amostra.

print(moda)

# E por fim preenchemos os valores NA com a moda
dsa_df['Quantidade'].fillna(value = moda, inplace = True)

print(dsa_df.isna().sum())