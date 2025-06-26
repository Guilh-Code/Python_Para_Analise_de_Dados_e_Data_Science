import pandas as pd

# Primeiro importamos um dataset
dsa_df = pd.read_csv("C:/Users/Guilh/OneDrive/Documentos/Atividades Curso/Python_Para_Analise_de_Dados_e_Data_Science/Cap10/Pandas/Manipulando Arquivo em CSV/dataset.csv")
print()

# Com Pandas podemos realizar diversas tarefas de split de strings dividindo uma coluna ou extraindo elementos do nosso interesse. Vamos ao exemplo!

print(dsa_df.head())
print('-='*23)

print(dsa_df['ID_Pedido'].head())
print('-='*23)

''' 
Este é o formato dos dados da coluna "ID_Pedido".

    - CA-2016-152156
    - US-2015-108966

Temos o país, o ano e o id do pedido. Vamos dividir essa coluna e extrair o ano para gravar em uma nova coluna.
'''

# Split da coluna pelo carcter '-'
print(dsa_df['ID_Pedido'].str.split('-'))
print('-='*23)

# Observe que o resultado são as listas em Python. Para extrair o ano precisamos especificar o índice da posição que queremos extrair (em nosso caso a posição 2, logo, índice 1 em Python):

print(dsa_df['ID_Pedido'].str.split('-').str[1].head())
print('-='*23)

# Fazemos o split da coluna e extraímos o item na posição 2 (índice 1)
dsa_df['Ano'] = dsa_df['ID_Pedido'].str.split('-').str[1]

# Então conferimos a nova coluna criada
print(dsa_df.head())