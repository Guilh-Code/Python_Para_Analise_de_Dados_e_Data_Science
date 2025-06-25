import pandas as pd

# Primeiro importamos um dataset
dsa_df = pd.read_csv("C:/Users/Guilh/OneDrive/Documentos/Atividades Curso/Python_Para_Analise_de_Dados_e_Data_Science/Cap10/Pandas/Preenchendo Valores Ausentes e Query de Dados no DataFrame/dataset.csv")
print()

# Checamos os valores mínimo e máximo da coluna Valor_Venda
print(dsa_df.Valor_Venda.describe())
print('-='*10)

# Geramos um novo dataframe apenas com o intervalo de vendas entre 229 e 10000
df2 = dsa_df.query('229 < Valor_Venda < 10000')

# Então confirmamos os valores mínimo e máximo
print(df2.Valor_Venda.describe())
print('-='*10)

# Geramos um novo dataframe apenas com os valores de venda acima da média
df3 = df2.query('Valor_Venda > 766')
print(df3.head())
