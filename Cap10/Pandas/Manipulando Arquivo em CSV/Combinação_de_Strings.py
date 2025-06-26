import pandas as pd

# Primeiro importamos um dataset
dsa_df = pd.read_csv("C:/Users/Guilh/OneDrive/Documentos/Atividades Curso/Python_Para_Analise_de_Dados_e_Data_Science/Cap10/Pandas/Manipulando Arquivo em CSV/dataset.csv")
print()

# A função cat() pode ser usada para concatenar strings em um dataframe do Pandas

# Vamos criar uma nova coluna concatenando as colunas "ID_Pedido" e "Segmento" com separador "-".
print(dsa_df.head())

# Concatenando strings
dsa_df['Pedido_Segmento'] = dsa_df['ID_Pedido'].str.cat(dsa_df['Segmento'], sep = '-')

print(dsa_df.head())
