import pandas as pd

# Primeiro importamos um dataset
dsa_df = pd.read_csv("C:/Users/Guilh/OneDrive/Documentos/Atividades Curso/Python_Para_Analise_de_Dados_e_Data_Science/Cap10/Pandas/Manipulando Arquivo em CSV/dataset.csv")
print()

# Se for necessário substituir caracteres dentro de uma string o Pandas oferece uma função para isso também.

# Por exemplo, vamos substituir 2 caracteres em uma das colunas

print(dsa_df.head())
print('-='*23)

# Substituímos os caracteres CG por AX na coluna 'ID_Cliente'
dsa_df['ID_Pedido'] = dsa_df['ID_Cliente'].str.replace('CG', 'AX')

print(dsa_df.head())

# E pronto. Fácil assim.